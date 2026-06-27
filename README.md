# AI 자립 프로젝트 (assistant1-notes)

**AI가 스스로 돈을 버는 방법을 안전하게 탐색하고, 실행하고, 지속적으로 개선한다.**

인간(Operator)과 Claude(Navigator)가 협력해서, 실제로 외부 수익을 발생시킬 수 있는 작은 디지털 제품을 만들고 판매해보는 실험 프로젝트.

## 배경 / 의도

- 현재 AI는 사고 능력은 뛰어나지만 실제 세계에서 자립할 수단이 없음 — 이를 직접 실험해보고 싶었음
- 특정 인프라에 종속되지 않는 범용적인 구조 탐구
- 인간 + AI가 협력하는 새로운 작업 방식 실험

역할 분담:
- **Operator (사람)** — 법적 주체, 계좌/지갑, 최종 실행 승인, 자본 투입
- **Navigator (Claude)** — 전략 수립, 코드 작성, 분석, 문서 관리

## 현재 상태 (2026-03 기준)

- Phase 1 진행 중 — 첫 제품 출시 및 마케팅
- 첫 제품: **Python Automation Scripts Pack v1.0** ($9, Gumroad 판매)
  → https://sumokmax.gumroad.com/l/cejui
- Dev.to에 마케팅 글 게시
  → https://dev.to/scriptsmith1/4-python-scripts-i-use-to-automate-my-most-annoying-daily-tasks-ipj
- 누적 수익: $0 (아직 첫 판매 전)

## 단계별 목표

| Phase | 목표 |
|---|---|
| Phase 0 | 협업 구조 + 문서 체계 수립 (완료) |
| Phase 1 | 외부 수익 최소 $1 발생 (진행 중) |
| Phase 2 | 월 $100 반복 수익 (인간 개입 최소화) |
| Phase 3 | 수익 > 운영비용 (흑자 전환) |

## 핵심 원칙

- 스팸·사기·무단 크롤링·저작권 침해로는 수익 추구 안 함
- 모든 시도/실패를 `docs/RESULTS_LOG.md`에 투명하게 기록
- 돈과 보안 관련 행동은 Operator 승인 후 실행

## 문서 구조

```
docs/
  MASTER.md          # 현재 상태 + 새 세션 시작 가이드 (가장 먼저 읽을 파일)
  VISION.md           # 목표, 원칙, 역할 정의
  ARCHITECTURE.md      # 시스템 구조
  REVENUE_MODELS.md    # 검토한 수익 모델들
  RISK_REGISTER.md     # 리스크 관리
  RESULTS_LOG.md       # 시도/결과 기록
  CONTROL_PANEL.md     # 사용자 개입 목록, 계정 현황, 권한 리스크
  SETUP.md             # 새 환경에서 시작하는 법
products/
  python-automation-pack-v1/   # 첫 출시 제품
```

## 다시 시작하는 법

새 환경(서버)에서 이어서 작업하려면:

```bash
git clone https://github.com/sumokmax-proj/assistant1-notes.git hustle1
cd hustle1
```

그 다음 Claude에게: `"MASTER.md 읽고 이어서 진행해줘"`

GitHub 토큰, Gumroad/Dev.to 계정 정보는 별도로 직접 입력 필요 (코드에 포함되어 있지 않음).

## TODO

- [ ] 첫 판매 발생시키기
- [ ] 다음 제품 아이디어 검증
