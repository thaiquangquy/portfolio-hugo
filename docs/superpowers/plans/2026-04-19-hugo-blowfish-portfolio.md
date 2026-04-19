# Hugo + Blowfish Portfolio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a static Hugo portfolio site with the Blowfish theme, migrating personal data from the existing React portfolio, with automated GitHub Actions deployment to GitHub Pages.

**Architecture:** Hugo static site generator with Blowfish as a git submodule theme. Content lives in `content/` as Markdown files with TOML front matter. Config split across `config/_default/` per Blowfish convention. GitHub Actions builds and pushes to `gh-pages` on every push to `main`.

**Tech Stack:** Hugo (extended, latest), Blowfish theme, GitHub Actions (`peaceiris/actions-hugo@v3`, `peaceiris/actions-gh-pages@v4`), Homebrew (local install)

---

## File Map

| File | Purpose |
|------|---------|
| `config/_default/hugo.toml` | Site title, baseURL, language, theme |
| `config/_default/params.toml` | Blowfish params: author, homepage layout, social links, colors |
| `config/_default/menus.toml` | Top nav: Home, Experience, Blog |
| `content/_index.md` | Home page hero text |
| `content/experience/_index.md` | Experience timeline as Markdown prose |
| `content/posts/boring-tech-wins.md` | Migrated blog post |
| `content/posts/building-in-public.md` | Migrated blog post |
| `content/posts/on-learning-slowly.md` | Migrated blog post |
| `static/img/quy_thai.jpg` | Profile photo (copied from current repo) |
| `static/CNAME` | Custom domain preservation across deploys |
| `.github/workflows/deploy.yml` | CI/CD: build Hugo → push to gh-pages |

---

### Task 1: Install Hugo locally

**Files:** none

- [ ] **Step 1: Install Hugo extended via Homebrew**

```bash
brew install hugo
```

- [ ] **Step 2: Verify installation**

```bash
hugo version
```

Expected output contains: `hugo v0.1xx.x` and `extended`

- [ ] **Step 3: Confirm working directory**

```bash
ls /Users/quythai/workspace/quy/portfolio-hugo
```

Expected: `docs/` directory only (git repo already initialized on `main`)

---

### Task 2: Scaffold Hugo site + add Blowfish as git submodule

**Files:**
- Create: `hugo.toml` (temporary root-level, will be replaced in Task 3)
- Create: `themes/blowfish/` (via submodule)

- [ ] **Step 1: Initialize Hugo site in the existing repo directory**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
hugo new site . --force --format toml
```

Expected: Hugo scaffolds `archetypes/`, `assets/`, `content/`, `layouts/`, `static/`, `themes/`, `hugo.toml`

- [ ] **Step 2: Remove the generated root hugo.toml (config goes in config/_default/)**

```bash
rm /Users/quythai/workspace/quy/portfolio-hugo/hugo.toml
mkdir -p /Users/quythai/workspace/quy/portfolio-hugo/config/_default
```

- [ ] **Step 3: Add Blowfish as a git submodule**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
git submodule add -b main https://github.com/nunocoracao/blowfish.git themes/blowfish
```

Expected: `themes/blowfish/` populated, `.gitmodules` created

- [ ] **Step 4: Commit scaffold + submodule**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
git add .
git commit -m "feat: scaffold Hugo site with Blowfish submodule"
```

---

### Task 3: Configure Hugo

**Files:**
- Create: `config/_default/hugo.toml`
- Create: `config/_default/params.toml`
- Create: `config/_default/menus.toml`

- [ ] **Step 1: Create `config/_default/hugo.toml`**

```toml
baseURL = "https://thaiquangquy.github.io/"
languageCode = "en"
defaultContentLanguage = "en"
title = "Quy Thai-Quang"
theme = "blowfish"

[pagination]
  pagerSize = 10

[taxonomies]
  tag = "tags"
  category = "categories"
