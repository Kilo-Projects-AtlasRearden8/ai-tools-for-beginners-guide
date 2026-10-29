#!/usr/bin/env python3
"""Build the static HTML site from Markdown source files."""

import os
import sys

try:
    import markdown
except ImportError:
    print("Error: the 'markdown' Python package is required.")
    print("Install it with: pip install markdown")
    sys.exit(1)

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(ROOT, "docs")
SITE_DIR = os.path.join(ROOT, "site")
ASSETS_DIR = os.path.join(SITE_DIR, "assets")

PAGES = [
    ("introduction.md", "index.html", "Welcome to AI Tools for Beginners", False),
    ("chatbots.md", "chatbots.html", "Chatbots", False),
    ("image-generators.md", "image-generators.html", "Image Generators", False),
    ("writing-assistants.md", "writing-assistants.html", "Writing Assistants", False),
    ("audio-tools.md", "audio-tools.html", "Audio Tools", False),
    ("setup.md", "setup.html", "Step-by-Step Setup", False),
    ("safety-privacy.md", "safety-privacy.html", "Safety and Privacy Basics", False),
]

CHEAT_SHEETS = [
    ("cheat-sheets/introduction.md", "cheat-sheets/introduction.html", "AI Tools for Beginners — Cheat Sheet", True),
    ("cheat-sheets/chatbots.md", "cheat-sheets/chatbots.html", "Chatbots — Cheat Sheet", True),
    ("cheat-sheets/image-generators.md", "cheat-sheets/image-generators.html", "Image Generators — Cheat Sheet", True),
    ("cheat-sheets/writing-assistants.md", "cheat-sheets/writing-assistants.html", "Writing Assistants — Cheat Sheet", True),
    ("cheat-sheets/audio-tools.md", "cheat-sheets/audio-tools.html", "Audio Tools — Cheat Sheet", True),
    ("cheat-sheets/setup.md", "cheat-sheets/setup.html", "Setup — Cheat Sheet", True),
    ("cheat-sheets/safety-privacy.md", "cheat-sheets/safety-privacy.html", "Safety & Privacy — Cheat Sheet", True),
]

NAV_LINKS = [
    ("index.html", "Home"),
    ("chatbots.html", "Chatbots"),
    ("image-generators.html", "Image Generators"),
    ("writing-assistants.html", "Writing Assistants"),
    ("audio-tools.html", "Audio Tools"),
    ("setup.html", "Setup"),
    ("safety-privacy.html", "Safety & Privacy"),
]

CHEAT_SHEET_LINKS = [
    ("cheat-sheets/introduction.html", "Overview"),
    ("cheat-sheets/chatbots.html", "Chatbots"),
    ("cheat-sheets/image-generators.html", "Image Generators"),
    ("cheat-sheets/writing-assistants.html", "Writing Assistants"),
    ("cheat-sheets/audio-tools.html", "Audio Tools"),
    ("cheat-sheets/setup.html", "Setup"),
    ("cheat-sheets/safety-privacy.html", "Safety & Privacy"),
]

CSS_FILE = "style.css"


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def md_to_html(text):
    return markdown.markdown(text, extensions=["extra", "toc", "tables"])


def nav_links(current_page=None):
    lines = []
    for href, label in NAV_LINKS:
        active = ' class="active"' if href == current_page else ""
        lines.append(f'        <li><a href="{href}"{active}>{label}</a></li>')
    return "\n".join(lines)


def cheat_sheet_links(current_page=None):
    lines = []
    for href, label in CHEAT_SHEET_LINKS:
        active = ' class="active"' if href == current_page else ""
        lines.append(f'        <li><a href="{href}"{active}>{label}</a></li>')
    return "\n".join(lines)


def page_template(title, body, is_cheat_sheet=False, current_page=None):
    if is_cheat_sheet:
        css_href = f"../assets/{CSS_FILE}"
        links = cheat_sheet_links(current_page)
    else:
        css_href = f"../assets/{CSS_FILE}"
        links = nav_links(current_page)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — AI Tools for Beginners</title>
<link rel="stylesheet" href="{css_href}">
</head>
<body>
<header>
  <div class="container">
    <h1><a href="index.html">AI Tools for Beginners</a></h1>
    <p class="subtitle">Plain-English AI guides from Asdale Dynamics, LLC</p>
  </div>
</header>

<nav>
  <div class="container">
    <ul>
{links}
    </ul>
  </div>
</nav>

<main class="container">
{body}
</main>

<footer>
  <div class="container">
    <p>© 2026 Asdale Dynamics, LLC. Plain-English AI education for beginners.</p>
  </div>
</footer>
</body>
</html>"""


def build():
    os.makedirs(ASSETS_DIR, exist_ok=True)

    css_src = os.path.join(ROOT, CSS_FILE)
    if os.path.exists(css_src):
        write_file(os.path.join(ASSETS_DIR, CSS_FILE), read_file(css_src))

    for md_name, html_name, title, is_cheat_sheet in PAGES + CHEAT_SHEETS:
        base_dir = DOCS_DIR
        out_dir = SITE_DIR
        if is_cheat_sheet:
            out_dir = os.path.join(SITE_DIR, "cheat-sheets")
            html_name = os.path.basename(html_name)

        md_path = os.path.join(base_dir, md_name)
        html_path = os.path.join(out_dir, html_name)

        md_text = read_file(md_path)
        body_html = md_to_html(md_text)
        full_html = page_template(title, body_html, is_cheat_sheet=is_cheat_sheet, current_page=html_name)
        write_file(html_path, full_html)

    print(f"Built {len(PAGES)} pages and {len(CHEAT_SHEETS)} cheat sheets into {SITE_DIR}")


if __name__ == "__main__":
    build()