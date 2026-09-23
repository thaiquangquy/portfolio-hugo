# ai-detector

Dev-only tool. Scores how "AI-sounding" a blog post's prose reads, using the
open-source [`ai-detect`](https://github.com/houtini-ai/ai-detect) CLI (MIT
licensed), which wraps `desklib/ai-text-detector-v1.01`, a DeBERTa-v3-large
model ranked #1 on the RAID detection benchmark. Runs fully local/offline
after a one-time model download — no API key, no upload.

This is isolated from the Hugo site itself: nothing here is referenced by
`layouts/`, `config/`, or the build, and it is not wired into
`.github/workflows/deploy.yml`.

## Setup

`ai-detect` requires **Python 3.10+**. The repo's system `python3` may be
older (macOS ships 3.9) — if so, install a newer one first, e.g.:

```
brew install python@3.12
```

Then, from this directory:

```
cd tools/ai-detector
/opt/homebrew/bin/python3.12 -m venv .venv   # or your python3.10+ path
source .venv/bin/activate
pip install -r requirements.txt
```

First invocation downloads model weights from Hugging Face into
`~/.cache/huggingface` (outside the repo, not gitignored here since it's
never inside the repo tree):
- `--model desklib` (default): ~1.7GB, the RAID-benchmarked model.
- `--model light`: ~126MB ONNX model, faster, slightly less validated.

## Usage

```
source .venv/bin/activate
python strip_frontmatter.py ../../content/posts/some-post.md
python strip_frontmatter.py ../../content/posts/some-post.md --model light
```

The script strips the post's YAML frontmatter (metadata isn't prose and
would skew scoring), runs `ai-detect --json` against the remaining body
text, prints the overall AI-probability score (`model_ai_pct`, 0-100) plus
the sentence-length-uniformity verdict, and appends a line to
`scores.log` (gitignored) for comparing runs over time.

Raw CLI, if you want the full per-sentence diagnostics instead:

```
ai-detect --file some-file.txt --json
ai-detect --help
```

## Confirmed CLI interface (ai-detect 1.0.0)

```
ai-detect [--file FILE] [--text TEXT] [--compare FILE1 FILE2] [--json]
          [--model {desklib,light}] [--device {auto,cpu,cuda}]
```

JSON output shape used by the wrapper:

```json
{
  "sentences": [{"sentence": "...", "label": "AI|Human", "ai_prob": 0.51, "human_prob": 0.49, "diagnostics": []}],
  "model_ai_pct": 72.8,
  "text_metrics": {"cv": 0.05, "verdict": "very uniform (AI-like)"}
}
```
