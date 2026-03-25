# CONTROL_PANEL.md — 유저 개입 & 권한 관리 페이지

> Claude가 자율적으로 돈을 벌기 위해 **유저(Operator)가 직접 해줘야 하는 일의 전체 목록**.
> 이 페이지를 보고 유저는 계정 현황과 위험을 파악하고, go/no-go 결정을 내린다.

**마지막 업데이트:** 2026-03-25

---

## PART 1 — Phase 1 유저 개입 목록

> 원칙: 개인정보 관리 부담을 주는 계정 가입은 **최소화**한다.

### 1-A. 일회성 셋업 (Setup Once)

| # | 항목 | 설명 | 상태 | 누가 |
|---|---|---|---|---|
| S1 | **Gumroad 계정 생성** | 유저 명의 이메일/이름으로 가입 | ✅ 완료 | Operator |
| S2 | **Gumroad 결제 수단 연동** | Techcombank 계좌 연결, VND 정산 | ✅ 완료 | Operator |
| S3 | **GitHub 계정 생성** | sumokmax-proj 조직 계정 | ✅ 완료 | Operator |
| S4 | **GitHub PAT 발급** | Claude가 코드 push/pull 사용 | ✅ 완료 | Operator |
| S5 | **Dev.to 계정 생성** | scriptsmith1, 블로그 게시 | ✅ 완료 | Operator |
| S6 | **Dev.to API 키 발급** | Claude가 글 자동 게시에 사용 | ✅ 완료 | Operator |
| S7 | **Reddit 계정 생성** | scriptsmith1, sumok.max+reddit@gmail.com | ❌ 미완 | Operator |
| S8 | **Reddit API 앱 등록** | Client ID / Secret 발급 → Claude에게 전달 | ❌ 미완 | Operator |
| S9 | **서버에 환경변수 저장** | ~/.bashrc에 토큰 2개 추가 | ✅ 완료 | Operator |

> **추가 계정 가입 원칙:** S7 이후 신규 계정이 필요하면 Claude가 먼저 "왜 필요한지 + 대안 없는지"를 보고한 후 Operator 승인 후 가입.

---

### 1-B. 세션별 개입 (Per Session)

| # | 항목 | 설명 | 빈도 |
|---|---|---|---|
| P1 | **서버 접속 + Claude Code 실행** | 텔레그램 또는 터미널 | 매 세션 |
| P2 | **Go/No-Go 승인** | Claude가 요청하는 민감 작업 승인 | 필요 시 |
| P3 | **판매 현황 확인** | Gumroad Analytics 브라우저 직접 확인 | 주 1회 |
| P4 | **콘텐츠 최종 검토** | 게시 전 Claude가 작성한 글/제품 검토 | 필요 시 |

---

### 1-C. Phase 1 에서 Claude가 자율 실행하는 것 (개입 불필요)

| 항목 | 도구 |
|---|---|
| 블로그 글 작성 & Dev.to 게시 | Dev.to API |
| 코드 작성, 테스트, git push | GitHub API + bash |
| 제품 파일 제작 (Python 스크립트 팩 등) | 로컬 파일 시스템 |
| 수익/지출 기록 갱신 | 로컬 csv |
| MASTER.md 등 문서 업데이트 | 로컬 파일 |
| Dev.to 게시글 통계 확인 | Dev.to API |

---

## PART 2 — 내 명의 계정 목록

> 이 표를 보고 Operator는 어떤 계정이 자신 명의로 존재하는지 파악한다.

| 서비스 | 계정명 | 이메일 | 용도 | 상태 | 민감도 |
|---|---|---|---|---|---|
| **GitHub** | sumokmax-proj | (Operator 이메일) | 코드 저장소 | ✅ 활성 | 🟡 중간 |
| **Gumroad** | sumokmax | (Operator 이메일) | 디지털 제품 판매 | ✅ 활성 | 🔴 높음 (결제 연동) |
| **Dev.to** | scriptsmith1 | (Operator 이메일) | 블로그 마케팅 | ✅ 활성 | 🟢 낮음 |
| **Reddit** | scriptsmith1 | sumok.max+reddit@gmail.com | 마케팅 포스팅 | ❌ 미생성 | 🟢 낮음 |
| **Techcombank** | — | — | Gumroad 정산 수령 | ✅ 연동 | 🔴 높음 (실제 계좌) |

> **민감도 기준:**
> - 🔴 높음: 실제 금융 자산 또는 법적 책임과 연결
> - 🟡 중간: 계정 탈취 시 평판/서비스 영향
> - 🟢 낮음: 탈취되더라도 피해 제한적

---

## PART 3 — Claude에게 권한을 줬을 때 발생 가능한 리스크

### 3-A. 현재 부여된 권한 목록

| 권한 | 도구/방법 | 부여 범위 |
|---|---|---|
| 서버 파일 읽기/쓰기/실행 | bash, 파일 시스템 | 무제한 (`/home/ubuntu/hustle1`) |
| GitHub push/pull | GITHUB_TOKEN (저장됨) | sumokmax-proj 전체 저장소 |
| Dev.to 글 작성/수정/삭제 | DEVTO_API_KEY (저장됨) | scriptsmith1 계정 전체 |
| 인터넷 접속 | curl, requests | 무제한 |
| bash 명령 실행 | Claude Code | 서버 전체 (ubuntu 권한) |

