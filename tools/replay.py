#!/usr/bin/env python3
"""Replay the HeatSync Labs MediaWiki revision history as git fast-import streams.

usage: replay.py <scratch-dir> <out-dir>

<scratch-dir> holds history_by_id/<pageid>.json (one per page, from the MediaWiki API),
pages/current_by_id.json, images.json and files/. Two streams are written:
  <out-dir>/wiki.stream  -> the GitHub wiki repo (pages at the root, branch master)
  <out-dir>/repo.stream  -> the source repo (pages under wiki/, branch main)
Every wiki revision becomes one commit authored by the original wiki user.
"""
import json, glob, os, re, sys, gzip, datetime, hashlib, urllib.parse, mimetypes
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import convert

SCRATCH, OUT = sys.argv[1], sys.argv[2]
TOOLS = os.path.dirname(os.path.abspath(__file__))
SOURCE = 'https://wiki.heatsynclabs.org'
IMPORT_DATE = datetime.date.today().isoformat()
IMPORT_NAME = 'HeatSync Labs Wiki Import'
IMPORT_EMAIL = 'wiki-import@wiki.heatsynclabs.invalid'
IMAGE_EXT = {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'}

# ---------------------------------------------------------------- load
current = json.load(open(f'{SCRATCH}/pages/current_by_id.json'))
by_title = {p['title']: p for p in current.values()}
images = json.load(open(f'{SCRATCH}/images.json'))['query']['allimages']
image_by_name = {i['name']: i for i in images}
have_file = {f for f in os.listdir(f'{SCRATCH}/files') if os.path.getsize(f'{SCRATCH}/files/{f}') > 0}
thumb_recovered = set(os.listdir(f'{SCRATCH}/files_thumb_recovered')) if os.path.isdir(f'{SCRATCH}/files_thumb_recovered') else set()

pages = []
for pid, cur in current.items():
    fn = f'{SCRATCH}/history_by_id/{pid}.json'
    revs = [r for r in json.load(open(fn))['revisions'] if '*' in r] if os.path.exists(fn) else []
    if not revs:  # history unavailable: keep at least the current revision
        revs = [r for r in cur['revisions'] if '*' in r]
    revs.sort(key=lambda r: (r['timestamp'], r['revid']))
    if not revs:
        continue
    pages.append(dict(title=cur['title'], ns=cur['ns'], pageid=cur['pageid'], revisions=revs))
print('pages with history', len(pages), 'revisions', sum(len(p['revisions']) for p in pages))

# ---------------------------------------------------------------- filenames
def is_redirect(text):
    return bool(convert.REDIRECT_RE.match(text))

for p in pages:
    p['head'] = p['revisions'][-1]['*']
    p['skip'] = False
    if p['ns'] == 6 and not any(r['*'].strip() for r in p['revisions']):
        p['skip'] = True  # File page that never had a description
    p['file'] = convert.page_filename(p['title'])

groups = {}
for p in pages:
    if not p['skip']:
        groups.setdefault(p['file'].lower(), []).append(p)
for key, grp in groups.items():
    if len(grp) < 2:
        continue
    keep = [p for p in grp if not is_redirect(p['head'])] or grp[:1]
    for p in grp:
        if p not in keep:
            p['skip'] = True; print('skip redirect colliding with target:', p['title'])
    keep.sort(key=lambda p: (p['ns'] != 0 and p['ns'] != 102, p['pageid']))
    # prefer the namespaced (reachable) page for the plain name
    keep.sort(key=lambda p: (p['ns'] == 0, p['pageid']))
    for n, p in enumerate(keep[1:], 2):
        p['file'] = f"{p['file']}-{n}"; print('collision renamed:', p['title'], '->', p['file'])

# ---------------------------------------------------------------- rendering
def render_file_page(title, text):
    name = title.split(':', 1)[1].replace(' ', '_')
    info = image_by_name.get(name)
    target = 'files/' + name
    ext = os.path.splitext(name)[1].lower()
    out = [f'# {title}', '']
    if name in have_file:
        if ext in IMAGE_EXT:
            out.append(f'![{name}]({target})'); out.append('')
        out.append(f'**File:** [{name}]({target})')
        if name in thumb_recovered:
            out.append('')
            out.append('> The original upload was already missing from the old wiki server; this is a reduced-size copy recovered from the Internet Archive.')
    else:
        out.append(f'**File:** `{name}`')
        out.append('')
        out.append(f'> This file was already missing from the old wiki server when the wiki was migrated ({IMPORT_DATE}); only its description survives.')
    if info:
        out.append('')
        out.append(f"*{info['mime']}, {info['size']:,} bytes" + (f", {info['width']}×{info['height']}" if info.get('width') else '') + '*')
    desc = convert.convert(title, text).strip()
    if desc:
        out += ['', '## Description', '', desc]
    return '\n'.join(out) + '\n'

def render(title, ns, text):
    if ns == 6:
        return render_file_page(title, text)
    return convert.convert(title, text)

jobs = {}
for p in pages:
    if p['skip']:
        continue
    for r in p['revisions']:
        key = hashlib.sha1((p['title'] + '\0' + r['*']).encode()).hexdigest()
        r['key'] = key
        jobs.setdefault(key, (p['title'], p['ns'], r['*']))
print('unique renders', len(jobs))
rendered = {}
with ThreadPoolExecutor(8) as ex:
    for key, md in zip(jobs, ex.map(lambda a: render(*a), jobs.values())):
        rendered[key] = md

# ---------------------------------------------------------------- categories, indexes
def categories_of(text):
    return [c.strip() for c in convert.CAT_RE.findall(text)]

cat_members = {}
for p in pages:
    if p['skip'] or p['ns'] == 6:
        continue
    for c in categories_of(p['head']):
        cat_members.setdefault(c, set()).add(p['title'])
head_files = {p['file']: p for p in pages if not p['skip']}

def category_page(cat):
    fn = convert.page_filename('Category:' + cat)
    existing = head_files.get(fn)
    body = rendered[existing['revisions'][-1]['key']].rstrip() + '\n\n' if existing else ''
    members = sorted(cat_members.get(cat, ()), key=str.lower)
    body += '## Pages in this category\n\n'
    body += '\n'.join(f'- [{t}]({convert.page_filename(t) if by_title[t]["title"]==t else t})' for t in members) + '\n'
    return fn, body

def files_index():
    rows = ['# Files', '', f'All {len(images)} files uploaded to the original wiki. Files marked *missing* were already gone from the old server when the wiki was migrated on {IMPORT_DATE}.', '',
            '| File | Type | Size | Description page | Status |', '|---|---|---|---|---|']
    for i in sorted(images, key=lambda i: i['name'].lower()):
        n = i['name']
        link = f'[{n}](files/{n})' if n in have_file else f'`{n}`'
        desc_fn = convert.page_filename('File:' + n)
        desc = f'[description]({desc_fn})' if desc_fn in head_files else ''
        status = 'ok' if n in have_file and n not in thumb_recovered else ('reduced-size (Internet Archive)' if n in have_file else '**missing**')
        rows.append(f"| {link} | {i['mime']} | {i['size']:,} | {desc} | {status} |")
    return '\n'.join(rows) + '\n'

# ---------------------------------------------------------------- fast-import
def q(path):
    if re.search(r'[\s"\\]', path) or path.startswith('"'):
        return '"' + path.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + '"'
    return path

def epoch(ts):
    return int(datetime.datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc).timestamp())

