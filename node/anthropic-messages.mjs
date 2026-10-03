// Anthropic SDK 그대로. baseURL 은 /v1 없이 https://oneport.kr 까지만 적습니다.
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: "https://oneport.kr",
  apiKey: process.env.ONEPORT_API_KEY,
});

const message = await client.messages.create({
  model: "claude-haiku-4-5",
  max_tokens: 200,
  messages: [{ role: "user", content: "한 문장으로 인사해 주세요." }],
});
console.log(message.content[0].text);
