# MASTER.md — AI 자립 프로젝트 현황판

> **새 환경에서 시작할 때:** 이 파일을 먼저 읽고 SETUP.md로 환경 복원 후 작업 시작.
> 매 세션 시작 시 Claude가 반드시 읽고, 세션 종료 시 반드시 업데이트한다.

---

## 현재 상태 (2026-03-15 기준)

| 항목 | 내용 |
|---|---|
| **프로젝트 단계** | Phase 1 — 제품 라이브, 마케팅 진행 중 |
| **시작일** | 2026-02-24 |
| **누적 수익** | $0 |
| **누적 지출** | $0 |
| **활성 제품** | Python Automation Scripts Pack v1.0 ($9) |
| **Gumroad URL** | https://sumokmax.gumroad.com/l/cejui |
| **Dev.to 게시글** | https://dev.to/scriptsmith1/4-python-scripts-i-use-to-automate-my-most-annoying-daily-tasks-ipj |
| **다음 마일스톤** | 첫 번째 판매 발생 |

---

## Phase 1 전체 체크리스트

### 기반 구축 (완료)
- [x] 협업 구조 확정 (Operator + Claude Navigator)
- [x] 문서 체계 수립 (MASTER / VISION / ARCHITECTURE / REVENUE_MODELS / RISK_REGISTER / RESULTS_LOG / SETUP)
- [x] GitHub 저장소 연동 (sumokmax-proj/assistant1-notes)
- [x] GitHub 토큰 서버 저장 (~/.git-credentials)

### Gumroad 셋업 (완료)
- [x] Gumroad 계정 생성 (sumokmax, 2026-02-25)
- [x] Identity Verification 완료
- [x] 결제 수단 연동 (Techcombank, CITAD: 01310001, 하노이 본점)
- [x] Payout Schedule: Weekly / $10 minimum (VND 정산)
- [x] 영어 글로벌 타겟 확정

### 제품 (완료)
- [x] Python Automation Scripts Pack v1.0 제작
  - file_organizer.py / email_drafter.py / price_monitor.py / pdf_extractor.py
  - README.md / requirements.txt
- [x] 커버 이미지 제작 (1280x720, 다크 테마)
- [x] Gumroad 업로드 및 발행 (2026-02-25)

### 마케팅 (진행 중)
- [x] Dev.to 계정 생성 (scriptsmith1)
- [x] Dev.to API 키 발급 및 서버 저장
- [x] Dev.to 블로그 게시 자동화 완료 (2026-02-28)
- [ ] **Reddit 포스팅** ← 다음 작업
- [ ] Hacker News Show HN
- [ ] 첫 판매 발생

### 자동화 (미완)
- [ ] Gumroad 업로드 자동화 (쿠키 방식)
- [ ] Reddit API 자동 포스팅
- [ ] MetaMask 지갑 생성 (Phase 2 전)

---

## 다음 세션 TOP 3 TODO

1. **Reddit 계정 생성** (`scriptsmith1`, `sumok.max+reddit@gmail.com`)
   → Reddit API 앱 등록 → Claude가 자동 포스팅 처리
   → 목표 서브레딧: r/SideProject (즉시), r/Python (karma 쌓은 후)

2. **판매 현황 점검**
   → Dev.to 조회수 확인 (API)
   → Gumroad Analytics 직접 확인 (app.gumroad.com/analytics)

3. **Gumroad 자동화 구현**
   → 브라우저 로그인 후 쿠키 추출 → Claude가 직접 업로드

---

## 미결 결정 사항

| 번호 | 질문 | 상태 |
|---|---|---|
| Q8 | Reddit 계정 생성 여부 | **미결 — 최우선** |
| Q9 | Hacker News 포스팅 시점 | Dev.to 조회수 보고 결정 |
| Q6 | MetaMask 지갑 생성 | Phase 2 전까지 보류 |

---

## 운영 규칙 (고정)

- **승인 필수:** 돈 이동, 결제 수단 등록, 보안 자격증명 관련 모든 행동
- **자율 실행:** 코드 작성, 문서 갱신, 툴 설치, API 호출, 분석
- **예산 한도:** $100 (무료 방법 우선)
- **사이클:** 실행 → 검증 → 개선 → 실행
- **피벗 기준:** 4주 내 수익 $0이면 모델 재검토
- **Gumroad UI:** Pause payouts 분홍=일시정지, 회색=정상

---

## 인프라 현황

| 항목 | 상태 | 위치/비고 |
|---|---|---|
| GitHub 저장소 | ✅ | sumokmax-proj/assistant1-notes |
| GitHub 토큰 | ✅ 서버 저장 | ~/.git-credentials |
| Gumroad 계정 | ✅ | sumokmax.gumroad.com |
| Gumroad 정산 | ✅ | Weekly / Techcombank VND |
| Dev.to 계정 | ✅ | scriptsmith1 |
| Dev.to API 키 | ✅ 서버 저장 | ~/.bashrc → DEVTO_API_KEY |
| 서버 | ✅ | /home/ubuntu/hustle1 (AWS) |
| Reddit 계정 | ❌ 미생성 | 다음 세션 |
| Gumroad 자동화 | ❌ 미구현 | 쿠키 방식 예정 |
| MetaMask | ❌ 보류 | Phase 2 |

---

## 마지막 세션 요약

| 항목 | 내용 |
|---|---|
| 날짜 | 2026-02-28 (세션 4) |
| 완료 | Dev.to 블로그 API 자동 게시, Dev.to API 키 저장 |
| 다음 | Reddit 포스팅, 판매 점검, Gumroad 자동화 |
| 판단 | 정상 진행 — 트래픽 확보가 현재 핵심 과제 |

---

## 관련 문서

- [SETUP.md](./SETUP.md) — **새 환경 셋업 가이드** (클론 후 반드시 읽기)
- [VISION.md](./VISION.md) — 목표, 원칙, 성공 기준
- [ARCHITECTURE.md](./ARCHITECTURE.md) — 기술 설계 및 자격증명 관리
- [REVENUE_MODELS.md](./REVENUE_MODELS.md) — 수익 모델 및 제품 현황
- [RISK_REGISTER.md](./RISK_REGISTER.md) — 위험 관리
- [RESULTS_LOG.md](./RESULTS_LOG.md) — 전체 세션 기록