def ident(user):
    slug = re.sub(r'[^a-z0-9]+', '-', user.lower()).strip('-') or 'anonymous'
    name = user.replace('<', '').replace('>', '').replace('\n', ' ') or 'Anonymous'
    return f'{name} <{slug}@wiki.heatsynclabs.invalid>'

class Stream:
    def __init__(self, path, branch, prefix):
        self.f = open(path, 'wb'); self.branch = branch; self.prefix = prefix; self.mark = 0
    def commit(self, who, when, msg, files):
        self.mark += 1
        f = self.f
        f.write(f'commit refs/heads/{self.branch}\nmark :{self.mark}\n'.encode())
        f.write(f'author {who} {when} +0000\ncommitter {who} {when} +0000\n'.encode())
        m = msg.encode(); f.write(f'data {len(m)}\n'.encode()); f.write(m); f.write(b'\n')
        if self.mark > 1:
            f.write(f'from :{self.mark-1}\n'.encode())
        for path, data in files:
            if isinstance(data, str): data = data.encode()
            f.write(f'M 100644 inline {q(self.prefix + path)}\ndata {len(data)}\n'.encode()); f.write(data); f.write(b'\n')
        f.write(b'\n')
    def close(self):
        self.f.write(b'done\n'); self.f.close()

os.makedirs(OUT, exist_ok=True)
streams = [Stream(f'{OUT}/wiki.stream', 'master', ''), Stream(f'{OUT}/repo.stream', 'main', 'wiki/')]

