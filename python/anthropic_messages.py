"""Anthropic SDK 그대로. base_url 은 /v1 없이 https://oneport.kr 까지만 적습니다(SDK 가 /v1/messages 를 붙입니다)."""
import os

import anthropic

client = anthropic.Anthropic(
    base_url="https://oneport.kr",
    api_key=os.environ["ONEPORT_API_KEY"],
)

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=200,
    messages=[{"role": "user", "content": "한 문장으로 인사해 주세요."}],
)
print(message.content[0].text)
