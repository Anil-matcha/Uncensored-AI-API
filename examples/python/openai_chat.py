#!/usr/bin/env python3
"""Call a Muapi text model through the OpenAI-compatible chat endpoint."""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MUAPI_API_KEY"],
    base_url="https://api.muapi.ai/v1",
)

response = client.chat.completions.create(
    model=os.environ.get("MODEL_ID", "qwen-3-8-27b-abliterated"),
    messages=[
        {"role": "system", "content": "You are a concise programming tutor."},
        {"role": "user", "content": "Explain idempotency in two sentences."},
    ],
    max_tokens=256,
)
print(response.choices[0].message.content)
