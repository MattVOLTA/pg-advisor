#!/usr/bin/env python3
"""Read Paul Graham essays for the PG advisor, without shipping them.

The advisor ships summaries and links, not essay text. This script reads an essay
from a local cache, or fetches it from paulgraham.com and caches it, so each user
makes their own copy.

Cache folder: $PG_ESSAYS_DIR if set, else ~/.pg-advisor/essays

Usage:
  essays.py get <slug>              print the essay text (fetches and caches if needed)
  essays.py find <slug> <phrase>    print lines containing a phrase (case-insensitive)
  essays.py search <phrase>         search every essay's full text (downloads them all first if needed: a few minutes, once)
  essays.py fetch-all               download every essay in the index (polite: a few minutes)
  essays.py where                   print the cache folder
"""
import html
import json
import os
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
INDEX = HERE / "references" / "knowledge" / "atlas-data.json"
CACHE = Path(os.environ.get("PG_ESSAYS_DIR") or Path.home() / ".pg-advisor" / "essays")


def load_essays():
    return {e["slug"]: e for e in json.load(open(INDEX))["essays"]}


class Body(HTMLParser):
    """Collect the text inside the first <font size=2 face=verdana>, the essay body."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth, self.done, self.out = 0, False, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.done:
            return
        if self.depth == 0:
            if tag == "font" and a.get("size") == "2" and (a.get("face") or "").lower() == "verdana":
                self.depth = 1
            return
        if tag == "font":
            self.depth += 1
        if tag == "br":
            self.out.append("\n")
        if tag == "p":
            self.out.append("\n\n")

    def handle_startendtag(self, tag, attrs):
        if self.depth and not self.done and tag == "br":
            self.out.append("\n")

    def handle_endtag(self, tag):
        if self.depth and not self.done and tag == "font":
            self.depth -= 1
            if self.depth == 0:
                self.done = True

    def handle_data(self, d):
        if self.depth and not self.done:
            self.out.append(d.replace("\n", " "))  # source line wraps aren't paragraph breaks


def fetch(e):
    req = urllib.request.Request(e["url"], headers={"User-Agent": "pg-advisor (personal reading cache)"})
    raw = urllib.request.urlopen(req, timeout=30).read()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    if e["url"].endswith(".txt") or ".txt?" in e["url"]:
        body = text
    else:
        p = Body()
        p.feed(text)
        body = "".join(p.out)
    body = re.sub(r"[ \t]+\n", "\n", html.unescape(body))
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return f"# {e['title']}\n\nSource: {e['url']}\n\n{body}\n"


def get(slug):
    es = load_essays()
    if slug not in es:
        sys.exit(f"Unknown essay '{slug}'. Slugs are in references/knowledge/index.md.")
    path = CACHE / f"{slug}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    try:
        text = fetch(es[slug])
    except Exception as err:  # noqa: BLE001
        sys.exit(f"Could not fetch {es[slug]['url']}: {err}. Cite from the summary and say the citation was not checked.")
    CACHE.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return text


def fetch_missing(verbose):
    es = load_essays()
    missing = [slug for slug in es if not (CACHE / f"{slug}.md").exists()]
    for n, slug in enumerate(missing, 1):
        get(slug)
        time.sleep(0.5)  # be polite to paulgraham.com
        if verbose:
            print(f"\r{n}/{len(missing)}", end="", flush=True)
    if verbose:
        print(f"\nCached {len(es)} essays in {CACHE}")
    return len(missing)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "where":
        print(CACHE)
    elif cmd == "get" and len(sys.argv) == 3:
        print(get(sys.argv[2]))
    elif cmd == "find" and len(sys.argv) >= 4:
        phrase = " ".join(sys.argv[3:]).lower()
        hits = [f"{i}: {line}" for i, line in enumerate(get(sys.argv[2]).splitlines(), 1) if phrase in line.lower()]
        print("\n".join(hits) if hits else f"'{phrase}' not found in {sys.argv[2]}")
    elif cmd == "fetch-all":
        fetch_missing(verbose=True)
    elif cmd == "search" and len(sys.argv) >= 3:
        # Summaries miss many specific claims, so a "did Graham say X?" check needs every essay's full text.
        missing = fetch_missing(verbose=False)
        if missing:
            print(f"(downloaded {missing} essays into {CACHE} first)", file=sys.stderr)
        phrase = " ".join(sys.argv[2:]).lower()
        es = load_essays()
        hits = []
        for slug, e in es.items():
            for i, line in enumerate(get(slug).splitlines(), 1):
                at = line.lower().find(phrase)
                if at >= 0:
                    # show the words around the match, not the paragraph's opening: matches often sit deep in long paragraphs
                    start, end = max(0, at - 160), min(len(line), at + len(phrase) + 160)
                    snippet = ("…" if start else "") + line[start:end].strip() + ("…" if end < len(line) else "")
                    hits.append(f"{e['year'] or '—'} {slug} ({e['title']}) line {i}: {snippet}")
        print("\n".join(hits) if hits else f"'{phrase}' appears in none of the {len(es)} essays")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
