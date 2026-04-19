# Hugo + Blowfish Portfolio — Design Spec

**Date:** 2026-04-19  
**Status:** Approved

## Overview

Replace the current React-based portfolio at `thaiquangquy.github.io` with a static Hugo site using the Blowfish theme. Personal data is migrated from the existing `portfolio.js`. MVP scope: Home, Experience, Blog.

## Repository

- **Path:** `~/workspace/quy/portfolio-hugo`
- **GitHub:** `github.com/thaiquangquy/portfolio-hugo` (new repo)
- **Default branch:** `main`
- **Deploy branch:** `gh-pages`

## Site Structure

```
portfolio-hugo/
├── config/
│   └── _default/
│       ├── hugo.toml          # site title, baseURL, language
│       ├── params.toml        # Blowfish theme params (colors, author info)
│       └── menus.toml         # nav: Home, Experience, Blog
├── content/
│   ├── _index.md              # Home page (bio, social links)
│   ├── experience/
│   │   └── _index.md          # Experience timeline
│   └── posts/                 # Blog posts
│       ├── boring-tech-wins.md
│       ├── building-in-public.md
│       └── on-learning-slowly.md
├── static/
│   └── img/                   # quy_thai.jpg and any logos
│   └── CNAME                  # preserves custom domain across deploys
├── themes/
│   └── blowfish/              # git submodule (not copied)
└── .github/
    └── workflows/
        └── deploy.yml         # Hugo build → gh-pages branch
```

## Content & Data Mapping

### Home (`content/_index.md`)
- Name: "Quy Thai-Quang"
- Bio: from `greeting.subTitle` in `portfolio.js`
- Social links (GitHub, LinkedIn, Gmail): configured in `params.toml` using Blowfish's built-in `socialLinks`
- Profile photo: `quy_thai.jpg` → `static/img/`

### Experience (`content/experience/_index.md`)
Three work entries from `portfolio.js`, rendered as a chronological Markdown list:
1. Full-Stack Software Engineer, Sub Leader — Personify Inc (Jun 2020–Present)
2. Team Lead — Robert Bosch Engineering Vietnam (Mar 2017–May 2020)
3. Software Engineer — i3 International Inc (Feb 2016–Mar 2017)

No custom shortcodes for MVP — plain Markdown prose.

### Blog (`content/posts/`)
Three existing Markdown posts migrated as-is. Front matter (`title`, `date`, `excerpt`) already compatible with Hugo. Blowfish renders a post list and individual pages automatically.

### Out of MVP Scope
Skills section, certifications, competitive sites, contact form — can be added in a future iteration.

## Theme

- **Blowfish** installed as a git submodule: `themes/blowfish`
- Configured via `config/_default/params.toml`
- Color scheme and layout to match the aesthetic of `https://n9o.xyz/`

## Deployment

GitHub Actions workflow (`.github/workflows/deploy.yml`) triggers on push to `main`:

1. Checkout with submodules (pulls Blowfish theme)
2. Install Hugo (latest, extended)
3. Build: `hugo --minify` → outputs to `./public`
4. Push `./public` to `gh-pages` branch via `peaceiris/actions-gh-pages`

GitHub Pages is configured to serve from the `gh-pages` branch. A `CNAME` file in `static/` ensures the custom domain (`thaiquangquy.github.io`) survives each deploy.

```yaml
name: Deploy Hugo site to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true
          fetch-depth: 0

      - uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: 'latest'
          extended: true

      - run: hugo --minify

      - uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
          publish_branch: gh-pages
```
