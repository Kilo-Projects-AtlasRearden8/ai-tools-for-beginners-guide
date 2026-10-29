#!/usr/bin/env python3
"""Verify the static site builds correctly from Markdown sources."""

import os
import sys
import unittest

ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(ROOT)
SITE_DIR = os.path.join(PROJECT_ROOT, "site")
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")
ASSETS_DIR = os.path.join(SITE_DIR, "assets")


class SiteBuildTests(unittest.TestCase):
    """Tests that the static site builds correctly."""

    def test_required_files_exist(self):
        """All expected source files must exist."""
        expected_docs = [
            "introduction.md",
            "chatbots.md",
            "image-generators.md",
            "writing-assistants.md",
            "audio-tools.md",
            "setup.md",
            "safety-privacy.md",
        ]
        for name in expected_docs:
            path = os.path.join(DOCS_DIR, name)
            self.assertTrue(os.path.isfile(path), f"Missing doc: {name}")

        expected_cheats = [
            os.path.join("cheat-sheets", "introduction.md"),
            os.path.join("cheat-sheets", "chatbots.md"),
            os.path.join("cheat-sheets", "image-generators.md"),
            os.path.join("cheat-sheets", "writing-assistants.md"),
            os.path.join("cheat-sheets", "audio-tools.md"),
            os.path.join("cheat-sheets", "setup.md"),
            os.path.join("cheat-sheets", "safety-privacy.md"),
        ]
        for name in expected_cheats:
            path = os.path.join(DOCS_DIR, name)
            self.assertTrue(os.path.isfile(path), f"Missing cheat sheet: {name}")

    def test_html_pages_exist(self):
        """All expected HTML output pages must exist after build."""
        expected_pages = [
            "index.html",
            "chatbots.html",
            "image-generators.html",
            "writing-assistants.html",
            "audio-tools.html",
            "setup.html",
            "safety-privacy.html",
        ]
        for name in expected_pages:
            path = os.path.join(SITE_DIR, name)
            self.assertTrue(os.path.isfile(path), f"Missing HTML page: {name}")

        expected_cheat_html = [
            os.path.join("cheat-sheets", "introduction.html"),
            os.path.join("cheat-sheets", "chatbots.html"),
            os.path.join("cheat-sheets", "image-generators.html"),
            os.path.join("cheat-sheets", "writing-assistants.html"),
            os.path.join("cheat-sheets", "audio-tools.html"),
            os.path.join("cheat-sheets", "setup.html"),
            os.path.join("cheat-sheets", "safety-privacy.html"),
        ]
        for name in expected_cheat_html:
            path = os.path.join(SITE_DIR, name)
            self.assertTrue(os.path.isfile(path), f"Missing cheat HTML: {name}")

    def test_css_exists(self):
        """The stylesheet must be copied into site/assets/."""
        path = os.path.join(ASSETS_DIR, "style.css")
        self.assertTrue(os.path.isfile(path), "Missing style.css in site/assets/")

    def test_html_has_valid_structure(self):
        """Each HTML page must have basic valid structure."""
        for name in ["index.html", "chatbots.html", "safety-privacy.html"]:
            path = os.path.join(SITE_DIR, name)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("<!DOCTYPE html>", content)
            self.assertIn("<html", content)
            self.assertIn("</html>", content)
            self.assertIn('<head>', content)
            self.assertIn('<body>', content)
            self.assertIn("style.css", content)
            self.assertIn("Asdale Dynamics, LLC", content)

    def test_credit_present(self):
        """Asdale Dynamics, LLC must be credited on every page."""
        for root, _, files in os.walk(SITE_DIR):
            for name in files:
                if not name.endswith(".html"):
                    continue
                path = os.path.join(root, name)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.assertIn("Asdale Dynamics, LLC", content,
                              f"{name} missing Asdale Dynamics, LLC credit")

    def test_copyright_present(self):
        """Copyright 2026 must appear on every page."""
        for root, _, files in os.walk(SITE_DIR):
            for name in files:
                if not name.endswith(".html"):
                    continue
                path = os.path.join(root, name)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.assertIn("© 2026", content,
                              f"{name} missing © 2026 copyright")

    def test_no_secrets_or_keys(self):
        """No API keys, secrets, or personal data in site files."""
        suspicious = ["sk-", "api_key", "secret_key", "access_token", "private_key"]
        for root, _, files in os.walk(SITE_DIR):
            for name in files:
                if not name.endswith((".html", ".css")):
                    continue
                path = os.path.join(root, name)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read().lower()
                for term in suspicious:
                    self.assertNotIn(term, content,
                                     f"{name} contains suspicious term: {term}")


if __name__ == "__main__":
    unittest.main()