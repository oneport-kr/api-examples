// OpenAI SDK 그대로, baseURL 만 원포트 AI 로 바꿉니다.
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://oneport.kr/v1",
  apiKey: process.env.ONEPORT_API_KEY,
});

const reply = await client.chat.completions.create({
  model: "gpt-5-mini",
  messages: [{ role: "user", content: "한 문장으로 인사해 주세요." }],
});
console.log(reply.choices[0].message.content);
