# internetpalace

Portfolio site for Şekip Alp Demirel — hardware, embedded and manufacturing engineering.
Live at **[alpdemirel.tech](https://alpdemirel.tech)**.

Built with [Astro](https://astro.build), deployed to GitHub Pages by Actions on every push to
`main`.

## Running locally

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # static output in dist/
npm run preview  # serve the built output
```

## Layout

```
src/
  content/projects/*.md    one markdown file per project
  content.config.ts        frontmatter schema (status, tech, 3D model, …)
  data/site.ts             bio, experience, skills — the CV content
  data/figures.json        generated; captioned figures pulled from the thesis
  diagrams/*.svg           generated; thesis block diagrams redrawn in English
  components/
    ModelViewer.astro      three.js viewer with exploded-view slider
    FigureGallery.astro    captioned figure gallery with lightbox
    SystemDiagrams.astro   inlines the SVG diagrams, themed via CSS variables
    ProjectCard.astro
  pages/
    index.astro            home
    about.astro            experience and skills
    lab.astro              3D viewer demo and documentation
    projects/[...slug].astro
public/
  figures/<slug>/          generated figure images
  models/                  .glb files for the 3D viewer
  CNAME                    custom domain
scripts/extract_figures.py PDF figure → web image pipeline
```

## Adding a project

Create `src/content/projects/my-project.md`. The filename becomes the URL slug.

```yaml
---
title: My Project
tagline: One sentence that says what it is and why it is interesting.
year: '2025'
status: shipped        # shipped | active | on-hold | research | archived
domain: Home Automation
tech: ['ESP32', 'Altium']
highlights:
  - Short, concrete, specific
figures: my-project    # optional, key into data/figures.json
featured: false
order: 50              # lower sorts first
---

Markdown body.
```

## Adding figures

`scripts/extract_figures.py` pulls embedded images out of a source PDF, converts them to WebP
and writes `src/data/figures.json`. Images are addressed by PDF `xref` rather than by page, so
the mapping stays stable, and each one carries an English title and explanation written in the
script.

To add or re-caption a figure, edit the `FIGURES` table and re-run:

```bash
pip install pymupdf pillow
npm run figures
```

Generated images are committed to the repo so CI does not need access to the source drive. The
source PDF is not published — only the figures.

## Redrawing diagrams

The thesis block diagrams (figures 1, 3, 6, 7 and 8) were Turkish screenshots on hard black
backgrounds, so they are **not** extracted from the PDF. They are redrawn in English by
`scripts/build_diagrams.py`, which emits SVG into `src/diagrams/`:

```bash
npm run diagrams
```

The generator lays out columns and routes wires arithmetically, so alignment is exact. The
SVGs carry no colours of their own — every fill and stroke is a `var(--dg-*)` supplied by
`SystemDiagrams.astro`, which is why they follow the light/dark theme. They are inlined into
the page rather than loaded as `<img>`, since CSS variables do not cross an image boundary.

Two things to watch when editing labels:

- **No arrow glyphs** (`→`). They are missing from some sans fonts and drag the whole text run
  into a serif fallback. Write `via TIP122` rather than `→ TIP122`.
- Use `\n` in a label for a line break; the generator emits `tspan`s and centres them.

## Adding a 3D model

Export a `.glb` with **one top-level object per part you want to explode** — nested children
move with their parent, so sub-assemblies that should stay together can just be grouped. Drop
it in `public/models/` and reference it from the project's frontmatter:

```yaml
model:
  src: /models/my-project.glb
  caption: Controller stack, exploded
  explode: 1.6     # separation distance multiplier
  yOffset: 0       # vertical nudge if the model frames badly
```

The viewer separates parts along each part's own centroid direction, falling back to the
stacking axis for parts near the assembly centre. three.js is code-split and lazy-loaded, so
pages without a model ship no 3D code.

## Deployment

`.github/workflows/deploy.yml` builds and publishes on push to `main`. In the repository
settings, **Pages → Build and deployment → Source** must be set to **GitHub Actions**.

The custom domain is set by `public/CNAME`. DNS for `alpdemirel.tech` needs:

| Type | Name | Value |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `alpdmrel.github.io` |
