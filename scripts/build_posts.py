#!/usr/bin/env python3
"""posts/*.md 의 머리말(front matter)을 읽어 posts.json(게시글 목록)을 만든다.
GitHub Actions가 posts/ 변경 시 자동 실행한다. 직접 실행: python3 scripts/build_posts.py
'_'로 시작하는 파일(_template.md 등)은 목록에서 제외한다."""
import json, re, sys, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATEGORIES = ["개발협력 동향", "데이터 인사이트", "성과측정 방법론", "통계 기법", "AI 활용"]
STATUS = {"published", "draft"}
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]{2,80}$")

def parse(text):
    m = re.match(r"^﻿?---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        raise ValueError("머리말(--- ... ---)이 없습니다")
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        k, sep, v = line.partition(":")
        if not sep:
            raise ValueError(f"'키: 값' 형식이 아닌 줄: {line}")
        k, v = k.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [t.strip().strip("\"'") for t in v[1:-1].split(",") if t.strip()]
        else:
            v = v.strip("\"'")
        meta[k] = v
    return meta, text[m.end():]

def main():
    items, errors = [], []
    for p in sorted((ROOT / "posts").glob("*.md")):
        if p.name.startswith("_"):
            continue
        slug = p.stem
        try:
            meta, body = parse(p.read_text(encoding="utf-8"))
            if not SLUG.match(slug):
                raise ValueError("파일 이름은 영문 소문자·숫자·하이픈만 씁니다(예: 2026-10-pdm-indicators.md)")
            for k in ("title", "date", "category", "summary"):
                if not meta.get(k):
                    raise ValueError(f"'{k}' 항목이 비어 있습니다")
            datetime.date.fromisoformat(meta["date"])
            if meta["category"] not in CATEGORIES:
                raise ValueError(f"분류는 다음 중 하나: {', '.join(CATEGORIES)}")
            status = meta.get("status", "draft")
            if status not in STATUS:
                raise ValueError("status는 published 또는 draft")
            tags = meta.get("tags", [])
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",") if t.strip()]
            words = len(re.sub(r"\s+", "", body))
            items.append({
                "slug": slug, "title": meta["title"], "date": meta["date"],
                "category": meta["category"], "summary": meta["summary"],
                "tags": tags, "author": meta.get("author", "kardis"),
                "status": status, "ai": str(meta.get("ai", "no")).lower() in ("yes", "true", "y"),
                "minutes": max(1, round(words / 500)),
            })
        except Exception as e:
            errors.append(f"{p.name}: {e}")
    items.sort(key=lambda x: (x["date"], x["slug"]), reverse=True)
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")
    try:  # 목록이 그대로면 갱신 시각도 그대로 둔다(불필요한 커밋 방지)
        old = json.loads((ROOT / "posts.json").read_text(encoding="utf-8"))
        if old.get("items") == items and old.get("categories") == CATEGORIES:
            now = old.get("updated", now)
    except Exception:
        pass
    out = {
        "updated": now,
        "categories": CATEGORIES,
        "items": items,
    }
    (ROOT / "posts.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"게시글 {len(items)}건 (공개 {sum(i['status']=='published' for i in items)}건)")
    for e in errors:
        print("오류:", e, file=sys.stderr)
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
