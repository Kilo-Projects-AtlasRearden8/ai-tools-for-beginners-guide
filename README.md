# AI Tools for Beginners

A plain-English, step-by-step manual for anyone who wants to use AI tools — chatbots, image generators, writing assistants, and audio tools — without the jargon and without being talked down to.

Written for beginners. Published by **Asdale Dynamics, LLC**.

## What's inside

- `docs/` — the beginner manuals in Markdown (easy to read or print)
- `site/` — the same manuals as a simple static website; open any `.html` file in your browser
- `docs/cheat-sheets/` — one-page printable summaries for each topic
- `build_site.py` — the small script that turns the Markdown into the website
- `tests/verify_site.py` — checks that the website builds correctly

## Topics

1. [Introduction](docs/introduction.md) — what AI tools are and how to think about them
2. [Chatbots](docs/chatbots.md) — AI you can talk to by typing
3. [Image generators](docs/image-generators.md) — type words, get pictures
4. [Writing assistants](docs/writing-assistants.md) — AI help with emails, letters, and resumes
5. [Audio tools](docs/audio-tools.md) — turning text into speech and speech into text
6. [Step-by-step setup](docs/setup.md) — getting started from scratch
7. [Safety and privacy basics](docs/safety-privacy.md) — staying safe while you explore

## How to read it

Open any file in `docs/` in a text editor, or open `site/index.html` in your web browser. You do not need an internet connection to read the files once they are on your computer.

To rebuild the website from the Markdown source:

```
python3 build_site.py
```

This writes the HTML files into `site/`.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.

## About

This guide supports the educational work of **Asdale Dynamics, LLC** (Indiana), founded by Dylan Asdale — a registered nurse, AI author, and founder of Asdale Dynamics, LLC. It follows the same plain-English, beginner-first approach as *The Massive AI Manual* and dylanasdale.github.io: explain it like a friend would, step by step, never condescending.

None of this is medical advice. It is education only.
