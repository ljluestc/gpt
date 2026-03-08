#!/usr/bin/env python3
"""Convert DevOps RAG JSONL to markdown for llm_qa ingestion.

Usage:
  python scripts/jsonl_to_markdown.py -i data.jsonl -o database/knowledge_db/devops_rag_qa/
  python scripts/jsonl_to_markdown.py -i devops_beginner_10_en.jsonl -o database/knowledge_db/devops_rag_qa/

Output: One .md file per Q&A, ready for UnstructuredMarkdownLoader.
"""

import argparse
import json
import re
from pathlib import Path


def slug(s: str) -> str:
    """Create filesystem-safe slug from string."""
    s = re.sub(r"[^\w\s-]", "", s.lower())
    s = re.sub(r"[-\s]+", "_", s).strip("_")
    return s[:60] if s else "q"


def item_to_markdown(item: dict, idx: int) -> str:
    """Convert single Q&A item to markdown."""
    q = item.get("question") or item.get("question_en") or item.get("question_zh") or "Question"
    cat = item.get("category", "devops")
    diff = item.get("difficulty", "")
    kw = item.get("keywords", [])
    if isinstance(kw, str):
        kw = [x.strip() for x in kw.split(",") if x.strip()]
    short = item.get("short_answer") or item.get("short_answer_en") or ""
    detailed = item.get("detailed_answer") or item.get("detailed_answer_en") or item.get("detailed_answer_zh") or short
    kp = item.get("key_points", [])
    if isinstance(kp, str):
        kp = [x.strip() for x in kp.split("\n") if x.strip()]
    ex = item.get("example") or item.get("example_en") or ""
    related = item.get("related_topics") or item.get("related_concepts") or []
    if isinstance(related, str):
        related = [x.strip() for x in related.split(",") if x.strip()]

    lines = [
        "# Question",
        q,
        "",
        "# Category",
        f"{cat}" + (f" / {diff}" if diff else ""),
        "",
        "# Keywords",
        ", ".join(kw) if kw else "devops, automation",
        "",
        "# Answer",
        "",
        detailed,
        "",
    ]
    if kp:
        lines.extend(["# Key Points", ""])
        for p in kp:
            lines.append(f"- {p}")
        lines.append("")
    if ex:
        lines.extend(["# Example", "", ex, ""])
    if related:
        lines.extend(["# Related Concepts", ""])
        lines.append(", ".join(related))
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Convert JSONL to markdown for RAG ingestion")
    parser.add_argument("-i", "--input", required=True, help="Input JSONL path")
    parser.add_argument("-o", "--output", required=True, help="Output directory for .md files")
    parser.add_argument("--prefix", default="devops", help="Filename prefix (e.g. devops, jenkins)")
    args = parser.parse_args()

    inp = Path(args.input)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    items = []
    with open(inp, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))

    for i, item in enumerate(items):
        q = item.get("question") or item.get("question_en") or item.get("question_zh") or f"Q{i+1}"
        base = slug(q)
        fid = item.get("id", f"{args.prefix}_{i+1:03d}")
        fname = f"{fid}_{base}.md"
        if len(fname) > 120:
            fname = f"{fid}.md"
        path = out / fname
        md = item_to_markdown(item, i + 1)
        path.write_text(md, encoding="utf-8")

    print(f"Wrote {len(items)} markdown files to {out}")


if __name__ == "__main__":
    main()
