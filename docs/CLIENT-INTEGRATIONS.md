# Client and Agent Integrations

Muapi exposes several interfaces for different clients. Choose the interface the client expects and use a model ID returned by that interface's model-list endpoint. Tool use requires a model that advertises tool support.

| Client type | Muapi interface | Base URL |
|---|---|---|
| Direct HTTP app | Per-model REST + poll or SSE | `https://api.muapi.ai/api/v1` |
| OpenAI SDK, OpenCode, or chat UI | OpenAI Chat Completions | `https://api.muapi.ai/v1` |
| Claude Code | Anthropic Messages proxy | `https://api.muapi.ai/anthropic` |
| Codex CLI | OpenAI Responses proxy | `https://api.muapi.ai/openai/v1` |

## OpenAI-compatible clients

Use the setup and SDK example in [OPENAI-COMPATIBLE.md](OPENAI-COMPATIBLE.md). Before configuring an agent or function-calling workflow, inspect `GET https://api.muapi.ai/v1/models?type=text` and choose a model with `capabilities.tools: true`.

## Claude Code

The Anthropic Messages proxy can connect Claude Code to selected tool-capable Muapi models. This is a separate interface from the `prompt`-based single-turn routes.

```bash
export ANTHROPIC_BASE_URL="https://api.muapi.ai/anthropic"
export ANTHROPIC_AUTH_TOKEN="$MUAPI_API_KEY"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen-3-8-27b-obliterated"
export ANTHROPIC_SMALL_FAST_MODEL="qwen-3-8-27b-obliterated"
claude --model qwen-3-8-27b-obliterated
```

List the proxy's current model IDs first:

```bash
curl -s "https://api.muapi.ai/anthropic/v1/models" \
  -H "Authorization: Bearer $MUAPI_API_KEY"
```

Claude Code may issue background requests using its configured small-model alias. Set the two small-model variables to a model ID returned by the endpoint. Keep the key in your shell environment or a local secret store; do not commit it in project settings. Quality, context limits, and cost vary by model, so review the result of each coding action.

## Codex CLI

Muapi's OpenAI Responses proxy is available to Codex CLI through a custom provider. Check available model IDs:

```bash
curl -s "https://api.muapi.ai/openai/v1/models" \
  -H "Authorization: Bearer $MUAPI_API_KEY"
```

Add a provider to the user-level `~/.codex/config.toml` file, substituting a returned model ID that supports the tools you need:

```toml
model = "qwen-3-8-27b-obliterated"
model_provider = "muapi"

[model_providers.muapi]
name = "Muapi"
base_url = "https://api.muapi.ai/openai/v1"
env_key = "MUAPI_API_KEY"
wire_api = "responses"
```

Export the key in the shell that launches Codex:

```bash
export MUAPI_API_KEY="your_muapi_api_key"
```

Model support and protocol behavior can change. Verify the returned model list, start with a small read-only task, and review changes before accepting them. Large agent contexts can consume more tokens because each request may include the conversation history.

## OpenCode

Configure OpenCode as an OpenAI-compatible provider using the base URL `https://api.muapi.ai/v1`, then choose a model that advertises tool support in `/v1/models?type=text`. Follow the current [OpenCode provider setup](https://muapi.ai/docs/opencode) for the complete configuration because client configuration formats can change.

## Direct REST

For one prompt at a time, use a model-specific route. Send `prompt` and supported optional fields to `POST /api/v1/{model-id}`, then poll for completion or use its `/stream` route. See [API.md](API.md).