events = sorted(((r['timestamp'], r['revid'], p, r) for p in pages if not p['skip'] for r in p['revisions']), key=lambda e: (e[0], e[1]))

# 1. uploaded files, dated just before the first edit
file_blobs = []
for n in sorted(have_file):
    file_blobs.append(('files/' + n, open(f'{SCRATCH}/files/{n}', 'rb').read()))
msg = (f'Import uploaded files from {SOURCE}\n\n{len(file_blobs)} of {len(images)} files listed by the old wiki could be retrieved; '
       f'the rest were already missing from the old server. See Files.md.\n')
for s in streams:
    s.commit(ident(IMPORT_NAME).replace('<' + 'heatsync-labs-wiki-import@wiki.heatsynclabs.invalid>', '<' + IMPORT_EMAIL + '>'), epoch(events[0][0]) - 1, msg, file_blobs)

# 2. one commit per revision
n = 0
for ts, revid, p, r in events:
    user = r.get('user', '(hidden)')
    comment = (r.get('comment') or '').strip()
    subject = comment if comment else f"Edit {p['title']}"
    if len(subject) > 72:
        subject = subject[:69] + '...'
    body = (f"{subject}\n\n{comment + chr(10) + chr(10) if comment and comment != subject else ''}"
            f"Imported from {SOURCE}\nPage: {p['title']}\nRevision: {revid} ({ts})\nWiki user: {user}\n")
    files = [(p['file'] + '.md', rendered[r['key']])]
    for s in streams:
        s.commit(ident(user), epoch(ts), body, files)
    n += 1
print('revision commits', n)

# 3. generated pages + repo scaffolding
now = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
gen = [('Home.md', open(f'{TOOLS}/wiki_extra/Home.md').read()),
       ('_Sidebar.md', open(f'{TOOLS}/wiki_extra/_Sidebar.md').read()),
       ('_Footer.md', open(f'{TOOLS}/wiki_extra/_Footer.md').read().replace('{DATE}', IMPORT_DATE)),
       ('Files.md', files_index())]
for cat in sorted(cat_members):
    gen.append((category_page(cat)[0] + '.md', category_page(cat)[1]))
gen.append(('Main-Page.md', '*The old wiki\'s Main Page is now **[Home](Home)**.*\n'))
msg = (f'Finish import: Home, sidebar, footer, Files index and category listings\n\n'
       f'Generated from the state of {SOURCE} on {IMPORT_DATE}.\n')
streams[0].commit(ident(IMPORT_NAME).replace('heatsync-labs-wiki-import@wiki.heatsynclabs.invalid', IMPORT_EMAIL), now, msg, gen)

repo_extra = []
for root, _dirs, fnames in os.walk(f'{TOOLS}/repo_extra'):  # os.walk so .github/ and dotfiles are included
    for name in fnames:
        path = os.path.join(root, name)
        repo_extra.append((os.path.relpath(path, f'{TOOLS}/repo_extra'), open(path, 'rb').read()))
for t in ('convert.py', 'wikilinks.lua', 'replay.py'):
    repo_extra.append(('tools/' + t, open(f'{TOOLS}/{t}', 'rb').read()))
hist = {}
for fn in glob.glob(f'{SCRATCH}/history_by_id/*.json'):
    h = json.load(open(fn)); hist[h['title']] = h
repo_extra.append(('archive/mediawiki-history.json.gz', gzip.compress(json.dumps(hist).encode(), 9)))
repo_extra.append(('archive/mediawiki-siteinfo.json', open(f'{SCRATCH}/siteinfo.json', 'rb').read()))
repo_extra.append(('archive/mediawiki-allimages.json', open(f'{SCRATCH}/images.json', 'rb').read()))
repo_extra.append(('archive/missing-files.txt', '\n'.join(sorted(i['name'] for i in images if i['name'] not in have_file)) + '\n'))
repo_extra.append(('archive/thumbnail-recovered-files.txt', '\n'.join(sorted(thumb_recovered)) + '\n'))
s = streams[1]
s.prefix = ''
s.commit(ident(IMPORT_NAME).replace('heatsync-labs-wiki-import@wiki.heatsynclabs.invalid', IMPORT_EMAIL), now,
         msg + '\nAlso adds the publishing workflow, migration tools and the raw MediaWiki archive.\n',
         [('wiki/' + a, b) for a, b in gen] + repo_extra)
for s in streams: s.close()
print('done')
