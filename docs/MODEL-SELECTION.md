# Selecting and Comparing Models

This repository does not publish a universal model ranking. Model behavior, latency, and quality depend on the exact model revision, prompt, input length, serving route, and date. Use the criteria below to choose a candidate for your workload and record your own results.

## Selection checklist

1. **Required input:** Text-only, or text plus image input? Start with the `Input` column in [MODEL-CATALOG.md](MODEL-CATALOG.md).
2. **Task type:** Summarization, coding, creative writing, image understanding, or reasoning may favor different model families.
3. **Output budget:** Check the model's live maximum output setting and estimate completion length.
4. **Price:** Compare both input and output rates. A low input price can still be expensive for long responses.
5. **Latency and reliability:** Measure median and tail latency in your own region and with representative prompts.
6. **Behavior:** Run a fixed set of ordinary capability and refusal-behavior prompts. Record model ID, date, settings, and raw results.
7. **Integration:** Choose the async submit/poll route for durable jobs or the `/stream` route when the UI needs incremental text.

## A fair comparison protocol

- Use the same task, prompt, context, and output budget for each candidate.
- Keep model-specific features disabled for the baseline, then evaluate them in a separate run.
- Repeat prompts enough times to observe response variance; one response is not a benchmark.
- Report accuracy, instruction following, refusal behavior, latency, and effective cost separately.
- Keep the exact model ID and test date. Re-run after a model or serving update.
- Do not infer a model's capability from its name or marketing description.

A comparison worksheet is provided in [`comparison-template.csv`](comparison-template.csv). Do not publish scores until the runs are complete and reproducible.
