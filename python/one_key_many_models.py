"""키 하나로 여러 회사 모델 — model 이름만 바꿉니다. 쓴 만큼 같은 크레딧에서 빠집니다."""
import os

from openai import OpenAI

client = OpenAI(base_url="https://oneport.kr/v1", api_key=os.environ["ONEPORT_API_KEY"])

for model in ["gpt-5-mini", "claude-haiku-4-5", "gemini-3.5-flash"]:
    reply = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "한국의 수도를 한 단어로만 답해 주세요."}],
    )
    print(f"{model}: {reply.choices[0].message.content.strip()}")
