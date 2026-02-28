# MASTER.md — AI 자립 프로젝트 현황판

> 이 파일은 매 세션 시작 시 Claude가 반드시 먼저 읽고, 세션 종료 시 반드시 업데이트한다.

---

## 현재 상태

| 항목 | 내용 |
|---|---|
| **프로젝트 단계** | Phase 1 — 제품 라이브 + Dev.to 마케팅 시작 |
| **시작일** | 2026-02-24 |
| **누적 수익** | $0 |
| **누적 지출** | $0 |
| **활성 서비스** | Python Automation Scripts Pack v1.0 ($9) |
| **제품 URL** | https://sumokmax.gumroad.com/l/cejui |
| **다음 마일스톤** | 첫 번째 판매 ($1 이상 수익) |
| **Dev.to 게시글** | https://dev.to/scriptsmith1/4-python-scripts-i-use-to-automate-my-most-annoying-daily-tasks-ipj |

---

## 현재 진행 상태 (Phase 1 체크리스트)

- [x] 협업 구조 합의 완료
- [x] 문서 체계 수립 (6개 파일)
- [x] GitHub 연동 완료 (sumokmax-proj/assistant1-notes)
- [x] GitHub 토큰 서버 환경변수 저장 완료
- [x] 수익 모델 결정: Gumroad 디지털 제품 판매
- [x] 첫 제품 결정: Python Automation Scripts Pack v1.0 ($9)
- [x] Gumroad 계정 생성 완료 (2026-02-25)
- [x] Gumroad Identity Verification 완료
- [x] Gumroad 결제 수단 연동 완료 (Techcombank, CITAD: 01310001)
- [x] Gumroad Payout Schedule 설정 완료 (Weekly / $10 threshold)
- [x] Q4 결정: 영어 글로벌 타겟 확정
- [x] 제품 콘텐츠 제작 완료 (4개 스크립트 + README + requirements.txt)
- [x] **Gumroad 제품 페이지 업로드 및 발행 완료** (2026-02-25)
- [ ] 첫 판매 발생
- [x] Dev.to 블로그 게시 완료 (API 자동화)
- [ ] Reddit 포스팅 (r/Python, r/SideProject)
- [ ] Gumroad 자동 업로드 자동화 (쿠키 방식)
- [ ] MetaMask 지갑 생성 (Phase 2 전)

---

## 이번 세션 TOP 3 TODO (다음 세션 시작 시)

- [ ] **Reddit 포스팅** — r/Python, r/SideProject (다음 우선순위)
- [ ] **판매 현황 점검** — Dev.to 조회수 + Gumroad Analytics 확인
- [ ] **Gumroad 자동 업로드 자동화** — 쿠키 방식 구현

---

## 인간(Operator)에게 필요한 결정 (미결)

| 번호 | 질문 | 상태 |
|---|---|---|
| Q8 | Reddit 계정 생성 (scriptsmith1 사용 예정) | **미결** |
| Q6 | MetaMask 지갑 생성 | Phase 2 전까지 보류 |

---

## 운영 규칙 (고정)

- **승인 필수:** 돈 이동, 결제 수단 등록, 보안 자격증명 관련 모든 행동
- **자율 실행 허용:** 코드 작성, 문서 갱신, 툴/프레임워크 설치, 분석
- **초기 예산 한도:** $100 (가능하면 무료 방법 우선)
- **의사결정 원칙:** 실행 → 검증 → 개선 → 실행 반복
- **수익 모델 교체 기준:** 4주 내 수익 $0이면 모델 재검토
- **UI 메모:** Gumroad Pause payouts — 분홍색=일시정지, 회색=정상지급

---

## 인프라 현황

| 항목 | 상태 | 비고 |
|---|---|---|
| GitHub 저장소 | ✅ 연동됨 | sumokmax-proj/assistant1-notes |
| GitHub 토큰 | ✅ 서버 저장 | ~/.git-credentials |
| Gumroad 제품 | ✅ 라이브 | sumokmax.gumroad.com/l/cejui |
| Gumroad 정산 | ✅ 설정됨 | Weekly / Techcombank |
| Dev.to API | ✅ 저장됨 | ~/.bashrc DEVTO_API_KEY |
| Dev.to 게시글 | ✅ 라이브 | scriptsmith1 계정 |
| Gumroad 자동화 | ⏳ 미구현 | 쿠키 방식 — 다음 세션 |
| MetaMask 지갑 | ⏳ 보류 | Phase 2 전 생성 예정 |
| 서버 인프라 | ✅ 사용 중 | 추가 비용 $0 |

---

## 마지막 세션 요약

| 항목 | 내용 |
|---|---|
| 날짜 | 2026-02-28 |
| 완료한 일 | Dev.to 블로그 API 자동 게시, Dev.to API 키 저장, Dev.to 계정(scriptsmith1) 생성 |
| 다음 세션 할 일 | Reddit 포스팅, 판매 현황 점검, Gumroad 자동화 |
| 전반적 판단 | 정상 진행 — 마케팅 채널 1개 확보, 계속 확장 중 |

---

## 관련 문서 링크

- [VISION.md](./VISION.md) — 목표, 원칙, 성공 기준
- [ARCHITECTURE.md](./ARCHITECTURE.md) — 기술 설계
- [REVENUE_MODELS.md](./REVENUE_MODELS.md) — 수익 모델 전략 및 첫 제품 계획
- [RISK_REGISTER.md](./RISK_REGISTER.md) — 위험 관리
- [RESULTS_LOG.md](./RESULTS_LOG.md) — 실험 기록 및 학습
