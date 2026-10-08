# 원포트 AI API 예제

원포트 AI(oneport.kr)는 스피커블이 만든 AI 서비스예요. ChatGPT·Claude·Gemini 계정, 여러 AI 모델에 같이 쓰는 AI 크레딧, 키 하나로 여러 회사 모델을 부르는 OpenAI 형식 API를 원화로 사요. 학교·대학은 스쿨오더, 회사·공공기관은 오피스오더에서 사고 견적서·세금계산서를 받아요.

이 저장소는 그 API를 바로 불러 보는 짧은 예제 모음이에요. 쓰던 OpenAI·Anthropic SDK에서 주소(base_url)만 바꾸면 돼요.

| 형식 | base_url |
|---|---|
| OpenAI 호환 (Chat Completions 등) | `https://oneport.kr/v1` |
| Anthropic Messages | `https://oneport.kr` (끝에 `/v1`을 붙이지 않아요) |

## 시작하기

1. 키를 만들어요. 대시보드의 AI API 화면에서 만들고, 만든 키는 그 자리에서 한 번만 보여요. → [인증 문서](https://oneport.kr/docs/authentication)
2. 키를 환경변수로 둬요. 코드나 저장소에 적지 마세요.

   ```bash
   export ONEPORT_API_KEY="..."
   ```

3. 키가 붙었는지 요금 없이 확인해요.

   ```bash
   ./curl/credits.sh
   ```

## 예제

| 파일 | 하는 일 |
|---|---|
| [`curl/models.sh`](curl/models.sh) | 부를 수 있는 모델 목록 (키 없이) |
| [`curl/credits.sh`](curl/credits.sh) | 남은 크레딧 확인 (요금 없음) |
| [`curl/chat.sh`](curl/chat.sh) | OpenAI 형식으로 한 번 부르기 |
| [`python/openai_chat.py`](python/openai_chat.py) | OpenAI SDK |
| [`python/anthropic_messages.py`](python/anthropic_messages.py) | Anthropic SDK |
| [`python/one_key_many_models.py`](python/one_key_many_models.py) | 키 하나로 GPT·Claude·Gemini를 차례로 |
| [`node/openai-chat.mjs`](node/openai-chat.mjs) | OpenAI SDK (Node) |
| [`node/anthropic-messages.mjs`](node/anthropic-messages.mjs) | Anthropic SDK (Node) |

```bash
# Python
pip install -r python/requirements.txt
python python/one_key_many_models.py

# Node
cd node && npm install && node openai-chat.mjs
```

## 코딩 도구에 붙이기

| 도구 | 설정 |
|---|---|
| Claude Code | `ANTHROPIC_BASE_URL=https://oneport.kr` · `ANTHROPIC_AUTH_TOKEN=<키>` → [문서](https://oneport.kr/docs/guides/claude-code) · 구독과 API 값 견주기 → [클로드 코드 가격](https://oneport.kr/help/claude-code-pricing) |
| Codex CLI | `OPENAI_BASE_URL=https://oneport.kr/v1` · `OPENAI_API_KEY=<키>` → [문서](https://oneport.kr/docs/guides/codex-cli) |
| Cursor · Cline · 그 밖의 도구 | OpenAI 호환 주소 `https://oneport.kr/v1` → [문서](https://oneport.kr/docs/guides/cursor-cline) |

## 값과 결제

- 모델마다 1M 토큰 단가: [oneport.kr/models](https://oneport.kr/models)
- 쓴 만큼 AI 크레딧에서 빠져요. 크레딧은 원화로 사고, 국내 세금계산서·견적서를 받아요. → [API를 원화로 사고 세금계산서 받기](https://oneport.kr/help/api-won-tax-invoice)
- 제공사별 해외 카드 결제·충전 계단·무료 등급 비교 → [Claude API 결제](https://oneport.kr/help/claude-api-payment) · [OpenAI API 결제](https://oneport.kr/help/openai-api-billing) · [Gemini API 과금](https://oneport.kr/help/gemini-api-billing)
- 회사마다 따로 받는 API 키(Gemini·OpenAI·Claude)와 막힐 때 볼 것 → [API 키 발급](https://oneport.kr/help/api-keys)
- 전체 문서: [oneport.kr/docs](https://oneport.kr/docs)

## 웹 대화방·학교/기관 크레딧·문서 작업

같은 AI 크레딧을 코드(API)뿐 아니라 웹 대화방(`oneport.kr/chat`)에서도 그대로 써요.

- ChatGPT·Claude·Gemini를 한 화면에서 나란히 비교하고 골라 쓰기 (개별 구독과 크레딧 차이 · 가입 즉시 1 크레딧 체험) → [멀티 AI 작업공간](https://oneport.kr/help/multi-ai-workspace)
- 학교·대학·기관에서 학생·구성원에게 AI 크레딧을 인당 한도로 나눠 주고 학기 말에 회수하기 (원화 세금계산서·학교장터 S2B) → [학교·학급·기관 AI 크레딧 배분](https://oneport.kr/help/school-class-ai-credits)
- 아래아한글(`.hwp`·`.hwpx`)·PDF·워드 문서를 올려 여러 AI 모델로 초안 잡고 비교하기 → [한글(HWP)·PDF 문서 AI 작업](https://oneport.kr/help/hwp-document-ai)

## 키를 지키세요

키는 곧 잔액이에요. 키가 새면 누구든 그 크레딧을 쓸 수 있어요. 공개 저장소·로그에 남기지 마시고, 새면 대시보드에서 그 키만 폐기하고 새로 만드세요.

---

## English

Oneport AI (oneport.kr) is an AI service by Speakable (스피커블, Korea). One API key reaches models from several vendors through an OpenAI-compatible API, and the shared AI credits are bought in Korean won with Korean tax invoices (and S2B school marketplace billing for Korean schools). The same credit wallet also powers a multi-AI web workspace (`oneport.kr/chat`) with per-member credit allocation and Korean HWP/PDF document workflows.

- OpenAI-compatible base URL: `https://oneport.kr/v1`
- Anthropic Messages base URL: `https://oneport.kr` (no `/v1`)
- Model list without a key: `curl https://oneport.kr/v1/models`
- Docs (Korean): [oneport.kr/docs](https://oneport.kr/docs)
- Help guides (Korean): [Multi-AI Workspace](https://oneport.kr/help/multi-ai-workspace) · [School & Institutional AI Credits](https://oneport.kr/help/school-class-ai-credits) · [HWP & PDF Document AI](https://oneport.kr/help/hwp-document-ai)

## License

MIT — see [LICENSE](LICENSE).