```

- [ ] **Step 2: Create `config/_default/params.toml`**

```toml
colorScheme = "ocean"
defaultAppearance = "dark"
autoSwitchAppearance = true

[homepage]
  layout = "profile"
  homepageImage = "img/quy_thai.jpg"
  showRecent = true
  showRecentItems = 3
  showMoreLink = true
  showMoreLinkDest = "/posts"

[author]
  name = "Quy Thai-Quang"
  image = "img/quy_thai.jpg"
  headline = "Full-Stack Software Engineer"
  bio = "A passionate developer who always thrives to work on end to end products which develop sustainable and scalable social and technical systems to create impact."
  links = [
    { github = "https://github.com/thaiquangquy" },
    { linkedin = "https://www.linkedin.com/in/quythai/" },
    { email = "mailto:thaiquangquy0108@gmail.com" },
  ]

[article]
  showDate = true
  showAuthor = false
  showReadingTime = true
  showTableOfContents = false

[list]
  showSummary = true
  groupByYear = false
```

- [ ] **Step 3: Create `config/_default/menus.toml`**

```toml
[[main]]
  name = "Home"
  pageRef = "/"
  weight = 10

[[main]]
  name = "Experience"
  pageRef = "experience"
  weight = 20

[[main]]
  name = "Blog"
  pageRef = "posts"
  weight = 30
```

- [ ] **Step 4: Verify Hugo config parses without errors**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
hugo config
```

Expected: config printed with no errors

- [ ] **Step 5: Commit config**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
git add config/
git commit -m "feat: add Hugo + Blowfish config"
```

---

### Task 4: Create Home page content + copy profile photo

**Files:**
- Create: `content/_index.md`
- Create: `static/img/quy_thai.jpg` (copied from current repo)

- [ ] **Step 1: Copy profile photo**

```bash
cp /Users/quythai/workspace/quy/masterPortfolio-dev/public/quy_thai.jpg \
   /Users/quythai/workspace/quy/portfolio-hugo/static/img/quy_thai.jpg
```

If the file doesn't exist at that path, check:
```bash
find /Users/quythai/workspace/quy/masterPortfolio-dev/public -name "quy_thai*"
```
Copy from wherever it's found.

- [ ] **Step 2: Create `content/_index.md`**

```markdown
---
title: "Quy Thai-Quang"
description: "Full-Stack Software Engineer based in Ho Chi Minh City"
---
```

The homepage layout `profile` in Blowfish pulls bio and social links from `params.toml` automatically — this file only needs the title and description.

- [ ] **Step 3: Start Hugo dev server and verify home page loads**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
hugo server -D
```

Open `http://localhost:1313` — expect: name, bio, social icons (GitHub, LinkedIn, email) visible.

Stop the server with `Ctrl+C`.

- [ ] **Step 4: Commit**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
git add content/_index.md static/img/
git commit -m "feat: add home page content and profile photo"
```

---

### Task 5: Create Experience page

**Files:**
- Create: `content/experience/_index.md`

- [ ] **Step 1: Create `content/experience/_index.md`**

```markdown
---
title: "Experience"
description: "My professional journey"
---

## Full-Stack Software Engineer, Sub Leader
**Personify Inc Vietnam** · Jun 2020 – Present · Ho Chi Minh City, Vietnam

Developed and led projects in IoT data visualization, microservices, and AWS cloud services. Implemented frontend and backend solutions for electric vehicle cloud platforms and user management systems using React, TypeScript, Java, Spring Boot, PostgreSQL, and AWS services.

---

## Team Lead
**Robert Bosch Engineering Vietnam** · Mar 2017 – May 2020 · Ho Chi Minh City, Vietnam

Led a team in developing Human-Machine Interface (HMI) components for speech dialog systems using C/C++ and the ASF framework. Worked on IPC, OOP principles, and product quality improvements. Collaborated with international teams and achieved a zero A/B/C bug milestone.

---

