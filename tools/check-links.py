"""Check every relative markdown link and every #anchor in the course."""
import re, sys
from pathlib import Path

ROOT = Path(".")
md_files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)

def slug(heading):
    """GitHub's anchor algorithm: lowercase, strip non-word, spaces->dashes."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)          # drop punctuation & emoji
    # GitHub replaces EACH space with a dash - it does not collapse runs.
    return s.replace(" ", "-")

# collect the anchors each file offers
anchors = {}
for p in md_files:
    found = set()
    for line in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            found.add(slug(m.group(2)))
    anchors[p.resolve()] = found

LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
bad = []
checked = 0
for p in md_files:
    for text, target in LINK.findall(p.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        checked += 1
        path_part, _, anchor = target.partition("#")
        if path_part:
            dest = (p.parent / path_part).resolve()
            if not dest.exists():
                bad.append(f"{p}: missing file -> {target}")
                continue
        else:
            dest = p.resolve()
        if anchor:
            if dest.suffix != ".md":
                continue
            if anchor not in anchors.get(dest, set()):
                bad.append(f"{p}: missing anchor -> {target}")

print(f"checked {checked} relative links across {len(md_files)} files")
if bad:
    print(f"\n{len(bad)} BROKEN:")
    for b in bad:
        print("  " + b)
    sys.exit(1)
print("all relative links and anchors resolve")
