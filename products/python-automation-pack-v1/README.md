# 🐍 Python Automation Scripts Pack v1.0

**Stop doing repetitive tasks manually. Let Python do it for you.**

A collection of 4 ready-to-use Python scripts that automate your most common daily tasks — no coding experience required to run them.

---

## What's Included

| Script | What It Does |
|---|---|
| `file_organizer.py` | Automatically sort files into folders by type or date |
| `email_drafter.py` | Generate professional emails from templates in seconds |
| `price_monitor.py` | Track product prices online and get alerted when they drop |
| `pdf_extractor.py` | Extract, search, and organize text from PDF files |

---

## Requirements

- Python 3.10 or higher ([download here](https://www.python.org/downloads/))
- Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Quick Start

### 1. File Organizer

Messy Downloads folder? Organize it in one command.

```bash
# Preview what will happen (no files moved)
python file_organizer.py ~/Downloads --dry-run

# Organize by file type (Images, Videos, Documents, etc.)
python file_organizer.py ~/Downloads --mode type

# Organize by date (2024/01/, 2024/02/, etc.)
python file_organizer.py ~/Downloads --mode date

# Organize by both type AND date
python file_organizer.py ~/Downloads --mode both
```

**Example output:**
```
Organizing: /Users/you/Downloads
Mode: type
--------------------------------------------------
  Moved: vacation.jpg → Images/
  Moved: report_q4.pdf → Documents/
  Moved: song.mp3 → Audio/
  Moved: script.py → Code/
--------------------------------------------------
Done. 4 file(s) were moved.
```

---

### 2. Email Drafter

Generate 7 types of professional emails instantly.

```bash
# See all available templates
python email_drafter.py --list

# Generate a follow-up email
python email_drafter.py --template follow_up --to "Sarah" --topic "our product demo"

# Generate a cold outreach email
python email_drafter.py --template cold_outreach --to "John" --company "TechCorp" --topic "a partnership idea"

# Request a meeting
python email_drafter.py --template meeting_request --to "Emma" --topic "Q1 strategy" --date "Tuesday at 2pm"

# Save to a .txt file
python email_drafter.py --template thank_you --to "Mike" --topic "the referral" --save
```

**Available templates:**
- `follow_up` — Follow up on any topic
- `cold_outreach` — Reach out to new contacts
- `thank_you` — Express gratitude professionally
- `apology` — Apologize for any situation
- `meeting_request` — Request a meeting with proposed time
- `project_update` — Send a structured project update
- `invoice_reminder` — Remind clients about unpaid invoices

---

### 3. Price Monitor

Track product prices on Amazon, eBay, or any website.

```bash
# Add a product to track
python price_monitor.py add \
  --url "https://www.amazon.com/dp/B08N5WRWNW" \
  --selector ".a-price-whole" \
  --target 89.99 \
  --name "Kindle Paperwhite"

# Check all prices right now
python price_monitor.py check

# Auto-monitor every 60 minutes
python price_monitor.py watch --interval 60

# See all tracked products
python price_monitor.py list

# View price history
python price_monitor.py history --name "Kindle Paperwhite"
```

> **Tip:** Use your browser's DevTools (F12 → Inspector) to find the correct CSS selector for any price element.

---

### 4. PDF Extractor

Extract, search, and convert PDFs to readable text.

```bash
# Extract all text from a PDF
python pdf_extractor.py extract report.pdf

# Extract as Markdown (great for notes apps)
python pdf_extractor.py extract report.pdf --format markdown

# Extract specific pages only
python pdf_extractor.py extract report.pdf --pages 1-10

# Batch extract all PDFs in a folder
python pdf_extractor.py batch ./my-pdfs/

# Search for a keyword across all PDFs
python pdf_extractor.py search ./my-pdfs/ --keyword "revenue"

# Get file info (pages, author, metadata)
python pdf_extractor.py info report.pdf
```

---

## Common Issues

**`pip` not found:**
Try `pip3` instead of `pip`.

**Permission denied (on Mac/Linux):**
Add `sudo` before the pip command: `sudo pip install -r requirements.txt`

**`python` not found:**
Try `python3` instead of `python`.

**Price monitor can't find price element:**
Some sites load prices with JavaScript. Try a different product page or contact us for help.

---

## System Requirements

| Requirement | Minimum |
|---|---|
| Python | 3.10+ |
| OS | Windows 10, macOS 11, Ubuntu 20.04 |
| RAM | 256 MB |
| Disk | 50 MB |

---

## Support

If you run into any issues or have questions, reach out via Gumroad messaging.
Feedback and feature requests are always welcome — v2.0 is coming soon!

---

## License

For personal and commercial use. Redistribution or resale of the scripts themselves is not permitted.

---

*Python Automation Scripts Pack v1.0 — Save hours every week.*
