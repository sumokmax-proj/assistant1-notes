# SETUP.md — 새 환경 셋업 가이드

> 새 폴더에 git clone 후 이 파일을 먼저 실행하세요.
> 서버 환경변수와 자격증명을 복원하는 방법을 설명합니다.

---

## 1. 저장소 클론

```bash
git clone https://github.com/sumokmax-proj/assistant1-notes.git
cd assistant1-notes
```

---

## 2. 환경변수 복원

아래 값들을 `~/.bashrc`에 추가해야 합니다.
(같은 서버라면 이미 저장되어 있으므로 `source ~/.bashrc`만 실행)

```bash
# ~/.bashrc에 추가
# 실제 값은 별도로 Operator에게 확인 (보안상 여기 기록 안 함)
export GITHUB_TOKEN="<GitHub PAT 토큰>"
export DEVTO_API_KEY="<Dev.to API 키>"
```

```bash
source ~/.bashrc
```

---

## 3. Git 자격증명 복원

```bash
git config --global credential.helper store

# ~/.git-credentials 파일 생성
echo "https://sumokmax-proj:${GITHUB_TOKEN}@github.com" > ~/.git-credentials

# 원격 저장소 URL 업데이트
git remote set-url origin "https://sumokmax-proj:${GITHUB_TOKEN}@github.com/sumokmax-proj/assistant1-notes.git"
```

---

## 4. Python 환경 복원 (제품 개발 시)

```bash
# venv 생성 (처음 한 번만)
sudo apt install python3.12-venv -y
cd products/python-automation-pack-v1
python3 -m venv venv
venv/bin/pip install requests beautifulsoup4 pymupdf

# 이후 사용 시
source products/python-automation-pack-v1/venv/bin/activate
```

---

## 5. 계정 정보 요약

| 서비스 | 계정 | 비고 |
|---|---|---|
| GitHub | sumokmax-proj | 토큰으로 인증 |
| Gumroad | sumokmax (sumok.max@gmail.com) | Google 로그인 |
| Dev.to | scriptsmith1 (sumok.max+devto@gmail.com) | API 키로 자동화 |
| Reddit | 미생성 | 다음 세션에 생성 예정 |

---

## 6. 주요 URL

| 항목 | URL |
|---|---|
| GitHub 저장소 | https://github.com/sumokmax-proj/assistant1-notes |
| Gumroad 제품 | https://sumokmax.gumroad.com/l/cejui |
| Gumroad 대시보드 | https://app.gumroad.com/dashboard |
| Dev.to 게시글 | https://dev.to/scriptsmith1/4-python-scripts-i-use-to-automate-my-most-annoying-daily-tasks-ipj |

---

## 7. 작업 재개 방법

새 환경에서 Claude에게:
```
"MASTER.md 읽고 이어서 진행해줘"
```

Claude가 현황 파악 후 다음 작업을 안내합니다.

---

## 8. Dev.to API 사용법

```bash
# 게시글 통계 확인
curl -s "https://dev.to/api/articles/me?per_page=5" \
  -H "api-key: ${DEVTO_API_KEY}"

# 새 글 게시 (curl 사용, Python urllib은 서버 IP 차단됨)
curl -s -X POST "https://dev.to/api/articles" \
  -H "api-key: ${DEVTO_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Mozilla/5.0 (compatible; scriptsmith-bot/1.0)" \
  -d '{"article":{"title":"제목","published":true,"body_markdown":"본문","tags":["python"]}}'
```

---

## 9. 서버 디렉토리 구조

```
/home/ubuntu/hustle1/          ← 메인 작업 디렉토리
├── docs/                      ← 프로젝트 문서 (이 파일들)
│   ├── MASTER.md              ← 현황판 (매 세션 읽기)
│   ├── SETUP.md               ← 이 파일
│   ├── VISION.md              ← 목표/원칙
│   ├── ARCHITECTURE.md        ← 기술 설계
│   ├── REVENUE_MODELS.md      ← 수익 전략
│   ├── RISK_REGISTER.md       ← 위험 관리
│   └── RESULTS_LOG.md         ← 세션 기록
├── products/
│   ├── python-automation-pack-v1/   ← 첫 번째 제품
│   │   ├── file_organizer.py
│   │   ├── email_drafter.py
│   │   ├── price_monitor.py
│   │   ├── pdf_extractor.py
│   │   ├── README.md
│   │   └── requirements.txt
│   ├── make_cover.py          ← 커버 이미지 생성 스크립트
│   └── cover.png              ← 생성된 커버 이미지
└── .gitignore
```
