# Safety, Limits, and Responsible Use

“Abliterated,” “obliterated,” and “derestricted” describe model variants or serving labels associated with reduced refusal behavior. They do not mean that the model is unrestricted, accurate, harmless, or guaranteed to comply with a request.

## Practical limits

- Outputs can be incorrect, incomplete, biased, or inconsistent across repeated runs.
- A model can still refuse a request. Behavior may change when the model or serving configuration changes.
- Image input is available only on the endpoints marked accordingly in the [model catalog](MODEL-CATALOG.md).
- The service schema, account limits, current rates, and provider terms govern actual usage. This guide is not a substitute for those current terms.
- Keep a human review step for consequential decisions, public content, code changes, and actions that affect other people.

## Application safeguards

- Validate and constrain user input where your product requires it.
- Treat model output as untrusted data. Escape it before rendering HTML and validate structured output before execution.
- Require explicit authorization and confirmation before an agent takes external or destructive actions.
- Protect credentials and avoid placing API keys in client-side code or logs.
- Minimize retention of prompts, responses, and image URLs; avoid sending sensitive data unless you have assessed the applicable privacy and service terms.
- Follow applicable law, Muapi terms, and the terms attached to each model.

Use this API for lawful development, research, and creative work. You are responsible for the way your application uses model outputs.
