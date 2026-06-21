# -*- coding: utf-8 -*-
"""Generate vercel.json rewrites: Korean SEO URLs -> static HTML pages."""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
REGIONS_DIR = os.path.join(BASE, "pages", "regions")

GUIDE_REWRITES = {
    "메인쿤고양이종류": "/pages/maine-coon-types.html",
    "메인쿤크기": "/pages/maine-coon-size.html",
    "메인쿤몸무게": "/pages/maine-coon-size.html",
    "메인쿤고양이성묘": "/pages/adult-cat.html",
    "메인쿤입양": "/pages/maine-coon-adoption.html",
    "메인쿤분양가": "/pages/maine-coon-adoption.html",
    "메인쿤분양가격": "/pages/maine-coon-adoption.html",
    "메인쿤특징": "/pages/maine-coon-personality.html",
    "메인쿤성격": "/pages/maine-coon-personality.html",
    "메인쿤수명": "/pages/maine-coon-adoption.html",
    "메인쿤유전병": "/pages/maine-coon-adoption.html",
    "털빠짐": "/pages/shedding-care.html",
    "메인쿤털빠짐": "/pages/shedding-care.html",
}

# Next.js-only SEO routes -> nearest static region/guide page
EXTRA_REWRITES = {
    "단원구메인쿤분양": "/pages/regions/ansan.html",
    "신림메인쿤분양": "/pages/regions/seoul.html",
    "노원구메인쿤분양": "/pages/regions/seoul.html",
    "강서구메인쿤분양": "/pages/regions/magok.html",
    "포항메인쿤분양": "/pages/regions/daegu.html",
    "성동구메인쿤분양": "/pages/regions/seoul.html",
    "세종메인쿤분양": "/pages/regions/jochiwon.html",
    "파주메인쿤분양": "/pages/regions/gimpo.html",
    "양평메인쿤분양": "/pages/regions/seoul.html",
    "익산메인쿤분양": "/pages/regions/jeonju.html",
    "강화도메인쿤분양": "/pages/regions/incheon.html",
    "도봉구메인쿤분양": "/pages/regions/uijeongbu.html",
    "안성메인쿤분양": "/pages/regions/suwon.html",
    "관악구메인쿤분양": "/pages/regions/seoul.html",
    "양주메인쿤분양": "/pages/regions/uijeongbu.html",
    "해운대메인쿤분양": "/pages/regions/busan.html",
    "종로메인쿤분양": "/pages/regions/seoul.html",
    "부평메인쿤분양": "/pages/regions/incheon.html",
    "영종도메인쿤분양": "/pages/regions/incheon.html",
    "은평구메인쿤분양": "/pages/regions/seoul.html",
    "금천구메인쿤분양": "/pages/regions/gwangmyeong.html",
    "순천메인쿤분양": "/pages/regions/mokpo.html",
    "간석메인쿤분양": "/pages/regions/incheon.html",
    "서초구메인쿤분양": "/pages/regions/seocho.html",
    "중동메인쿤분양": "/pages/regions/bucheon.html",
    "미추홀구메인쿤분양": "/pages/regions/incheon.html",
    "달서구메인쿤분양": "/pages/regions/daegu.html",
    "화곡동메인쿤분양": "/pages/regions/magok.html",
    "광진구메인쿤분양": "/pages/regions/gangdong.html",
    "목동메인쿤분양": "/pages/regions/yeongdeungpo.html",
    "동작구메인쿤분양": "/pages/regions/seocho.html",
    "경산메인쿤분양": "/pages/regions/daegu.html",
}


def load_region_keywords() -> dict[str, str]:
    """Return keyword -> /pages/regions/{slug}.html from existing HTML files."""
    mapping: dict[str, str] = {}
    title_re = re.compile(r"<title>([^|]+)\s*\|")
    for name in os.listdir(REGIONS_DIR):
        if not name.endswith(".html"):
            continue
        slug = name[:-5]
        path = os.path.join(REGIONS_DIR, name)
        with open(path, encoding="utf-8") as f:
            head = f.read(800)
        m = title_re.search(head)
        if not m:
            continue
        keyword = m.group(1).strip()
        mapping[keyword] = f"/pages/regions/{slug}.html"
    return mapping


def destination_for(keyword: str, region_map: dict[str, str]) -> str | None:
    if keyword in region_map:
        return region_map[keyword]
    if keyword in GUIDE_REWRITES:
        return GUIDE_REWRITES[keyword]
    if keyword in EXTRA_REWRITES:
        return EXTRA_REWRITES[keyword]
    return None


def collect_nextjs_keywords() -> list[str]:
    archive = os.path.join(BASE, "_archive", "nextjs_app")
    if not os.path.isdir(archive):
        return []
    return sorted(
        name
        for name in os.listdir(archive)
        if os.path.isdir(os.path.join(archive, name))
    )


def build_rewrites() -> list[dict]:
    region_map = load_region_keywords()
    mapping: dict[str, str] = dict(region_map)
    mapping.update(GUIDE_REWRITES)
    mapping.update(EXTRA_REWRITES)

    for keyword in collect_nextjs_keywords():
        if keyword not in mapping:
            dest = destination_for(keyword, region_map)
            if dest:
                mapping[keyword] = dest

    rewrites = []
    for keyword in sorted(mapping.keys()):
        dest = mapping[keyword]
        rewrites.append({"source": f"/{keyword}", "destination": dest})
        rewrites.append({"source": f"/{keyword}/", "destination": dest})

    return rewrites


def main() -> None:
    config = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "framework": None,
        "buildCommand": None,
        "devCommand": None,
        "installCommand": None,
        "outputDirectory": ".",
        "cleanUrls": True,
        "trailingSlash": False,
        "rewrites": build_rewrites(),
    }

    out_path = os.path.join(BASE, "vercel.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
        f.write("\n")

    count = len(config["rewrites"]) // 2
    print(f"Wrote {out_path} with {count} Korean URL rewrites")


if __name__ == "__main__":
    main()
