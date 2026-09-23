#!/usr/bin/env python3
"""Score a markdown blog post's AI-generated-text probability via ai-detect.

Strips Hugo's YAML frontmatter (the leading `---` ... `---` block) before
scoring, since frontmatter is metadata, not prose, and would skew the result.
"""
import argparse
import datetime
import json
import subprocess
import sys
import tempfile
from pathlib import Path

LOG_PATH = Path(__file__).parent / "scores.log"


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Path to a markdown post (frontmatter is stripped automatically)")
    parser.add_argument(
        "--model", choices=["desklib", "light"], default="desklib",
        help="Detection model to pass through to ai-detect: 'desklib' (full, RAID #1) or "
             "'light' (126MB ONNX, faster) (default: desklib)",
    )
    args = parser.parse_args()

    md_path = Path(args.path)
    body = strip_frontmatter(md_path.read_text())

    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as tmp:
        tmp.write(body)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["ai-detect", "--file", tmp_path, "--model", args.model, "--json"],
            capture_output=True, text=True,
        )
    finally:
        Path(tmp_path).unlink(missing_ok=True)

    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        return result.returncode

    stdout = result.stdout
    json_start = stdout.find("{")
    raw_json = stdout[json_start:] if json_start != -1 else stdout

    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError:
        print("Could not parse ai-detect output as JSON; raw output below:\n")
        print(stdout)
        return 1

    score = data.get("model_ai_pct")
    verdict = data.get("text_metrics", {}).get("verdict")

    print(f"{md_path.name}: model_ai_pct={score}%  model={args.model}  verdict={verdict}")

    with LOG_PATH.open("a") as log:
        log.write(f"{datetime.datetime.now().isoformat()}\t{md_path}\t{args.model}\t{score}\t{verdict}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
