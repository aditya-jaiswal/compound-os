#!/usr/bin/env python3
"""Generate views/team-pending.html (sprintos-style) from team/accountability/team-loops.md.
Pull-free team view: grouped by owner, with a self-filter, status + age badges.
Run: python3 views/build_team_pending.py   (then commit; GitHub Pages serves the HTML)"""
import re, json, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "team" / "accountability" / "team-loops.md"
OUT = ROOT / "views" / "team-pending.html"
DIR_MD = ROOT / "customers" / "customer-directory.md"
ACCOUNTS_DIR = ROOT / "customers" / "accounts"
TODAY = datetime.date.today()

def _slugify(s):
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", (s or "").lower()))

def load_accounts():
    """Canonical account list: names from the customer directory + slugs of account
    folders. Used to tag each board item with the account it belongs to (explicit,
    not fuzzy), so account pages render the right items."""
    names = []
    try:
        for line in DIR_MD.read_text().splitlines():
            line = line.strip()
            if not line.startswith("|"):
                continue
            cell0 = line.strip("|").split("|")[0].strip()
            if not cell0 or cell0.lower() == "account" or set(cell0) <= set("-: "):
                continue
            names.append(cell0)
    except Exception:
        pass
    slugs = set(_slugify(n) for n in names)
    try:
        slugs.update(p.name for p in ACCOUNTS_DIR.iterdir() if p.is_dir())
    except Exception:
        pass
    # longest name first so a longer account name wins over a shorter substring
    return sorted(set(names), key=len, reverse=True), slugs

ACCT_NAMES, ACCT_SLUGS = load_accounts()
ACCT_TAG_RE = re.compile(r"\[acct:([a-z0-9-]+)\]")

def resolve_account(item, notes):
    """Account slug this item belongs to, or '' if none. Priority:
    1) explicit [acct:slug] in Notes, 2) 'Account Name:' prefix in the item,
    3) a unique known-account name mentioned in the item."""
    m = ACCT_TAG_RE.search(notes or "")
    if m:
        return m.group(1)
    pm = re.match(r"\s*([^:]{2,40}?):\s", item or "")
    if pm:
        cand = _slugify(pm.group(1))
        if cand in ACCT_SLUGS:
            return cand
    il = (item or "").lower()
    hits = [n for n in ACCT_NAMES if re.search(r"\b" + re.escape(n.lower()) + r"\b", il)]
    return _slugify(hits[0]) if hits else ""

def parse_rows(md):
    rows = []
    in_tbl = False
    for line in md.splitlines():
        if line.strip().startswith("| ID "):
            in_tbl = True; continue
        if in_tbl:
            if not line.strip().startswith("|"):
                if line.strip() == "": continue
                break
            if set(line.strip()) <= set("|-: "):  # separator row
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 9 or cells[0] == "ID":
                continue
            rows.append(dict(zip(
                ["id","owner","item","source","kind","status","since","due","notes"], cells)))
    return rows

def age_days(since):
    try:
        d = datetime.date.fromisoformat(since)
        return (TODAY - d).days
    except Exception:
        return None

rows = parse_rows(SRC.read_text())
for r in rows:
    r["age"] = age_days(r.get("since",""))
    try:
        r["overdue"] = datetime.date.fromisoformat(r["due"]) < TODAY and r["status"] != "done"
    except Exception:
        r["overdue"] = False
    r["account"] = resolve_account(r.get("item",""), r.get("notes",""))
    r["notes"] = ACCT_TAG_RE.sub("", r.get("notes","")).strip()  # hide the [acct:] tag from display

owners = sorted({r["owner"] for r in rows})
open_items = [r for r in rows if r["status"] != "done"]
blocked = [r for r in rows if r["status"] == "blocked"]
overdue = [r for r in rows if r["overdue"]]

meta = {
    "generated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    "total_open": len(open_items),
    "blocked": len(blocked),
    "overdue": len(overdue),
    "owners": len(owners),
}

