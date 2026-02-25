"""
email_drafter.py — Generate professional emails from templates in seconds.

Usage:
    python email_drafter.py --list
    python email_drafter.py --template follow_up --to "John" --topic "our meeting"
    python email_drafter.py --template cold_outreach --to "Sarah" --company "Acme" --topic "partnership"
    python email_drafter.py --template thank_you --to "Mike" --topic "the interview"
    python email_drafter.py --template apology --to "Client" --topic "the delayed delivery"
    python email_drafter.py --template meeting_request --to "Emma" --topic "product demo" --date "Friday at 3pm"
"""

import argparse
from datetime import datetime

TEMPLATES = {
    "follow_up": {
        "subject": "Following up on {topic}",
        "body": """Hi {to},

I hope this message finds you well.

I wanted to follow up on {topic}. I understand you may be busy, but I'd love to
hear your thoughts whenever you have a moment.

Please let me know if you need any additional information from my end.

Looking forward to hearing from you.

Best regards,
{from_name}""",
    },
    "cold_outreach": {
        "subject": "Quick idea for {company} regarding {topic}",
        "body": """Hi {to},

I hope you don't mind me reaching out. My name is {from_name}, and I came across
{company} recently.

I noticed an opportunity related to {topic} that I believe could be valuable for
your team. I'd love to share a quick idea — it won't take more than 10 minutes.

Would you be open to a brief call this week?

Best,
{from_name}""",
    },
    "thank_you": {
        "subject": "Thank you for {topic}",
        "body": """Hi {to},

I just wanted to take a moment to thank you for {topic}.

It genuinely made a difference, and I truly appreciate your time and effort.

If there's ever anything I can do to return the favor, please don't hesitate to ask.

Warm regards,
{from_name}""",
    },
    "apology": {
        "subject": "Apology regarding {topic}",
        "body": """Hi {to},

I want to sincerely apologize for {topic}.

I understand this may have caused inconvenience, and that's entirely on me.
I take full responsibility and I'm already working on making sure this doesn't
happen again.

Please let me know what I can do to make this right.

Sincerely,
{from_name}""",
    },
    "meeting_request": {
        "subject": "Meeting request: {topic}",
        "body": """Hi {to},

I hope you're doing well.

I'd love to schedule some time to discuss {topic}. Would {date} work for you?
If not, I'm happy to find a time that fits your schedule.

A quick 20–30 minute call would be enough to cover the key points.

Looking forward to connecting.

Best,
{from_name}""",
    },
    "project_update": {
        "subject": "Project update: {topic}",
        "body": """Hi {to},

Here's a quick update on {topic}:

- Status: [In Progress / Completed / Blocked]
- Completed this week: [list key items]
- Next steps: [what comes next]
- Blockers (if any): [mention any issues]

Please let me know if you have any questions or feedback.

Best,
{from_name}""",
    },
    "invoice_reminder": {
        "subject": "Friendly reminder: Invoice for {topic}",
        "body": """Hi {to},

I hope everything is going well.

This is a friendly reminder that the invoice for {topic} is now due.
If you've already sent payment, please disregard this message.

If you have any questions about the invoice, feel free to reach out.

Thank you for your prompt attention.

Best regards,
{from_name}""",
    },
}


def list_templates():
    print("\nAvailable templates:")
    print("-" * 40)
    for name, content in TEMPLATES.items():
        print(f"  {name:<20} → {content['subject']}")
    print()


def generate_email(template_name: str, variables: dict) -> dict:
    if template_name not in TEMPLATES:
        raise ValueError(f"Template '{template_name}' not found. Use --list to see available templates.")

    template = TEMPLATES[template_name]
    subject = template["subject"]
    body = template["body"]

    for key, value in variables.items():
        subject = subject.replace(f"{{{key}}}", value)
        body = body.replace(f"{{{key}}}", value)

    return {"subject": subject, "body": body}


def save_to_file(email: dict, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Subject: {email['subject']}\n")
        f.write("-" * 50 + "\n")
        f.write(email["body"])
    print(f"\nSaved to: {filename}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate professional email drafts from templates."
    )
    parser.add_argument("--list", action="store_true", help="List all available templates")
    parser.add_argument("--template", help="Template name to use")
    parser.add_argument("--to", default="[Recipient]", help="Recipient name")
    parser.add_argument("--from-name", default="[Your Name]", dest="from_name", help="Your name")
    parser.add_argument("--topic", default="[topic]", help="Main topic or subject")
    parser.add_argument("--company", default="[Company]", help="Company name (for cold_outreach)")
    parser.add_argument("--date", default="[proposed date]", help="Meeting date (for meeting_request)")
    parser.add_argument("--save", action="store_true", help="Save output to a .txt file")
    args = parser.parse_args()

    if args.list:
        list_templates()
        return

    if not args.template:
        parser.print_help()
        return

    variables = {
        "to": args.to,
        "from_name": args.from_name,
        "topic": args.topic,
        "company": args.company,
        "date": args.date,
    }

    try:
        email = generate_email(args.template, variables)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"\n{'='*50}")
    print(f"Subject: {email['subject']}")
    print(f"{'='*50}")
    print(email["body"])
    print(f"{'='*50}\n")

    if args.save:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"email_{args.template}_{timestamp}.txt"
        save_to_file(email, filename)


if __name__ == "__main__":
    main()
