# Portfolio — Final Verification Audit

**Project:** Manish Kumar · Crea Graphix — portfolio site
**Audited:** 2026-08-25
**Scope:** End-to-end check of the content-sync pipeline, the live site, the redesigned CV, the reorganized asset tree, and GitHub readiness.

**Verdict:** ✅ **GitHub-ready.** The site is internally consistent and deployable today. Every asset the site references exists on disk, all scripts parse, no file breaks GitHub's 100 MB limit, and — following the authorized cleanup below — `assets/` is now **214 MB** (down from 3.4 GB). The repository is lean enough for a normal clone and for GitHub Pages.

---

## 1. Folder structure

```
Portfolio New/
├── index.html                 · single page, renders from content.js
├── css/style.css              · 61 KB, design system + responsive
├── js/main.js                 · renders projects, certs, hero, lightbox, nav-assistant
├── content.config.json        · human-editable manifest (source of truth)
├── content.js                 · generated → window.SITE_CONTENT (do not hand-edit)
├── sync.js                    · zero-dependency Node build (config → content.js)
├── Sync-Portfolio.bat         · double-click sync (Windows)
├── sync.command               · double-click sync (macOS/Linux)
├── Manish-Kumar-CV.pdf        · on-brand 1-page CV (linked from the site)
├── README.md / README-SYNC.md · project + workflow docs
├── .gitignore                 · excludes sources, archives, side folders
└── assets/
    ├── profile/               · hero photo
    ├── certificates/          · 9 certificate images
    ├── global/
    └── projects/<slug>/gallery/   · 14 project folders
        └── PROJECT-INDEX.md    · human-readable map of curated media
```

Structure is clean, conventional, and GitHub-friendly: lowercase-slug project folders, a single `assets/` root, one source of truth (`content.config.json`), and no build dependencies.

---

## 2. Files moved / deleted

| Action | Result |
|---|---|
| Assets reorganized into `assets/projects/<slug>/gallery/` | ✔ 14 project folders, sanitized slugs |
| Design sources removed (PSD/PSB/AI/EPS + ZIPs) | ✔ none remain in the tree |
| Non-curated video removed | ✔ 5 videos remain, all referenced |
| Deletion log written | `DELETED-FILES.log` (git-ignored) |
| Largest per-file blocker (was ~25 GB / 33 files > 100 MB) | ✔ **cleared** — no file now exceeds 100 MB |
| **Non-curated raw pool removed (authorized 2026-08-25)** | ✔ **1,840 files / 3,217 MB deleted**, 172 empty subfolders pruned |

The first cleanup removed design sources and surplus video; the second (this audit) removed the non-curated image/PDF working pool. Every deletion is manifested in `DELETED-FILES.log`. **All 85 curated files were preserved** and independently re-verified after deletion.

---

## 3. References — all resolve

| Check | Result |
|---|---|
| Asset paths referenced by `content.js` | **99 / 99 present**, 0 missing |
| `index.html` local links (`css/style.css`, `js/main.js`, `content.js`, CV) | ✔ all exist |
| Hardcoded/stale asset paths in `js/main.js` | ✔ none — every media URL comes from `SITE_CONTENT` |
| Media URLs passed through `encodeURI()` (spaces/parens safe) | ✔ confirmed |
| CV link (`index.html` → `Manish-Kumar-CV.pdf`) + chatbot rule | ✔ points at the new CV |
| `sync.js` run | ✔ clean — 14 projects, 9 certificates |
| JS syntax (`node --check`) on main.js / sync.js / content.js | ✔ all pass |

---

## 4. Asset footprint (after cleanup)

| Group | Files | Size |
|---|---:|---:|
| **Published** (what the site actually loads) | 85 | **214 MB** |
| Retained non-site files (2 alt profile photos, `README.md`, `PROJECT-INDEX.md`) | 4 | < 1 MB |
| **Total in `assets/`** | 89 | **214 MB** |

`assets/` went from **1,929 files / 3.4 GB → 89 files / 214 MB**. The only non-published files left are two alternate headshots and two docs — all intentional. The largest remaining file is ~38 MB (well under the 100 MB limit).

---

## 5. Potential problems

1. **~~Repo weight~~ — resolved.** The non-curated 3.2 GB pool has been deleted (authorized). `assets/` is now 214 MB.
2. **Empty lightbox `src`.** `index.html` has `<img src="" id="lightbox-img">`; JS fills it on click. Harmless in modern browsers (a tiny validation nit). One-line fix available if you want it spotless.
3. **Git not initialized.** The folder is not yet a git repo — run `git init` (and confirm `.gitignore` is respected) before the first push.
4. **Fonts in the CV are stand-ins.** Space Grotesk / Inter / JetBrains Mono aren't installed here and the network is blocked, so the CV embeds close stand-ins (Lato + Source Code Pro). Swappable if you provide the real `.ttf` files.

---

## 6. GitHub readiness

| Item | Status |
|---|---|
| No file > 100 MB (hard limit) | ✔ Pass |
| `.gitignore` excludes sources, archives, `EXAMPLE_PORTFOLIO_URL/`, `Ai studio/`, `*.log` | ✔ |
| Dependency-free (no `node_modules` to commit) | ✔ |
| Total repo size healthy (< ~1 GB) | ✔ **214 MB** |
| Git initialized | ✖ not yet — run `git init` |

**Items already git-ignored (won't be pushed):** `EXAMPLE_PORTFOLIO_URL/` (43 MB), `crea-graphix-—-manish-kumar-portfolio - Ai studio/` (370 KB) + its `.zip` (308 KB), `DELETED-FILES.log` (now ~230 KB).

### Remaining step to publish

Only `git init` → commit → push (or point GitHub Pages at the folder). No size remediation is needed anymore — the repo is lean. The two side folders and the deletion log stay local via `.gitignore`.
