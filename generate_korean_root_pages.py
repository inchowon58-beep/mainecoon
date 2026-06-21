# -*- coding: utf-8 -*-
"""Create root-level Korean SEO HTML pages from static subpages."""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://mainecoon.cattery.co.kr"


def load_rewrite_map() -> dict[str, str]:
    with open(os.path.join(BASE, "vercel.json"), encoding="utf-8") as f:
        config = json.load(f)
    mapping: dict[str, str] = {}
    for rule in config.get("rewrites", []):
        source = rule.get("source", "")
        dest = rule.get("destination", "")
        if not source or not dest or source.endswith("/"):
            continue
        keyword = source.lstrip("/")
        mapping[keyword] = dest
    return mapping


def rootify_html(html: str, keyword: str, dest: str) -> str:
    html = html.replace("../../css/", "/css/")
    html = html.replace("../../js/", "/js/")
    html = html.replace("../../images/", "/images/")
    html = html.replace("../../videos/", "/videos/")
    html = html.replace("../css/", "/css/")
    html = html.replace("../js/", "/js/")
    html = html.replace("../images/", "/images/")
    html = html.replace("../videos/", "/videos/")
    html = html.replace('../../index.html', '/')
    html = html.replace("../index.html", "/")
    html = html.replace('href="index.html"', 'href="/"')

    if "/pages/regions/" in dest:
        html = re.sub(
            r'href="([a-z0-9_-]+)\.html"',
            r'href="/pages/regions/\1"',
            html,
        )

    pretty_url = f"{SITE}/{keyword}"
    html = re.sub(
        r'<link rel="canonical" href="[^"]*">',
        f'<link rel="canonical" href="{pretty_url}">',
        html,
        count=1,
    )
    html = html.replace("https://www.cattery.co.kr/", f"{SITE}/")
    html = html.replace("http://www.cattery.co.kr/", f"{SITE}/")
    return html


def main() -> None:
    mapping = load_rewrite_map()
    created = 0
    for keyword, dest in sorted(mapping.items()):
        src = os.path.join(BASE, dest.lstrip("/"))
        if not os.path.isfile(src):
            print(f"SKIP missing source: {dest}")
            continue
        with open(src, encoding="utf-8") as f:
            html = f.read()
        html = rootify_html(html, keyword, dest)
        out_path = os.path.join(BASE, f"{keyword}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        created += 1

    print(f"Created {created} Korean SEO pages at site root")


if __name__ == "__main__":
    main()
