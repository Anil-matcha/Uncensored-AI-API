#!/usr/bin/env python3
"""Submit one Muapi LLM request and poll for its text result."""

import json
import os
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_ROOT = "https://api.muapi.ai/api/v1"
MODEL_ID = os.environ.get("MODEL_ID", "qwen-3-8-27b-abliterated")
API_KEY = os.environ.get("MUAPI_API_KEY")


def request_json(url: str, *, method: str = "GET", body: dict | None = None) -> dict:
    if not API_KEY:
        raise RuntimeError("Set MUAPI_API_KEY in your environment.")
    payload = None if body is None else json.dumps(body).encode("utf-8")
    request = Request(
        url,
        data=payload,
        method=method,
        headers={
            "x-api-key": API_KEY,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Muapi returned HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Could not reach Muapi: {exc.reason}") from exc


def main() -> None:
    submitted = request_json(
        f"{API_ROOT}/{MODEL_ID}",
        method="POST",
        body={
            "prompt": "Explain the difference between a queue and a stack in three sentences.",
            "system_prompt": "You are a concise programming tutor.",
            "max_tokens": 256,
        },
    )
    request_id = submitted["request_id"]
    print(f"Submitted request {request_id}")

    deadline = time.monotonic() + 120
    while time.monotonic() < deadline:
        result = request_json(f"{API_ROOT}/predictions/{request_id}/result")
        status = result.get("status")
        if status == "completed":
            print("\n".join(str(item) for item in result.get("outputs", [])))
            return
        if status == "failed":
            raise RuntimeError(result.get("error", "Generation failed."))
        if status not in {"pending", "processing"}:
            raise RuntimeError(f"Unexpected prediction status: {status!r}")
        time.sleep(1)

    raise TimeoutError(f"Timed out waiting for request {request_id}")


if __name__ == "__main__":
    main()