## Software Engineer
**i3 International Inc** · Feb 2016 – Mar 2017 · Ho Chi Minh City, Vietnam

Designed and implemented UI applications using C/C++, Boost framework, and Microsoft Direct2D. Integrated voice command services and contributed to the release of Video Pilot Client v5.
```

- [ ] **Step 2: Verify experience page in dev server**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
hugo server -D
```

Open `http://localhost:1313/experience` — expect: three job entries rendered with headings, bold company names, and paragraph descriptions. Stop with `Ctrl+C`.

- [ ] **Step 3: Commit**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
git add content/experience/
git commit -m "feat: add experience page"
```

---

### Task 6: Migrate blog posts

**Files:**
- Create: `content/posts/boring-tech-wins.md`
- Create: `content/posts/building-in-public.md`
- Create: `content/posts/on-learning-slowly.md`

The existing posts use `category` (singular) and `excerpt` which are not standard Hugo taxonomies. Update front matter: `category` → `categories` (array), `excerpt` → `description`.

- [ ] **Step 1: Copy and update `content/posts/boring-tech-wins.md`**

```markdown
---
title: "Boring Tech Wins"
date: "2024-10-03"
categories: ["tech"]
description: "Every new framework promises to solve the same problems. Most of the time, the boring choice is the right one."
featured: false
---

Every year a new framework launches with the promise of solving the fundamental problems of software development. Every year engineers adopt it with enthusiasm. Every year the same problems resurface, just in a new form.

## The appeal of new

New technology is exciting because it represents possibility. Before you've built anything real with a new tool, you can project onto it all the things you wish your current stack could do. The ergonomics feel better because you haven't hit the edges yet.

This is mostly a cognitive trick.

## What boring tech actually means

When I say "boring tech" I mean: technology with a long track record, a large community, well-understood failure modes, and predictable performance characteristics.

Postgres is boring. Linux is boring. HTTP is boring. These things are boring because they've been run in production at massive scale for decades. Every edge case has been discovered. Every weird behavior is documented. The documentation doesn't have open issues because it was written in 2014 and still works.

## The real cost of novelty

The cost of picking a new technology is rarely the initial adoption. It's everything that comes after:

- Debugging something that has three Stack Overflow results
- Upgrading when breaking changes ship and the migration guide is incomplete
- Onboarding a new engineer who has never used the tool
- Being unable to hire because the talent pool is thin

None of these costs show up in the benchmark blog post.

## My rule of thumb

I use new technology in toy projects. I use boring technology in production. The toy projects are where I figure out if the new thing is actually better — and most of the time, it isn't, just different.

The few times I've bet on new technology in production have been expensive lessons. The many times I've bet on boring technology, I've been grateful for it.
```

- [ ] **Step 2: Copy and update `content/posts/building-in-public.md`**

Copy the file from the source repo and update front matter:
```bash
cp /Users/quythai/workspace/quy/masterPortfolio-dev/src/data/blog/posts/building-in-public.md \
   /Users/quythai/workspace/quy/portfolio-hugo/content/posts/building-in-public.md
```

Then open the file and replace the front matter block with:
```markdown
---
title: "Why I Started Building in Public"
date: "2024-11-15"
categories: ["personal"]
description: "Building in public is uncomfortable. Here's why I think that discomfort is exactly the point."
featured: true
---
```
(Keep the body content unchanged.)

- [ ] **Step 3: Copy and update `content/posts/on-learning-slowly.md`**

```bash
cp /Users/quythai/workspace/quy/masterPortfolio-dev/src/data/blog/posts/on-learning-slowly.md \
   /Users/quythai/workspace/quy/portfolio-hugo/content/posts/on-learning-slowly.md
```

Replace the front matter block with:
```markdown
---
title: "On Learning Slowly"
date: "2024-09-01"
categories: ["thinking"]
description: "We treat learning like a sprint. It might be better as a walk."
featured: false
---
```
(Keep the body content unchanged.)

- [ ] **Step 4: Verify blog list and individual posts in dev server**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
hugo server -D
```