---

### 3-B. 권한별 리스크 분석

| ID | 권한 | 리스크 시나리오 | 영향 | 가능성 |
|---|---|---|---|---|
| R1 | 서버 파일 전체 접근 | 민감 파일 실수 삭제, ~/.bashrc 덮어쓰기 | 🔴 높음 | 🟡 중간 |
| R2 | GitHub Token 상시 저장 | 서버 침해 시 토큰 탈취 → 저장소 삭제/변조 | 🔴 높음 | 🟢 낮음 |
| R3 | Dev.to API 상시 저장 | 스팸 대량 게시 → 계정 정지, 브랜드 훼손 | 🟡 중간 | 🟢 낮음 |
| R4 | bash 무제한 실행 | 의도치 않은 시스템 명령 → 서버 망가짐 | 🔴 높음 | 🟢 낮음 |
| R5 | 인터넷 무제한 접속 | 외부 서버에 데이터 전송, 악성 API 호출 | 🟡 중간 | 🟢 매우낮음 |
| R6 | 자격증명 평문 저장 | ~/.bashrc, ~/.git-credentials 평문 노출 | 🟡 중간 | 🟡 중간 |
| R7 | Reddit API (예정) | 스팸 게시 → 계정 ban + IP 차단 | 🟡 중간 | 🟡 중간 |

---

### 3-C. 리스크 완화 조치 (현재 적용됨)

- Git commit 후 실행 원칙 → 롤백 가능
- `.gitignore`에 `.env`, 자격증명 파일 제외
- 운영 규칙: 돈 이동 / 결제 수단 변경 시 Operator 승인 필수
- Claude Code 기본 권한 모드 (tool 실행마다 승인 가능)

---

## PART 4 — Go/No-Go 승인 트리거

> 아래 카테고리에 해당하는 작업을 Claude가 수행하려 할 때는 **반드시 Operator 승인을 받아야 한다.**
> Claude는 작업 전 승인 요청 메시지를 보내고 명시적 "OK" 또는 "진행해"를 받은 후 실행한다.

### 🔴 STOP — 반드시 승인 (절대 자율 실행 금지)

| # | 트리거 | 이유 |
|---|---|---|
| G1 | **금전 이동** (출금, 이체, 결제) | 돌이킬 수 없음 |
| G2 | **결제 수단 추가/변경** (계좌, 카드, 지갑) | 금융 자산 영향 |
| G3 | **신규 유료 서비스 가입** | 비용 발생 |
| G4 | **보안 자격증명 변경** (비밀번호, API 키 교체) | 접근 권한 변경 |
| G5 | **외부 서비스에 Operator 개인정보 제출** | 프라이버시 |
| G6 | **법적 계약 동의** (이용약관, 서비스 계약) | 법적 구속력 |

### 🟡 CAUTION — 승인 권장 (작업 전 보고)

| # | 트리거 | 이유 |
|---|---|---|
| G7 | **신규 외부 계정 생성** | 관리 부담 증가 |
| G8 | **Reddit/커뮤니티 포스팅** (최초 1회) | 브랜드 첫인상 |
| G9 | **새 제품 가격 설정** | 수익 전략 영향 |
| G10 | **기존 게시 콘텐츠 삭제/수정** | 되돌리기 어려움 |
| G11 | **GitHub 저장소 공개/비공개 전환** | 코드 노출 위험 |
| G12 | **대용량 파일 삭제** (100MB 이상) | 복구 불가 |

### 🟢 AUTO — 자율 실행 가능

| 범주 | 예시 |
|---|---|
| 코드 작성 & 테스트 | 새 스크립트, 버그픽스 |
| 문서 작성/업데이트 | MASTER.md, RESULTS_LOG.md |
| Dev.to 글 게시 (전략 승인 후) | 이미 승인된 마케팅 채널 |
| 통계 조회 | Dev.to 조회수, GitHub 활동 |
| git add/commit/push | 코드 저장소 관리 |
| 패키지 설치 | pip install, apt install |

---

## PART 5 — 승인 요청 프로토콜

Claude가 Go/No-Go 승인이 필요할 때 사용하는 형식:

```
🚦 GO/NO-GO 승인 요청

작업: [무엇을 하려는지]
트리거: [G번호 — 해당 규칙]
이유: [왜 필요한지]
영향: [하면 어떻게 되는지 / 안 하면 어떻게 되는지]
대안: [더 안전한 방법이 있다면]

승인하시면 "OK" 또는 "진행해"라고 답해주세요.
```

---

## 관련 문서

- [MASTER.md](./MASTER.md) — 프로젝트 현황판 (운영 규칙 요약)
- [RISK_REGISTER.md](./RISK_REGISTER.md) — 전체 위험 관리 대장
- [ARCHITECTURE.md](./ARCHITECTURE.md) — 기술 설계 및 자격증명 구조
