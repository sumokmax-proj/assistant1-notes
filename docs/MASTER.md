# MASTER.md — AI 자립 프로젝트 현황판

> 이 파일은 매 세션 시작 시 Claude가 반드시 먼저 읽고, 세션 종료 시 반드시 업데이트한다.

---

## 현재 상태

| 항목 | 내용 |
|---|---|
| **프로젝트 단계** | Phase 1 — 첫 제품 제작 준비 중 |
| **시작일** | 2026-02-24 |
| **누적 수익** | $0 |
| **누적 지출** | $0 |
| **활성 서비스** | 없음 |
| **다음 마일스톤** | Q4 결정 → 제품 제작 → Gumroad 업로드 |

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
- [ ] **Q4 결정: 제품 타겟 언어 (한국어 vs 영어)** ← 미결
- [ ] 제품 콘텐츠 제작 (Q4 결정 즉시 착수)
- [ ] Gumroad 제품 페이지 업로드
- [ ] MetaMask 지갑 생성
- [ ] 첫 수익 발생

---

## 이번 세션 TOP 3 TODO (다음 세션 시작 시)

- [ ] **Q4 결정: 한국어 vs 영어 타겟** → 결정 즉시 제품 제작 시작
- [ ] Python Automation Scripts Pack v1.0 제작 (Claude 실행)
- [ ] MetaMask 지갑 생성 완료 여부 확인

---

## 인간(Operator)에게 필요한 결정 (미결)

| 번호 | 질문 | 상태 |
|---|---|---|
| Q4 | 제품 타겟: 한국어 시장 vs 영어 글로벌 시장? | **미결 — 최우선** |
| Q6 | MetaMask 지갑 생성 완료됐는가? | 진행 중 |

---

## 운영 규칙 (고정)

- **승인 필수:** 돈 이동, 결제 수단 등록, 보안 자격증명 관련 모든 행동
- **자율 실행 허용:** 코드 작성, 문서 갱신, 툴/프레임워크 설치, 분석
- **초기 예산 한도:** $100 (가능하면 무료 방법 우선)
- **의사결정 원칙:** 실행 → 검증 → 개선 → 실행 반복
- **수익 모델 교체 기준:** 4주 내 수익 $0이면 모델 재검토
- **UI 메모:** Gumroad Pause payouts 토글 — 분홍색=일시정지(위험), 회색=정상지급(안전)

---

## 인프라 현황

| 항목 | 상태 | 비고 |
|---|---|---|
| GitHub 저장소 | ✅ 연동됨 | sumokmax-proj/assistant1-notes |
| GitHub 토큰 | ✅ 서버 저장 | ~/.git-credentials |
| Gumroad 계정 | ✅ 완료 | Weekly 정산 / Techcombank 연결 |
| MetaMask 지갑 | ⏳ 생성 대기 | 안내 완료 |
| 서버 인프라 | ✅ 현재 서버 사용 | 추가 비용 $0 |

---

## 마지막 세션 요약

| 항목 | 내용 |
|---|---|
| 날짜 | 2026-02-25 |
| 완료한 일 | Gumroad 전체 셋업 완료 (가입/인증/Techcombank 연동/Payout 설정) |
| 다음 세션 전 Operator 할 일 | Q4(한/영 타겟) 결정, MetaMask 생성 |
| 전반적 판단 | 정상 진행 — 제품 제작만 남은 상태 |

---

## 관련 문서 링크

- [VISION.md](./VISION.md) — 목표, 원칙, 성공 기준
- [ARCHITECTURE.md](./ARCHITECTURE.md) — 기술 설계
- [REVENUE_MODELS.md](./REVENUE_MODELS.md) — 수익 모델 전략 및 첫 제품 계획
- [RISK_REGISTER.md](./RISK_REGISTER.md) — 위험 관리
- [RESULTS_LOG.md](./RESULTS_LOG.md) — 실험 기록 및 학습
