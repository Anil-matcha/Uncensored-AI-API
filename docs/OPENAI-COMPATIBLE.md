# OpenAI-Compatible Chat Completions

Muapi offers a shared chat-completions endpoint for OpenAI-compatible clients. This is separate from the model-specific `/api/v1/{model-id}` endpoints documented in [API.md](API.md): chat completions use a `messages` array and return a completion response; model-specific routes use `prompt`, return a `request_id`, and are polled for the result.

## Endpoint and authentication

```text
Base URL: https://api.muapi.ai/v1
Chat:     POST https://api.muapi.ai/v1/chat/completions
Models:   GET  https://api.muapi.ai/v1/models?type=text
Auth:     Authorization: Bearer YOUR_MUAPI_API_KEY
```

List current model IDs and capabilities before choosing a model:

```bash
curl "https://api.muapi.ai/v1/models?type=text" \
  -H "Authorization: Bearer $MUAPI_API_KEY"
```

Use exact IDs from this response. The model catalog may include text models beyond the 21 routes in this repository. Tool calling is model-specific; check `capabilities.tools` before sending a `tools` array.

## cURL

```bash
curl "https://api.muapi.ai/v1/chat/completions" \
  -H "Authorization: Bearer $MUAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-3-8-27b-abliterated",
    "messages": [
      {"role": "system", "content": "You are a concise technical tutor."},
      {"role": "user", "content": "Explain idempotency in one paragraph."}
    ],
    "max_tokens": 512
  }'
```

## OpenAI Python SDK

Install the SDK with `pip install openai`, then set `MUAPI_API_KEY` in your environment:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MUAPI_API_KEY"],
    base_url="https://api.muapi.ai/v1",
)

response = client.chat.completions.create(
    model="qwen-3-8-27b-abliterated",
    messages=[
        {"role": "system", "content": "You are a concise technical tutor."},
        {"role": "user", "content": "Explain idempotency in one paragraph."},
    ],
    max_tokens=512,
)
print(response.choices[0].message.content)
```

## Streaming

Set `stream=True` in the OpenAI SDK request or pass `"stream": true` in the HTTP body. Consume the returned SSE events and stop at `[DONE]`. This is the chat-completions streaming protocol; it differs from the direct model route's SSE endpoint.

## Tools and limits

- Function calling is supported only on models that advertise `capabilities.tools: true` in the live model list.
- If a model does not support tools, the API rejects tool fields. Do not infer tool support from the model family or the direct route.
- Use the live API reference for supported chat parameters, token caps, image input, and usage fields.
- Keep your key server-side and avoid logging private prompts or credentials.
