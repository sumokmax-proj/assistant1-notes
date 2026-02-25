"""
pdf_extractor.py — Extract and organize text from PDF files instantly.

Usage:
    # Extract single PDF to text
    python pdf_extractor.py extract report.pdf

    # Extract to markdown
    python pdf_extractor.py extract report.pdf --format markdown

    # Extract specific pages only
    python pdf_extractor.py extract report.pdf --pages 1-5

    # Batch extract all PDFs in a folder
    python pdf_extractor.py batch /path/to/folder

    # Search for keyword across all PDFs in a folder
    python pdf_extractor.py search /path/to/folder --keyword "revenue"

    # Get basic info (page count, metadata)
    python pdf_extractor.py info report.pdf

Requirements:
    pip install pymupdf
"""

import argparse
import re
from pathlib import Path
from datetime import datetime

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Missing dependency. Please run: pip install pymupdf")
    exit(1)


def parse_page_range(page_str: str, total_pages: int) -> list[int]:
    pages = set()
    for part in page_str.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-")
            pages.update(range(int(start) - 1, min(int(end), total_pages)))
        else:
            pages.add(int(part) - 1)
    return sorted(pages)


def extract_text_from_pdf(pdf_path: Path, page_indices: list[int] | None = None) -> list[dict]:
    doc = fitz.open(str(pdf_path))
    results = []
    indices = page_indices if page_indices is not None else range(len(doc))
    for i in indices:
        if i >= len(doc):
            continue
        page = doc[i]
        text = page.get_text("text").strip()
        results.append({"page": i + 1, "text": text})
    doc.close()
    return results


def format_as_text(pages: list[dict], include_page_markers: bool = True) -> str:
    parts = []
    for p in pages:
        if include_page_markers:
            parts.append(f"--- Page {p['page']} ---\n{p['text']}")
        else:
            parts.append(p["text"])
    return "\n\n".join(parts)


def format_as_markdown(pages: list[dict], title: str = "") -> str:
    lines = []
    if title:
        lines.append(f"# {title}\n")
    lines.append(f"*Extracted on {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
    for p in pages:
        lines.append(f"## Page {p['page']}\n")
        lines.append(p["text"])
        lines.append("")
    return "\n".join(lines)


def cmd_extract(args):
    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}")
        return

    doc = fitz.open(str(pdf_path))
    total_pages = len(doc)
    doc.close()

    page_indices = None
    if args.pages:
        page_indices = parse_page_range(args.pages, total_pages)
        print(f"Extracting pages: {[p+1 for p in page_indices]}")
    else:
        print(f"Extracting all {total_pages} pages from: {pdf_path.name}")

    pages = extract_text_from_pdf(pdf_path, page_indices)

    if args.format == "markdown":
        output = format_as_markdown(pages, title=pdf_path.stem)
        ext = ".md"
    else:
        output = format_as_text(pages)
        ext = ".txt"

    if args.output:
        out_path = Path(args.output)
    else:
        out_path = pdf_path.with_suffix(ext)

    out_path.write_text(output, encoding="utf-8")
    chars = sum(len(p["text"]) for p in pages)
    print(f"Saved to: {out_path}")
    print(f"Pages extracted: {len(pages)} | Characters: {chars:,}")


def cmd_batch(args):
    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a valid directory.")
        return

    pdfs = list(folder.glob("*.pdf"))
    if not pdfs:
        print("No PDF files found in the folder.")
        return

    out_folder = folder / "extracted"
    out_folder.mkdir(exist_ok=True)

    print(f"Found {len(pdfs)} PDF file(s). Saving to: {out_folder}/\n")
    for pdf_path in pdfs:
        print(f"Processing: {pdf_path.name}...", end=" ", flush=True)
        try:
            pages = extract_text_from_pdf(pdf_path)
            if args.format == "markdown":
                output = format_as_markdown(pages, title=pdf_path.stem)
                out_path = out_folder / pdf_path.with_suffix(".md").name
            else:
                output = format_as_text(pages)
                out_path = out_folder / pdf_path.with_suffix(".txt").name
            out_path.write_text(output, encoding="utf-8")
            print(f"Done ({len(pages)} pages)")
        except Exception as e:
            print(f"FAILED — {e}")

    print(f"\nBatch extraction complete. Results in: {out_folder}")


def cmd_search(args):
    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a valid directory.")
        return

    pdfs = list(folder.glob("*.pdf"))
    if not pdfs:
        print("No PDF files found.")
        return

    keyword = args.keyword.lower()
    print(f"Searching for '{args.keyword}' in {len(pdfs)} PDF(s)...\n")

    total_matches = 0
    for pdf_path in pdfs:
        pages = extract_text_from_pdf(pdf_path)
        file_matches = []
        for p in pages:
            if keyword in p["text"].lower():
                lines = p["text"].split("\n")
                matching_lines = [l.strip() for l in lines if keyword in l.lower() and l.strip()]
                file_matches.append({"page": p["page"], "lines": matching_lines[:3]})

        if file_matches:
            print(f"Found in: {pdf_path.name}")
            for m in file_matches:
                print(f"  Page {m['page']}:")
                for line in m["lines"]:
                    highlighted = re.sub(f"({re.escape(args.keyword)})", r"[\1]", line, flags=re.IGNORECASE)
                    print(f"    ...{highlighted}...")
            total_matches += len(file_matches)
            print()

    if total_matches == 0:
        print(f"No matches found for '{args.keyword}'.")
    else:
        print(f"Total: {total_matches} match(es) found across {len(pdfs)} file(s).")


def cmd_info(args):
    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}")
        return

    doc = fitz.open(str(pdf_path))
    meta = doc.metadata
    print(f"\nFile:       {pdf_path.name}")
    print(f"Pages:      {len(doc)}")
    print(f"Size:       {pdf_path.stat().st_size / 1024:.1f} KB")
    print(f"Title:      {meta.get('title', 'N/A')}")
    print(f"Author:     {meta.get('author', 'N/A')}")
    print(f"Created:    {meta.get('creationDate', 'N/A')}")
    print(f"Modified:   {meta.get('modDate', 'N/A')}")
    total_chars = sum(len(doc[i].get_text()) for i in range(len(doc)))
    print(f"Characters: {total_chars:,}")
    doc.close()


def main():
    parser = argparse.ArgumentParser(description="Extract and organize text from PDF files.")
    subparsers = parser.add_subparsers(dest="command")

    # extract
    p_ext = subparsers.add_parser("extract", help="Extract text from a single PDF")
    p_ext.add_argument("pdf", help="Path to the PDF file")
    p_ext.add_argument("--format", choices=["text", "markdown"], default="text")
    p_ext.add_argument("--pages", help="Page range, e.g. '1-5' or '1,3,5'")
    p_ext.add_argument("--output", help="Output file path (optional)")

    # batch
    p_batch = subparsers.add_parser("batch", help="Extract all PDFs in a folder")
    p_batch.add_argument("folder", help="Folder containing PDF files")
    p_batch.add_argument("--format", choices=["text", "markdown"], default="text")

    # search
    p_search = subparsers.add_parser("search", help="Search for a keyword across PDFs")
    p_search.add_argument("folder", help="Folder containing PDF files")
    p_search.add_argument("--keyword", required=True, help="Keyword to search for")

    # info
    p_info = subparsers.add_parser("info", help="Show PDF metadata and info")
    p_info.add_argument("pdf", help="Path to the PDF file")

    args = parser.parse_args()

    commands = {
        "extract": cmd_extract,
        "batch": cmd_batch,
        "search": cmd_search,
        "info": cmd_info,
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
