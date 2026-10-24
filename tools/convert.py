#!/usr/bin/env python3
"""Convert HeatSync Labs MediaWiki wikitext to GitHub-wiki Markdown."""
import re, subprocess, sys, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
FILTER = os.path.join(HERE, 'wikilinks.lua')

# exact-title overrides for pages whose names collide case-insensitively (mirrored in wikilinks.lua)
OVERRIDES = {'Woodshop': 'Woodshop-Layout'}

def page_filename(title):
    t = title.strip().replace('_', ' ')
    if not t: return ''
    if t.lower() == 'main page': return 'Home'
    t = t[0].upper() + t[1:]
    if t in OVERRIDES: return OVERRIDES[t]
    t = re.sub(r'[ _]+', '-', t).replace(':', '-').replace('/', '-')
    t = re.sub(r'[\\?*"<>|#]', '', t)
    t = re.sub(r'-+', '-', t).strip('-')
    return t

def file_target(name):
    name = name.strip().replace('_', ' ')
    name = name[0].upper() + name[1:]
    return 'files/' + name.replace(' ', '_')

REDIRECT_RE = re.compile(r'^\s*#REDIRECT\s*:?\s*\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', re.I)
CAT_RE = re.compile(r'\[\[\s*Category\s*:\s*([^\]|]+)(?:\|[^\]]*)?\]\]\s*', re.I)
GALLERY_RE = re.compile(r'<gallery[^>]*>(.*?)</gallery>', re.S | re.I)
NOTE_RE = re.compile(r'\{\{\s*note\s*\|(.*?)\}\}', re.S | re.I)
TEMPLATE_RE = re.compile(r'\{\{[^{}]*\}\}')
MAGIC_RE = re.compile(r'__(NOTOC|TOC|FORCETOC|NOEDITSECTION|NEWSECTIONLINK|HIDDENCAT|NOGALLERY)__')

def _gallery(m):
    out = ['']
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line: continue
        parts = line.split('|', 1)
        name = re.sub(r'^(File|Image):', '', parts[0].strip(), flags=re.I)
        cap = parts[1].strip() if len(parts) > 1 else ''
        out.append(f'[[File:{name}|thumb|{cap}]]' if cap else f'[[File:{name}|thumb]]')
    out.append('')
    return '\n'.join(out)

def preprocess(wikitext):
    """Return (wikitext, categories)."""
    cats = [c.strip() for c in CAT_RE.findall(wikitext)]
    text = CAT_RE.sub('', wikitext)
    text = GALLERY_RE.sub(_gallery, text)
    text = NOTE_RE.sub(lambda m: "''Note:'' " + m.group(1), text)
    text = TEMPLATE_RE.sub('', text)
    text = MAGIC_RE.sub('', text)
    return text, cats

def pandoc(wikitext):
    r = subprocess.run(['pandoc', '-f', 'mediawiki', '-t', 'gfm', '--wrap=none',
                        '--lua-filter', FILTER], input=wikitext, text=True,
                       capture_output=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip())
    return r.stdout

def postprocess(md):
    # pandoc escapes some chars gfm does not need escaped; leave as-is for fidelity.
    md = re.sub(r'\n{3,}', '\n\n', md)
    # nested link inside an image's alt text (from gallery captions): keep the plain text
    md = re.sub(r'!\[\[([^\]]*)\]\([^)]*\)\]', r'![\1]', md)
    return md.strip() + '\n'

def convert(title, wikitext):
    """Convert one page. Returns markdown."""
    m = REDIRECT_RE.match(wikitext)
    if m:
        target = m.group(1).strip()
        ftarget = file_target(target.split(':', 1)[1]) if re.match(r'^(File|Image|Media):', target, re.I) else page_filename(target.split('#')[0])
        return f'*This page redirects to **[{target}]({ftarget})**.*\n'
    text, cats = preprocess(wikitext)
    try:
        md = pandoc(text)
    except Exception as e:
        md = ('> **Note:** this revision could not be converted automatically; the original wikitext is preserved below.\n\n'
              '```mediawiki\n' + wikitext.replace('```', '` ` `') + '\n```\n')
        sys.stderr.write(f'pandoc failed for {title!r}: {e}\n')
    md = postprocess(md)
    if cats:
        links = ', '.join(f'[{c}]({page_filename("Category:" + c)})' for c in cats)
        md += f'\n---\n*Categories: {links}*\n'
    return md

if __name__ == '__main__':
    import json
    title = sys.argv[1]
    sys.stdout.write(convert(title, sys.stdin.read()))