TEMPLATE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Team Pending</title>
<style>
:root{--bg:#0b1f3a;--ink:#1f2328;--muted:#6b7280;--line:#e6e9ef;--accent:#4361ee;
--open:#6b7280;--prog:#2563eb;--blocked:#dc2626;--done:#16a34a;--warn:#b45309;}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;color:var(--ink);background:#f6f8fb;}
header{background:var(--bg);color:#fff;padding:22px 28px;}
header h1{margin:0;font-size:20px;letter-spacing:-.3px}
header .sub{opacity:.8;font-size:12px;margin-top:4px}
.stats{display:flex;gap:14px;flex-wrap:wrap;margin-top:14px}
.stat{background:rgba(255,255,255,.08);border-radius:10px;padding:8px 14px;min-width:90px}
.stat .n{font-size:22px;font-weight:700}
.stat .l{font-size:11px;opacity:.8;text-transform:uppercase;letter-spacing:.5px}
.wrap{max-width:1080px;margin:0 auto;padding:20px 28px 60px}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0}
.chip{border:1px solid var(--line);background:#fff;border-radius:999px;padding:6px 14px;font-size:13px;cursor:pointer;color:var(--ink)}
.chip.active{background:var(--bg);color:#fff;border-color:var(--bg)}
.owner{background:#fff;border:1px solid var(--line);border-radius:14px;margin:14px 0;overflow:hidden}
.owner h2{margin:0;padding:12px 16px;font-size:15px;background:#f1f4f9;border-bottom:1px solid var(--line);
display:flex;justify-content:space-between;align-items:center}
.owner h2 .cnt{font-size:12px;color:var(--muted);font-weight:500}
.row{display:grid;grid-template-columns:1fr auto auto auto auto;gap:10px;align-items:center;
padding:11px 16px;border-bottom:1px solid var(--line)}
.row:last-child{border-bottom:none}
.row .item{font-size:14px}
.row .meta{font-size:11px;color:var(--muted);margin-top:2px}
.badge{font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px;white-space:nowrap;text-transform:capitalize}
.b-open{background:#f1f3f7;color:var(--open)}
.b-in-progress{background:#e0ecff;color:var(--prog)}
.b-blocked{background:#fde8e8;color:var(--blocked)}
.b-done{background:#e6f6ec;color:var(--done)}
.src{font-size:10px;color:var(--muted);border:1px solid var(--line);border-radius:6px;padding:2px 7px;text-transform:uppercase;letter-spacing:.4px}
.kind{font-size:10px;font-weight:600;border-radius:6px;padding:2px 7px;text-transform:uppercase;letter-spacing:.4px}
.k-task{background:#eef2ff;color:#4361ee}
.k-follow-up{background:#fff7ed;color:#b45309}
.due{font-size:12px;color:var(--muted)}
.due.over{color:var(--blocked);font-weight:600}
.age.old{color:var(--blocked)}
.note{font-size:13px;color:var(--muted);margin:6px 0 0}
footer{max-width:1080px;margin:0 auto;padding:0 28px 40px;color:var(--muted);font-size:12px}
@media(max-width:640px){.row{grid-template-columns:1fr;gap:4px}}
</style></head>
<body>
<header>
  <h1>Team Pending</h1>
  <div class="sub">What is open teamwide and under whom · generated __GEN__</div>
  <div class="stats">
    <div class="stat"><div class="n">__OPEN__</div><div class="l">Open</div></div>
    <div class="stat"><div class="n">__BLOCKED__</div><div class="l">Blocked</div></div>
    <div class="stat"><div class="n">__OVERDUE__</div><div class="l">Overdue</div></div>
    <div class="stat"><div class="n">__OWNERS__</div><div class="l">Owners</div></div>
  </div>
</header>
<div class="wrap">
  <div class="note">Tip: click your name to see just your items (your self view). The full board is everyone's pending work.</div>
  <div class="filters" id="filters"></div>
  <div id="board"></div>
</div>
<footer>Source of truth: GitHub board + team-loops ledger. This page is published from the team repo (no pull needed to view). Hide closed items by default.</footer>
<script>
const DATA = __DATA__;
let active = "All";
const board = document.getElementById('board');
const filters = document.getElementById('filters');
const owners = [...new Set(DATA.map(r=>r.owner))].sort();
function badge(s){return '<span class="badge b-'+s.replace(/\s/g,'-')+'">'+s+'</span>';}
function render(){
  const rows = DATA.filter(r=>r.status!=='done').filter(r=> active==='All' || r.owner===active);
  const byOwner = {};
  rows.forEach(r=>{(byOwner[r.owner]=byOwner[r.owner]||[]).push(r);});
  board.innerHTML = Object.keys(byOwner).sort().map(o=>{
    const items = byOwner[o].sort((a,b)=>({blocked:0,'in-progress':1,open:2}[a.status]||3)-({blocked:0,'in-progress':1,open:2}[b.status]||3));
    return '<div class="owner"><h2>'+o+' <span class="cnt">'+items.length+' open</span></h2>'+
      items.map(r=>{
        const over = r.overdue ? ' over' : '';
        const old = (r.age!==null && r.age>3 && r.status!=='done') ? ' old' : '';
        const kind = r.kind||'follow-up';
        return '<div class="row"><div><div class="item">'+r.item+'</div>'+
          '<div class="meta">'+(r.notes||'')+'</div></div>'+
          '<span class="kind k-'+kind.replace(/\s/g,'-')+'">'+kind+'</span>'+
          '<span class="src">'+r.source+'</span>'+
          badge(r.status)+
          '<div class="due'+over+'">'+(r.due?('due '+r.due):'')+(r.age!==null?' · <span class="age'+old+'">'+r.age+'d</span>':'')+'</div>'+
        '</div>';
      }).join('')+'</div>';
  }).join('') || '<p style="color:#6b7280">Nothing open here. 🎉</p>';
}
function renderFilters(){
  filters.innerHTML = ['All',...owners].map(o=>'<span class="chip'+(o===active?' active':'')+'" data-o="'+o+'">'+o+'</span>').join('');
  filters.querySelectorAll('.chip').forEach(c=>c.onclick=()=>{active=c.dataset.o;renderFilters();render();});
}
renderFilters();render();
</script>
</body></html>"""

html = (TEMPLATE
    .replace("__DATA__", json.dumps(rows))
    .replace("__GEN__", meta["generated"])
    .replace("__OPEN__", str(meta["total_open"]))
    .replace("__BLOCKED__", str(meta["blocked"]))
    .replace("__OVERDUE__", str(meta["overdue"]))
    .replace("__OWNERS__", str(meta["owners"])))
OUT.write_text(html)
print(f"Wrote {OUT}  ({meta['total_open']} open, {meta['blocked']} blocked, {meta['overdue']} overdue, {meta['owners']} owners)")
