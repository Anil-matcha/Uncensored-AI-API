# Muapi Abliterated LLM API

This guide describes the public request pattern used by Muapi's abliterated LLM endpoints. Check the [live model page](https://muapi.ai/abliterated-llm-api) for the current IDs, schemas, and prices.

## Base URL and authentication

```text
https://api.muapi.ai/api/v1
```

Send your Muapi key in the `x-api-key` header. Keep the key on a server or in a secret manager; do not place it in browser code, a public repository, or a mobile app bundle.

```http
x-api-key: YOUR_MUAPI_API_KEY
Content-Type: application/json
```

## Submit a generation

Each model has a dedicated route. Replace `{model-id}` with an exact ID from [MODEL-CATALOG.md](MODEL-CATALOG.md).

```http
POST /api/v1/{model-id}
```

Example body:

```json
{
  "prompt": "Explain why idempotency matters in an API retry strategy.",
  "system_prompt": "You are a concise software engineering tutor.",
  "max_tokens": 512
}
```

`prompt` is required. The other common fields are optional and subject to that model's schema:

| Field | Type | Use |
|---|---|---|
| `prompt` | string | User message or instruction. Required. |
| `system_prompt` | string | Optional system-level instruction. |
| `max_tokens` | integer | Optional output limit. The accepted range can differ by model. |
| `image_url` | string | Optional public image URL for models marked as image-capable. |
| `thinking` | boolean | Optional reasoning control on the supported Qwen 3.8 and DeepSeek V4.1 Flash routes. |

Do not send optional fields to every model automatically. Use the live endpoint schema as the final authority.

A successful submission returns a JSON object containing `request_id`. Store that ID and poll the result endpoint.

## Poll a result

```http
GET /api/v1/predictions/{request_id}/result
```

Use the same `x-api-key` header. The response has a `status`; keep polling for `pending` or `processing`, stop on `completed` or `failed`, and apply a finite timeout in your client. On completion, the text is returned in `outputs`. On failure, inspect the error field and decide whether a retry is safe.

Avoid rapid, unbounded polling. The examples use a one-second delay and a two-minute client timeout; tune these values to your application's needs and current service guidance.

## Stream text

For a direct SSE response, append `/stream` to the model route:

```http
POST /api/v1/{model-id}/stream
Content-Type: application/json
x-api-key: YOUR_MUAPI_API_KEY
```

Send the same model-specific JSON body as a normal request. The server responds with `text/event-stream` and emits content delta events followed by `data: [DONE]`. A stream does not return a `request_id` for polling. Handle disconnects, error events, and partial output in your client.

A quick terminal check:

```bash
curl -N -X POST "https://api.muapi.ai/api/v1/qwen-3-8-27b-abliterated/stream" \
  -H "x-api-key: $MUAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Write a two-sentence description of a lunar greenhouse."}'
```

## Image input

Only models marked `Text + image` in the catalog accept `image_url`. The URL must be reachable by the service. Image support and limits can be model-specific; check the model schema before sending private or sensitive material.

## Errors and retries

- Treat non-2xx HTTP responses as request errors; record the status and a sanitized message for debugging.
- A `failed` prediction is terminal. Do not keep polling it as if it were still running.
- Retry only when the failure is transient and your application can tolerate duplicate work. Use an application-level request identifier or deduplication strategy where duplicate completions would be costly.
- Never log API keys, full prompts containing sensitive information, or private image URLs.
- If a model returns no useful output, first check the exact model ID, input fields, account balance, and live availability.

## OpenAI-compatible chat endpoint

The model-specific routes in this guide use Muapi's `prompt`-based request body. For clients that expect the OpenAI Chat Completions format, Muapi also provides a separate `POST https://api.muapi.ai/v1/chat/completions` route. That endpoint accepts `model` and `messages`, uses `Authorization: Bearer YOUR_API_KEY`, and supports streaming. Function calling is available only for models whose live model-list entry advertises `capabilities.tools: true`.

See [OPENAI-COMPATIBLE.md](OPENAI-COMPATIBLE.md) for cURL and SDK examples. Muapi also exposes an Anthropic Messages proxy and an OpenAI Responses proxy for compatible agent clients; see [CLIENT-INTEGRATIONS.md](CLIENT-INTEGRATIONS.md) for setup notes.
