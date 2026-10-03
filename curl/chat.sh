#!/usr/bin/env bash
# OpenAI 형식 한 번 — model 만 바꾸면 다른 회사 모델입니다.
: "${ONEPORT_API_KEY:?ONEPORT_API_KEY 를 먼저 넣어 주세요}"
curl -s https://oneport.kr/v1/chat/completions \
  -H "Authorization: Bearer $ONEPORT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5-mini",
    "messages": [{"role": "user", "content": "한 문장으로 인사해 주세요."}]
  }'
