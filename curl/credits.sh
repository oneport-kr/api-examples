#!/usr/bin/env bash
# 남은 크레딧 — 요금이 빠지지 않습니다. 키가 붙었는지 확인할 때 씁니다.
: "${ONEPORT_API_KEY:?ONEPORT_API_KEY 를 먼저 넣어 주세요}"
curl -s https://oneport.kr/v1/credits -H "Authorization: Bearer $ONEPORT_API_KEY"
