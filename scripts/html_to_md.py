#!/usr/bin/env python3
"""Convert site HTML pages to clean markdown files.

Uses only Python stdlib (html.parser). Extracts content from <section class="about">
and strips navigation, sidebar, and footer boilerplate.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class HTMLToMarkdown(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []       # list of finished markdown blocks
        self.buf = ""          # current text buffer
        self.in_section = False
        self.in_nav = False
        self.in_footer = False
        self.in_a = False
        self.a_href = ""
        self.list_depth = 0
        self.in_li = False

    def _active(self):
        return self.in_section and not self.in_nav and not self.in_footer

    def _flush(self):
        """Push current buffer as a block and reset."""
        text = self.buf.strip()
        if text:
            self.blocks.append(text)
        self.buf = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "section" and "about" in attrs_dict.get("class", ""):
            self.in_section = True
            return
        if tag == "nav":
            self.in_nav = True
            return
        if tag == "footer":
            self.in_footer = True
            return

        if not self._active():
            return

        if tag == "h1":
            self._flush()
            self.buf = "# "
        elif tag == "h2":
            self._flush()
            self.buf = "## "
        elif tag == "a":
            self.in_a = True
            self.a_href = attrs_dict.get("href", "")
            self.buf += "["
        elif tag == "strong":
            self.buf += "**"
        elif tag in ("em", "i"):
            self.buf += "*"
        elif tag == "ul":
            # Flush any preceding text before starting a list
            if not self.in_li:
                self._flush()
            self.list_depth += 1
        elif tag == "li":
            # Flush previous li if any
            if self.in_li:
                self._flush()
            self.in_li = True
            indent = "  " * max(0, self.list_depth - 1)
            self.buf = f"{indent}- "
        elif tag == "br":
            # Treat <br> as a paragraph break if outside a list item review
            if self.in_li:
                # Inside a book review li, br is just a space
                self.buf += " "
            else:
                self._flush()
        elif tag == "p":
            self._flush()

    def handle_endtag(self, tag):
        if tag == "section":
            self._flush()
            self.in_section = False
            return
        if tag == "nav":
            self.in_nav = False
            return
        if tag == "footer":
            self.in_footer = False
            return

        if not self._active():
            return

        if tag in ("h1", "h2"):
            self._flush()
        elif tag == "a":
            self.buf += f"]({self.a_href})"
            self.in_a = False
            self.a_href = ""
        elif tag == "strong":
            self.buf += "**"
        elif tag in ("em", "i"):
            self.buf += "*"
        elif tag == "ul":
            self.list_depth -= 1
            if self.list_depth == 0:
                self._flush()
                self.in_li = False
        elif tag == "li":
            self._flush()
            if self.list_depth <= 1:
                self.in_li = False
        elif tag == "p":
            self._flush()

    def handle_data(self, data):
        if not self._active():
            return
        text = re.sub(r"\s+", " ", data)
        self.buf += text

    def get_markdown(self):
        self._flush()
        result = "\n\n".join(b for b in self.blocks if b.strip())
        result = re.sub(r"\n{3,}", "\n\n", result)
        return result.strip() + "\n"


def convert_file(html_path: Path) -> str:
    parser = HTMLToMarkdown()
    parser.feed(html_path.read_text())
    return parser.get_markdown()


def main():
    if len(sys.argv) > 1:
        files = [Path(f) for f in sys.argv[1:]]
    else:
        site_root = Path(__file__).resolve().parent.parent
        files = sorted(site_root.glob("*.html"))

    for html_path in files:
        md_path = html_path.with_name(html_path.name + ".md")
        md_content = convert_file(html_path)
        md_path.write_text(md_content)
        print(f"  {html_path.name} -> {md_path.name}")


if __name__ == "__main__":
    main()
