# Abliterated LLM Model Catalog

This catalog reflects the 21 endpoints shown on Muapi's Abliterated LLM page. Rates below are a point-in-time snapshot reviewed on **2026-11-10** and are shown in USD per million tokens. Recheck the [live model catalog](https://muapi.ai/abliterated-llm-api) before use; names, rates, schemas, and availability can change.

“Text + image” means the current endpoint schema includes `image_url`. “Thinking” means the current schema exposes a `thinking` option. These labels describe request fields, not measured model quality.

| Group | Model ID / API route | Input | Thinking | Input $/1M | Output $/1M |
|---|---|---|:---:|---:|---:|
| MiMo | `mimo-v2-6-flash-abliterated` | Text + image | — | 1.00 | 3.00 |
| Abliterated Model | `abliterated-model` | Text + image | — | 2.00 | 6.00 |
| Abliterated Model | `abliterated-model-large` | Text | — | 6.00 | 10.00 |
| Abliterated Model | `abliterated-model-large-v2` | Text | — | 6.00 | 10.00 |
| Qwen | `qwen-3-8-27b-abliterated` | Text + image | Yes | 0.30 | 2.40 |
| Qwen | `qwen-3-8-27b-obliterated` | Text + image | Yes | 0.50 | 3.00 |
| Qwen | `qwen-2-5-32b-abliterated` | Text | — | 1.40 | 1.40 |
| Qwen | `qwen-3-5-27b-queen-derestricted` | Text + image | — | 0.612 | 0.612 |
| Qwen | `qwen-3-5-27b-blossom-derestricted` | Text + image | — | 0.612 | 0.612 |
| Qwen | `qwen-3-5-27b-opus-distilled-derestricted` | Text + image | — | 0.612 | 0.612 |
| Llama | `llama-3-3-70b-abliterated` | Text | — | 1.40 | 1.40 |
| Llama | `neuraldaredevil-8b-abliterated` | Text | — | 0.88 | 0.88 |
| DeepSeek R1 | `deepseek-r1-llama-70b-abliterated` | Text | — | 1.40 | 1.40 |
| DeepSeek R1 | `deepseek-r1-qwen-32b-abliterated` | Text | — | 2.80 | 2.80 |
| GLM | `glm-5-3-flash-abliterated` | Text + image | — | 0.40 | 1.60 |
| GLM | `glm-5-3-abliterated` | Text | — | 2.50 | 4.50 |
| GLM | `glm-4-6-derestricted-v5` | Text | — | 0.80 | 3.00 |
| Gemma | `gemma-4-26b-a4b-abliterated` | Text | — | 0.30 | 1.40 |
| Gemma | `gemma-4-31b-gembrain-abliterated` | Text + image | — | 0.612 | 0.612 |
| Gemma | `gemma-4-31b-sdft-abliterated` | Text + image | — | 0.612 | 0.612 |
| DeepSeek V4 | `deepseek-v4-1-flash-abliterated` | Text | Yes | 0.66 | 2.64 |

## Reading the table

- The model ID is also the path segment for the submit and stream routes.
- Input and output rates are separate. Estimate a request using the prompt and completion token counts, then verify the actual billing shown in your Muapi account.
- The published model page and live schema take precedence over this snapshot.
- A displayed `thinking` option is not a promise that every response will expose private reasoning. Use it as the API control documented for that model.
- Image inputs can change cost and token use. Check the model's current image limits before sending large or sensitive files.

## Endpoint count

The table contains 21 endpoints: Abliterated Model (3), MiMo (1), Qwen (6), Llama (2), DeepSeek R1 (2), GLM (3), Gemma (3), and DeepSeek V4 (1). The separate low-refusal catalog may include other endpoints that are not part of this 21-model page.
