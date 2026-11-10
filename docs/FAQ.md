# FAQ and Troubleshooting

## How do I choose a model?

Start with the [model catalog](MODEL-CATALOG.md). Check input modality, current input/output price, and the model's live schema. Then compare candidates with the method in [MODEL-SELECTION.md](MODEL-SELECTION.md).

## Is this a single OpenAI-compatible chat endpoint?

The individual model route uses Muapi's `prompt` field. Muapi also exposes separate OpenAI-compatible Chat Completions and Anthropic Messages interfaces. See [OPENAI-COMPATIBLE.md](OPENAI-COMPATIBLE.md) and [CLIENT-INTEGRATIONS.md](CLIENT-INTEGRATIONS.md).

## How do I get the text result?

Submit a request, save `request_id`, then poll `/api/v1/predictions/{request_id}/result` with the same API key. On completion, read the text from `outputs`.

## Can I stream output?

Yes. Use `POST /api/v1/{model-id}/stream` and consume its SSE response. The stream ends with a `[DONE]` event. See the streaming example in [API.md](API.md).

## Which models accept images?

The model catalog marks those routes as `Text + image`. For those models, send a reachable image URL in `image_url`. Do not assume image input works on every LLM route.

## Why is my model ID rejected?

Use the exact current ID from the Muapi model page. Check spelling, API key access, and current availability. Model IDs can change as the catalog evolves.

## Why is my request still pending?

A queued generation may take time. Poll at a measured interval, set a client timeout, and stop polling after `completed` or `failed`. The examples use a one-second interval and a finite deadline.

## The model failed. Should I retry?

First inspect the response status and error, verify the request fields against that model's schema, and check current service status. Retry only if the failure is plausibly transient and your application can safely handle duplicate work.

## Are the listed prices guaranteed?

No. The table is a dated snapshot. Check the live Muapi page and your account's usage details for current rates and actual billing.
