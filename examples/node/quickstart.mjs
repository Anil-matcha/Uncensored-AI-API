const apiKey = process.env.MUAPI_API_KEY;
const modelId = process.env.MODEL_ID ?? "qwen-3-8-27b-abliterated";
const apiRoot = "https://api.muapi.ai/api/v1";

if (!apiKey) {
  throw new Error("Set MUAPI_API_KEY in your environment.");
}

async function apiRequest(path, options = {}) {
  const response = await fetch(`${apiRoot}${path}`, {
    ...options,
    headers: {
      "x-api-key": apiKey,
      "content-type": "application/json",
      ...options.headers,
    },
  });
  const body = await response.json();
  if (!response.ok) {
    throw new Error(`Muapi returned HTTP ${response.status}: ${JSON.stringify(body)}`);
  }
  return body;
}

const submitted = await apiRequest(`/${modelId}`, {
  method: "POST",
  body: JSON.stringify({
    prompt: "Explain the difference between a queue and a stack in three sentences.",
    system_prompt: "You are a concise programming tutor.",
    max_tokens: 256,
  }),
});

const requestId = submitted.request_id;
console.log(`Submitted request ${requestId}`);
const deadline = Date.now() + 120_000;

while (Date.now() < deadline) {
  const result = await apiRequest(`/predictions/${requestId}/result`);
  if (result.status === "completed") {
    console.log((result.outputs ?? []).join("\n"));
    process.exit(0);
  }
  if (result.status === "failed") {
    throw new Error(result.error ?? "Generation failed.");
  }
  if (!["pending", "processing"].includes(result.status)) {
    throw new Error(`Unexpected prediction status: ${result.status}`);
  }
  await new Promise((resolve) => setTimeout(resolve, 1000));
}

throw new Error(`Timed out waiting for request ${requestId}`);