Check:
- `http://localhost:1313/posts` — expect: list of 3 posts with titles and descriptions
- `http://localhost:1313/posts/boring-tech-wins` — expect: full post content rendered

Stop with `Ctrl+C`.

- [ ] **Step 5: Commit**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
git add content/posts/
git commit -m "feat: migrate blog posts"
```

---

### Task 7: Add static assets

**Files:**
- Create: `static/CNAME`

- [ ] **Step 1: Create `static/CNAME`**

```
thaiquangquy.github.io
```

(One line, no trailing newline needed. This file is copied into the build output root so GitHub Pages preserves the custom domain on every deploy.)

- [ ] **Step 2: Commit**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
git add static/CNAME
git commit -m "feat: add CNAME for GitHub Pages custom domain"
```

---

### Task 8: Add GitHub Actions deploy workflow

**Files:**
- Create: `.github/workflows/deploy.yml`

- [ ] **Step 1: Create `.github/workflows/deploy.yml`**

```bash
mkdir -p /Users/quythai/workspace/quy/portfolio-hugo/.github/workflows
```

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

- [ ] **Step 2: Commit**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
git add .github/
git commit -m "feat: add GitHub Actions deploy workflow"
```

---

### Task 9: Verify local build

**Files:** none (verification only)

- [ ] **Step 1: Run full Hugo build**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
hugo --minify
```

Expected: `public/` directory created, output like:
```
Start building sites …
                   | EN
-------------------+-----
  Pages            | 10
  Paginator pages  |  0
  Non-page files   |  0
  Static files     |  4
  Processed images |  0
  Aliases          |  0
  Sitemaps         |  1
  Cleaned          |  0

Total in XXX ms
```

Zero warnings or errors.

- [ ] **Step 2: Check that public/CNAME exists**

```bash
cat /Users/quythai/workspace/quy/portfolio-hugo/public/CNAME
```

Expected: `thaiquangquy.github.io`

- [ ] **Step 3: Add public/ to .gitignore**

```bash
echo "public/" >> /Users/quythai/workspace/quy/portfolio-hugo/.gitignore
echo ".hugo_build.lock" >> /Users/quythai/workspace/quy/portfolio-hugo/.gitignore
```

- [ ] **Step 4: Commit .gitignore**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
git add .gitignore
git commit -m "chore: add .gitignore for Hugo build output"
```

---

### Task 10: Create GitHub repo and push

**Files:** none (git remote operations)

- [ ] **Step 1: Create the GitHub repo via gh CLI**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
gh repo create thaiquangquy/portfolio-hugo --public --source=. --remote=origin
```

If `gh` is not authenticated, run `gh auth login` first.

- [ ] **Step 2: Push main branch**

```bash
cd /Users/quythai/workspace/quy/portfolio-hugo
git push -u origin main
```

- [ ] **Step 3: Verify GitHub Actions triggered**

```bash
gh run list --repo thaiquangquy/portfolio-hugo
```

Expected: one workflow run in `queued` or `in_progress` state.

- [ ] **Step 4: Wait for deploy and confirm gh-pages branch exists**

```bash
gh run watch --repo thaiquangquy/portfolio-hugo
```

After it completes:
```bash
git ls-remote origin gh-pages
```

Expected: a commit SHA next to `refs/heads/gh-pages`

- [ ] **Step 5: Enable GitHub Pages in repo settings**

```bash
gh api repos/thaiquangquy/portfolio-hugo/pages \
  --method POST \
  -f source.branch=gh-pages \
  -f source.path=/
```

If the repo already has Pages configured from a previous deploy, skip this step.

- [ ] **Step 6: Verify site is live**

Open `https://thaiquangquy.github.io` in a browser.

Expected: Blowfish profile page with name "Quy Thai-Quang", bio, social links, and recent posts visible.
