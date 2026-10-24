-- pandoc Lua filter: MediaWiki links/images -> GitHub wiki targets
local function trim(s) return (s:gsub("^%s+", ""):gsub("%s+$", "")) end

-- exact-title overrides for pages whose names collide case-insensitively
local overrides = { ["Woodshop"] = "Woodshop-Layout" }

local function pagename(t)
  t = t:gsub("^:", "")
  t = t:gsub("_", " ")
  t = trim(t)
  if t == "" then return "" end
  if t:lower() == "main page" then return "Home" end
  t = t:sub(1, 1):upper() .. t:sub(2)
  if overrides[t] then return overrides[t] end
  t = t:gsub("[ _]+", "-")
  t = t:gsub(":", "-"):gsub("/", "-")
  t = t:gsub("[\\%?%*\"<>|#]", "")
  t = t:gsub("%-+", "-"):gsub("^%-", ""):gsub("%-$", "")
  return t
end

local function anchor(f)
  -- MediaWiki fragment -> GitHub heading anchor
  f = f:gsub("%.(%x%x)", function(h) return string.char(tonumber(h, 16)) end)
  f = f:gsub("_", " ")
  f = trim(f):lower()
  f = f:gsub("[^%w%s%-]", "")
  f = f:gsub("%s+", "-")
  return f
end

local function filename(fn)
  fn = trim((fn:gsub("_", " ")))
  fn = fn:sub(1, 1):upper() .. fn:sub(2)
  return "files/" .. fn:gsub(" ", "_")
end

local image_ext = { jpg = true, jpeg = true, png = true, gif = true, svg = true, webp = true }

function Link(el)
  local is_wiki = el.classes:includes("wikilink") or el.title == "wikilink"
  if not is_wiki then return el end
  local tgt = el.target:gsub("%%20", " ")
  local page, frag = tgt:match("^([^#]*)#?(.*)$")
  local fn = page:match("^:?[Ff]ile:(.*)") or page:match("^:?[Ii]mage:(.*)") or page:match("^:?[Mm]edia:(.*)")
  local wp = page:match("^[Ww]ikipedia:(.*)") or page:match("^[Ww]:(.*)")
  if page:match("^https?://") then
    el.target = page
  elseif fn then
    el.target = filename(fn)
  elseif wp then
    el.target = "https://en.wikipedia.org/wiki/" .. (wp:gsub(" ", "_"))
  elseif trim(page) == "" then
    el.target = "#" .. anchor(frag)
  else
    local p = pagename(page)
    if frag ~= "" then p = p .. "#" .. anchor(frag) end
    el.target = p
  end
  el.title = ""
  el.classes = {}
  el.attributes = {}
  return el
end

function Image(el)
  local src = el.src:gsub("%%20", " ")
  src = src:gsub("^[Ff]ile:", ""):gsub("^[Ii]mage:", "")
  local ext = src:match("%.(%w+)$")
  local target = filename(src)
  el.src = target
  el.title = ""
  if ext and image_ext[ext:lower()] then
    -- drop size/alignment attributes; GitHub ignores them anyway
    el.attributes = {}
    return el
  end
  -- non-image file (pdf, zip, doc): emit a link instead of a broken image
  local label = el.caption
  if #label == 0 then label = { pandoc.Str(src) } end
  return pandoc.Link(label, target)
end

-- Figures (thumb images with captions) -> plain image paragraph + italic caption,
-- so GitHub renders them without raw <figure> HTML.
function Figure(el)
  local blocks = {}
  for _, b in ipairs(el.content) do table.insert(blocks, b) end
  local cap = pandoc.utils.blocks_to_inlines(el.caption.long or {})
  if #cap > 0 then
    table.insert(blocks, pandoc.Para({ pandoc.Emph(cap) }))
  end
  return blocks
end
