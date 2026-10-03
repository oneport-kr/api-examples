"""OpenAI SDK 그대로, base_url 만 원포트 AI 로 바꿉니다."""
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://oneport.kr/v1",
    api_key=os.environ["ONEPORT_API_KEY"],
)

reply = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[{"role": "user", "content": "한 문장으로 인사해 주세요."}],
)
print(reply.choices[0].message.content)
