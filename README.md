# AI Tools for Beginners

A plain-English, step-by-step manual for anyone who wants to use AI tools — chatbots, image generators, writing assistants, and audio tools — without the jargon and without being talked down to.

Written for beginners. Published by **Asdale Dynamics, LLC**.

## Who this is for

This guide is for anyone who wants to start using AI tools but doesn't know where to begin. You don't need to be a programmer. If you can type into a search box, you can use these tools.

It was created by **Asdale Dynamics, LLC** (Indiana), founded by Dylan Asdale — a registered nurse turned AI author. It follows the same plain-English, beginner-first approach as *The Massive AI Manual* and dylanasdale.github.io: explain it like a friend would, step by step, never condescending.

## What's inside

| Folder | Contents |
|--------|----------|
| `docs/` | Beginner manuals in Markdown (easy to read or print) |
| `docs/cheat-sheets/` | One-page printable summaries for each topic |
| `site/` | The same manuals as a simple static website; open any `.html` file in your browser |
| `build_site.py` | Small script that turns the Markdown into the website |
| `tests/verify_site.py` | Checks that the website builds correctly |
| `LICENSE` | MIT License |

## Topics covered

1. [Introduction](docs/introduction.md) — what AI tools are and how to think about them
2. [Chatbots](docs/chatbots.md) — AI assistants you talk to by typing
3. [Image generators](docs/image-generators.md) — type words, get pictures
4. [Writing assistants](docs/writing-assistants.md) — AI help with emails, letters, and resumes
5. [Audio tools](docs/audio-tools.md) — turning text into speech and speech into text
6. [Step-by-step setup](docs/setup.md) — getting started from scratch
7. [Safety and privacy basics](docs/safety-privacy.md) — staying safe while you explore

Each topic page includes step-by-step instructions, realistic examples, free and low-cost tools to try, and a printable cheat sheet.

## How to read it

Open any file in `docs/` in a text editor, or open `site/index.html` in your web browser. You do not need an internet connection to read the files once they are on your computer.

To print a cheat sheet, open the matching file in `site/cheat-sheets/` and print from your browser.

## How to rebuild the website

The Markdown files in `docs/` are the source. To regenerate the static HTML site:

```
python3 build_site.py
```

This requires the Python `markdown` package:

```
pip install markdown
```

The script writes all HTML files into `site/` and copies the stylesheet into `site/assets/`.

## Running the tests

```
python3 -m pytest tests/verify_site.py -v
```

All tests should pass. The tests check that source files exist, HTML pages are generated, the stylesheet is in place, every page credits Asdale Dynamics, LLC, every page carries the © 2026 copyright, and no API keys or secrets appear in the built site.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.

## About Asdale Dynamics, LLC

Asdale Dynamics, LLC (Indiana, formed October 2026) is focused on beginner-friendly AI education, books and guides, and practical tools the LLC can publish or sell. Founder Dylan Asdale is a registered nurse and AI author. His book *The Massive AI Manual* and hub site dylanasdale.github.io explain AI plainly, step by step, never condescending.

This guide supports that mission. None of it is medical advice — it is education only.
