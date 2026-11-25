#!/usr/bin/env bash
set -euo pipefail

: "${MUAPI_API_KEY:?Set MUAPI_API_KEY before running this example}"
API_ROOT="https://api.muapi.ai/api/v1"
MODEL_ID="${MODEL_ID:-qwen-3-8-27b-abliterated}"

SUBMIT_RESPONSE=$(curl --fail-with-body --silent --show-error \
  -X POST "${API_ROOT}/${MODEL_ID}" \
  -H "x-api-key: ${MUAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Explain the difference between a queue and a stack in three sentences.","max_tokens":256}')

REQUEST_ID=$(printf '%s' "$SUBMIT_RESPONSE" | python3 -c 'import json,sys; print(json.load(sys.stdin)["request_id"])')
printf 'Submitted request %s\n' "$REQUEST_ID"

for attempt in $(seq 1 120); do
  RESULT=$(curl --fail-with-body --silent --show-error \
    "${API_ROOT}/predictions/${REQUEST_ID}/result" \
    -H "x-api-key: ${MUAPI_API_KEY}")
  STATUS=$(printf '%s' "$RESULT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("status", ""))')
  case "$STATUS" in
    completed)
      printf '%s\n' "$RESULT" | python3 -c 'import json,sys; d=json.load(sys.stdin); print("\n".join(str(x) for x in d.get("outputs", [])))'
      exit 0
      ;;
    failed)
      printf '%s\n' "$RESULT" >&2
      exit 1
      ;;
    pending|processing)
      sleep 1
      ;;
    *)
      printf 'Unexpected status: %s\nResponse: %s\n' "$STATUS" "$RESULT" >&2
      exit 1
      ;;
  esac
done

printf 'Timed out waiting for request %s\n' "$REQUEST_ID" >&2
exit 1
