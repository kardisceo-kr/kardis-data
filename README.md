# kardis-data

kardis 홈페이지의 「중점협력국 동향」과 「인사이트」가 읽는 공개 데이터 저장소입니다.

- `news.json` — 중점협력국 정치·경제·사회 동향. 매일 1회 갱신.
- `countries.json` — 중점협력국 25개국 목록과 표시 지표(세계은행 지표 코드).
- `RULES.md` — 동향 작성 규칙.
- `posts/` — 인사이트 게시글(마크다운, 파일 하나가 글 하나). 작성 규칙은 `POSTS.md`.
- `posts.json` — 게시글 목록. `posts/`가 바뀌면 GitHub Actions가 자동으로 다시 만듭니다(`scripts/build_posts.py`).

사이트: https://kardis.kr (준비 중) · 문의: kardisceo@gmail.com

동향 항목은 제목·요약·출처 링크만 담으며 기사 본문은 싣지 않습니다. 요약은 kardis가 작성합니다.

갱신 작업: 매일 07:00(KST) 자동 갱신, 월요일에 전체 국가 갱신.
