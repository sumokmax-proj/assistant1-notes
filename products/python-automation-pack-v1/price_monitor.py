"""
price_monitor.py — Monitor product prices on any website and get alerted when they drop.

Usage:
    # Add a product to monitor
    python price_monitor.py add --url "https://example.com/product" --selector ".price" --target 29.99 --name "My Product"

    # Check prices once
    python price_monitor.py check

    # Monitor continuously (every 60 minutes)
    python price_monitor.py watch --interval 60

    # View all tracked products
    python price_monitor.py list

    # View price history
    python price_monitor.py history --name "My Product"

    # Remove a product
    python price_monitor.py remove --name "My Product"

Requirements:
    pip install requests beautifulsoup4
"""

import json
import re
import time
import argparse
import csv
from pathlib import Path
from datetime import datetime

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Please run: pip install requests beautifulsoup4")
    exit(1)

DATA_FILE = Path("price_monitor_data.json")
HISTORY_FILE = Path("price_history.csv")


def load_data() -> dict:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"products": []}


def save_data(data: dict):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def extract_price(text: str) -> float | None:
    cleaned = re.sub(r"[^\d.,]", "", text.strip())
    cleaned = cleaned.replace(",", "")
    try:
        return float(cleaned)
    except ValueError:
        return None


def fetch_price(url: str, selector: str) -> tuple[float | None, str]:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        element = soup.select_one(selector)
        if not element:
            return None, f"Selector '{selector}' not found on page."
        raw_text = element.get_text()
        price = extract_price(raw_text)
        if price is None:
            return None, f"Could not parse price from: '{raw_text}'"
        return price, "OK"
    except requests.RequestException as e:
        return None, f"Request error: {e}"


def log_history(name: str, url: str, price: float, target: float, alerted: bool):
    file_exists = HISTORY_FILE.exists()
    with open(HISTORY_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "name", "url", "price", "target", "alert_triggered"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            name, url, price, target, alerted
        ])


def cmd_add(args):
    data = load_data()
    names = [p["name"] for p in data["products"]]
    if args.name in names:
        print(f"A product named '{args.name}' already exists. Use a different name.")
        return
    product = {
        "name": args.name,
        "url": args.url,
        "selector": args.selector,
        "target_price": args.target,
        "added": datetime.now().isoformat(),
        "last_price": None,
        "last_checked": None,
    }
    data["products"].append(product)
    save_data(data)
    print(f"Added: '{args.name}' — target price ${args.target}")


def cmd_list(args):
    data = load_data()
    if not data["products"]:
        print("No products being tracked. Use 'add' to start.")
        return
    print(f"\n{'Name':<20} {'Target':>8} {'Last Price':>12} {'Last Checked':<20}")
    print("-" * 65)
    for p in data["products"]:
        last_price = f"${p['last_price']:.2f}" if p["last_price"] else "Not checked"
        last_checked = p["last_checked"][:16] if p["last_checked"] else "Never"
        print(f"{p['name']:<20} ${p['target_price']:>7.2f} {last_price:>12} {last_checked:<20}")
    print()


def cmd_check(args):
    data = load_data()
    if not data["products"]:
        print("No products to check.")
        return

    alerts = []
    for product in data["products"]:
        print(f"Checking: {product['name']}...", end=" ", flush=True)
        price, status = fetch_price(product["url"], product["selector"])

        if price is None:
            print(f"FAILED — {status}")
            continue

        product["last_price"] = price
        product["last_checked"] = datetime.now().isoformat()

        alerted = price <= product["target_price"]
        log_history(product["name"], product["url"], price, product["target_price"], alerted)

        if alerted:
            print(f"ALERT! ${price:.2f} (target: ${product['target_price']:.2f}) ← PRICE DROP!")
            alerts.append(product)
        else:
            diff = price - product["target_price"]
            print(f"${price:.2f} (target: ${product['target_price']:.2f}, ${diff:.2f} above target)")

    save_data(data)

    if alerts:
        print(f"\n{'='*50}")
        print(f"PRICE ALERTS: {len(alerts)} product(s) hit target price!")
        for p in alerts:
            print(f"  → {p['name']}: ${p['last_price']:.2f} (target: ${p['target_price']:.2f})")
            print(f"    {p['url']}")
        print(f"{'='*50}\n")
    else:
        print("\nNo price alerts triggered.")


def cmd_watch(args):
    print(f"Starting price monitor (interval: {args.interval} minutes). Press Ctrl+C to stop.\n")
    while True:
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running price check...")
        cmd_check(args)
        print(f"Next check in {args.interval} minutes...")
        time.sleep(args.interval * 60)


def cmd_history(args):
    if not HISTORY_FILE.exists():
        print("No history recorded yet.")
        return
    print(f"\nPrice history for: {args.name or 'all products'}")
    print("-" * 75)
    with open(HISTORY_FILE, "r") as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader if not args.name or r["name"] == args.name]
    if not rows:
        print("No history found.")
        return
    print(f"{'Timestamp':<22} {'Name':<20} {'Price':>8} {'Target':>8} {'Alert'}")
    print("-" * 75)
    for row in rows[-20:]:
        alert = "YES!" if row["alert_triggered"] == "True" else ""
        print(f"{row['timestamp']:<22} {row['name']:<20} ${float(row['price']):>7.2f} ${float(row['target']):>7.2f} {alert}")
    print()


def cmd_remove(args):
    data = load_data()
    before = len(data["products"])
    data["products"] = [p for p in data["products"] if p["name"] != args.name]
    if len(data["products"]) < before:
        save_data(data)
        print(f"Removed: '{args.name}'")
    else:
        print(f"Product '{args.name}' not found.")


def main():
    parser = argparse.ArgumentParser(description="Monitor product prices on any website.")
    subparsers = parser.add_subparsers(dest="command")

    # add
    p_add = subparsers.add_parser("add", help="Add a product to monitor")
    p_add.add_argument("--url", required=True)
    p_add.add_argument("--selector", required=True, help="CSS selector for the price element")
    p_add.add_argument("--target", type=float, required=True, help="Alert when price drops to this value")
    p_add.add_argument("--name", required=True, help="Friendly name for this product")

    # list
    subparsers.add_parser("list", help="List all tracked products")

    # check
    subparsers.add_parser("check", help="Check all prices once")

    # watch
    p_watch = subparsers.add_parser("watch", help="Continuously monitor prices")
    p_watch.add_argument("--interval", type=int, default=60, help="Check interval in minutes (default: 60)")

    # history
    p_hist = subparsers.add_parser("history", help="Show price history")
    p_hist.add_argument("--name", default=None, help="Filter by product name")

    # remove
    p_remove = subparsers.add_parser("remove", help="Remove a tracked product")
    p_remove.add_argument("--name", required=True)

    args = parser.parse_args()

    commands = {
        "add": cmd_add,
        "list": cmd_list,
        "check": cmd_check,
        "watch": cmd_watch,
        "history": cmd_history,
        "remove": cmd_remove,
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
