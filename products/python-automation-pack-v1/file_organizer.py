"""
file_organizer.py — Automatically organize files in any folder.

Usage:
    python file_organizer.py /path/to/folder
    python file_organizer.py /path/to/folder --mode date
    python file_organizer.py /path/to/folder --mode type
    python file_organizer.py /path/to/folder --mode both
    python file_organizer.py /path/to/folder --dry-run
"""

import os
import shutil
import argparse
from pathlib import Path
from datetime import datetime

FILE_TYPE_MAP = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic", ".tiff"],
    "Videos":     [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
    "Audio":      [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Documents":  [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".md"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "Presentations": [".ppt", ".pptx", ".odp"],
    "Archives":   [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2"],
    "Code":       [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".go", ".rs"],
    "Data":       [".json", ".xml", ".yaml", ".yml", ".toml", ".sql"],
    "Executables": [".exe", ".dmg", ".pkg", ".deb", ".rpm", ".sh", ".bat"],
}


def get_file_type(extension: str) -> str:
    ext = extension.lower()
    for category, extensions in FILE_TYPE_MAP.items():
        if ext in extensions:
            return category
    return "Others"


def get_file_date(filepath: Path) -> str:
    timestamp = filepath.stat().st_mtime
    return datetime.fromtimestamp(timestamp).strftime("%Y/%m")


def organize_by_type(folder: Path, dry_run: bool) -> int:
    moved = 0
    for item in folder.iterdir():
        if item.is_dir():
            continue
        category = get_file_type(item.suffix)
        dest_dir = folder / category
        dest = dest_dir / item.name
        if dry_run:
            print(f"  [DRY RUN] {item.name} → {category}/")
        else:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(dest))
            print(f"  Moved: {item.name} → {category}/")
        moved += 1
    return moved


def organize_by_date(folder: Path, dry_run: bool) -> int:
    moved = 0
    for item in folder.iterdir():
        if item.is_dir():
            continue
        date_path = get_file_date(item)
        dest_dir = folder / date_path
        dest = dest_dir / item.name
        if dry_run:
            print(f"  [DRY RUN] {item.name} → {date_path}/")
        else:
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(item), str(dest))
            print(f"  Moved: {item.name} → {date_path}/")
        moved += 1
    return moved


def organize_by_both(folder: Path, dry_run: bool) -> int:
    moved = 0
    for item in folder.iterdir():
        if item.is_dir():
            continue
        category = get_file_type(item.suffix)
        date_path = get_file_date(item)
        dest_dir = folder / category / date_path
        dest = dest_dir / item.name
        if dry_run:
            print(f"  [DRY RUN] {item.name} → {category}/{date_path}/")
        else:
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(item), str(dest))
            print(f"  Moved: {item.name} → {category}/{date_path}/")
        moved += 1
    return moved


def main():
    parser = argparse.ArgumentParser(
        description="Automatically organize files in a folder."
    )
    parser.add_argument("folder", help="Path to the folder to organize")
    parser.add_argument(
        "--mode",
        choices=["type", "date", "both"],
        default="type",
        help="Organize by file type, date, or both (default: type)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving any files",
    )
    args = parser.parse_args()

    folder = Path(args.folder).expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        print(f"Error: '{folder}' is not a valid directory.")
        return

    print(f"\nOrganizing: {folder}")
    print(f"Mode: {args.mode} {'(DRY RUN)' if args.dry_run else ''}")
    print("-" * 50)

    if args.mode == "type":
        count = organize_by_type(folder, args.dry_run)
    elif args.mode == "date":
        count = organize_by_date(folder, args.dry_run)
    else:
        count = organize_by_both(folder, args.dry_run)

    print("-" * 50)
    print(f"Done. {count} file(s) {'would be' if args.dry_run else 'were'} moved.\n")


if __name__ == "__main__":
    main()
