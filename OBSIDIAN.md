# Reading this course in Obsidian

⬅ [Course home](README.md)

The course is written as GitHub-flavoured Markdown. Obsidian reads the same files but
renders them with its own engine and its own defaults — so out of the box it looks
different. **Three settings fix almost all of it**, and this repository now ships them.

> **Honest caveat:** I could not test this inside Obsidian while writing it. The settings
> below follow from how the two renderers differ, and the fragile constructs have been
> removed. If something still looks wrong, tell me what and I will fix it.

---

## The good news: it is already configured

`.obsidian/app.json` is **committed to this repository**. Open the repo folder as a vault
and Obsidian picks the settings up automatically:

```json
{
  "strictLineBreaks": true,
  "readableLineLength": false,
  "defaultViewMode": "preview",
  "useMarkdownLinks": true,
  "newLinkFormat": "relative"
}
```

**Open it as a vault:** Obsidian → *Open folder as vault* → choose the repository folder
(for example `...\Python\Python projects\Python-basics`). Do **not** create a new vault
and copy files in — you would lose the settings and the Git history.

If the settings do not seem to apply, Obsidian may have written its own on first open.
Set them by hand — they are all in *Settings → Editor*:

| Setting | Set it to | Why |
|---------|-----------|-----|
| **Strict line breaks** | **ON** | 🌟 the big one — see below |
| **Readable line length** | **OFF** | wide tables need the full window |
| **Default view for new tabs** | **Reading view** | so diagrams render immediately |
| **Use [[Wikilinks]]** | **OFF** | keeps links portable back to GitHub |
| **New link format** | **Relative path to file** | same reason |

---

## Why "Strict line breaks" matters so much

This is the setting that makes the difference between "looks broken" and "looks like
GitHub".

The course's prose is **hard-wrapped at about 90 characters** — 3,259 lines of it. In
Markdown those are *soft* wraps: a single newline inside a paragraph is just a space.

```markdown
This is one paragraph that happens to be
written across three source lines because
90 characters is a comfortable width.
```

| | Renders as |
|---|---|
| **GitHub** | one flowing paragraph |
| **Obsidian, Strict line breaks OFF** (its default) | three separate short lines ❌ |
| **Obsidian, Strict line breaks ON** | one flowing paragraph ✅ |

Obsidian's default is the note-taker's convention (Enter means a new line). GitHub
follows the CommonMark standard. **Turning "Strict line breaks" on makes Obsidian follow
CommonMark too** — which is what the course is written for.

---

## What renders identically in both

| | |
|---|---|
| Headings, **bold**, *italic*, lists | ✅ |
| Tables | ✅ |
| Fenced code blocks with syntax highlighting | ✅ |
| Blockquotes and the `> **⚠️ …**` warning boxes | ✅ |
| Horizontal rules, emoji | ✅ |
| **Mermaid diagrams** (all 41) | ✅ in Reading view or Live Preview |
| **`<details>` collapsible answer blocks** (all 58) | ✅ — they have the blank line after `<summary>` that both renderers need |
| Links to other files | ✅ |
| `- [ ]` checkboxes | ✅ — Obsidian makes them clickable, which is nicer |

### Diagrams only render in Reading view

Mermaid is drawn in **Reading view** and **Live Preview**, never in **Source mode**.
If you see raw ```mermaid text, press **Ctrl-E** to switch view. The committed setting
opens files in Reading view so this should not come up.

---

## The one thing that genuinely does not travel: `#anchor` links

There are about 100 links in the course that jump to a specific heading, like:

```markdown
[Exercise 1.11](exercises.md#exercise-111--count-the-zeros)
```

The two apps compute heading anchors **differently**:

| | Anchor for the heading `## Exercise 1.1 — Types warm-up` |
|---|---|
| **GitHub** | `#exercise-11--types-warm-up` — lowercased, punctuation stripped, each space a dash |
| **Obsidian** | matches the **heading text itself** |

So in Obsidian those links **open the right file but do not jump to the right heading.**
No renderer setting can reconcile this — the algorithms simply differ.

**This is deliberately not "fixed".** The repository's primary home is GitHub, which is
where your colleagues will read it, and rewriting 100 links for Obsidian would break them
there. Nothing is lost: the link still opens the correct file.

**Working around it in Obsidian:**

- **Ctrl-O** then type the heading — Obsidian's quick switcher finds headings directly
- **Ctrl-F** inside the file for the exercise number
- the outline panel (*Settings → Core plugins → Outline*) lists every heading, clickable

---

## Optional extras worth turning on

*Settings → Core plugins:*

| Plugin | Why it helps here |
|--------|-------------------|
| **Outline** | a clickable table of contents per lesson — largely replaces the anchor links |
| **Graph view** | shows how the 30 lesson files link together; genuinely useful for seeing the course shape |
| **Search** | `path:course/ range(` finds every mention across the lessons |
| **Page preview** | hover a link to peek at the target without leaving the page |

*Appearance:* any theme works. The course uses no custom CSS and no colour assumptions.

---

## What NOT to do

| ❌ | Why |
|---|---|
| Create a new vault and copy the `.md` files into it | you lose the committed settings, the Git history and every relative link |
| Let Obsidian "fix" links on rename | it rewrites them to Obsidian's format and they break on GitHub |
| Edit lesson files in Obsidian and forget to commit | Obsidian writes straight to disk; run `git status` before you close |
| Install a Markdown-formatter plugin | several of them re-wrap paragraphs or convert links, producing a huge meaningless diff |

---

## If you edit the course in Obsidian

Obsidian saves directly to the files, so your changes are real Git changes:

```bash
git status                       # see what you touched
bash tools/run-all-scripts.sh    # 80/80 if you changed any .py
python3 tools/check-links.py     # 469/469 if you changed links
python3 tools/check-tables.py    # 122/122 if you touched a table
git add -A && git commit -m "..." && git push
```

Those three checks are exactly why they exist — they catch a broken link or a ragged
table before your colleagues see it.

---

## Quick diagnosis

| What you see | Fix |
|--------------|-----|
| Prose broken into short ragged lines | **Strict line breaks → ON** |
| Raw ```mermaid text instead of a diagram | **Ctrl-E** for Reading view |
| Tables squeezed into a narrow column | **Readable line length → OFF** |
| A link opens the file but not the heading | expected — see the anchor section above |
| An answer block shows raw `**(a)**` markup | report it; the blank line after `<summary>` should prevent this |
| A link does not resolve at all | **Use [[Wikilinks]] → OFF**, and open the *repository folder* as the vault |
