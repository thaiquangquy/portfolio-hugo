---
name: check-ai-score
description: This skill should be used when the user wants to check how "AI-sounding" a blog post reads before publishing it — e.g. "run the AI detector on this post", "check ai score for content/posts/x.md", "verify this is human enough before I publish", "/check-ai-score", "/check-ai-score stuck-at-parallel". It runs this repo's local tools/ai-detector CLI (wrapping the open-source houtini-ai/ai-detect) against the given post, or the most recently edited one if none is named, reports the AI-probability score, and compares it against the ~50% phase-1 target established for this repo.
---

# Check AI Score

Run the repo's local AI-text detector (`tools/ai-detector/`, wrapping the
open-source `houtini-ai/ai-detect` CLI) against a blog post before
publishing, without the user needing to remember venv paths or CLI flags.

## Steps

1. **Resolve the target file.**
   - If the user's request names a path, filename, or slug, resolve it
     against `content/posts/` (accept a bare filename like `foo.md`, a slug
     like `foo`, or a full path).
   - If nothing was named, find the most recently modified file under
     `content/posts/*.md`. If `git status` shows one with uncommitted
     changes, prefer that one — it's the likelier "about to publish"
     candidate.
   - Confirm the resolved file with the user in one line before running
     anything, unless it's the obvious current-conversation post.

2. **Ensure the tool is set up.** Check whether `tools/ai-detector/.venv`
   exists.
   - If missing, bootstrap it per `tools/ai-detector/README.md`: confirm a
     Python 3.10+ interpreter is available (`python3.12`, installing via
     `brew install python@3.12` if none exists), create the venv with it,
     then `pip install -r tools/ai-detector/requirements.txt` (plus
     `onnxruntime` if the `--model light` path will be used).
   - If it already exists, just activate it — don't reinstall.

3. **Run the scorer** from `tools/ai-detector/`:
   ```bash
   source .venv/bin/activate
   python strip_frontmatter.py <resolved-path-to-post>
   ```
   Default to the `desklib` model (this repo's primary, RAID-benchmarked
   metric). Only add `--model light` as a secondary opinion if the user asks
   for one — it has a known header-segmentation artifact (see the README)
   that inflates scores on posts with `##` subheadings, so treat it as
   noisier, not authoritative.

4. **Report plainly:**
   - The `model_ai_pct` score and `verdict` from the output.
   - Compare it to this repo's phase-1 target: landing near **50%** (an
     ambiguous, human-or-AI-could-be reading), not 0% or 100%.
     - Well above that band (roughly >65%) → say it reads strongly
       AI-flavored and suggest an editing pass: vary sentence rhythm, add
       concrete specifics, break up clean parallel structure. Don't rewrite
       it yourself unless asked.
     - At or below the band → say it's fine to publish as-is.
   - Note that the run was appended to `tools/ai-detector/scores.log`, so
     scores are comparable across edits over time.

5. **Never edit the post automatically as part of this skill.** Scoring and
   rewriting are separate steps — only score here, and wait for an explicit
   follow-up request before changing any prose.
