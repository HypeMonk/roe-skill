# Grader-called services and agents

## Decide whether a service is necessary

Read what the grader does. These are different deliverables:

- pasted value/JSON, remotely verified: compute locally;
- public JSON file fetched by GET: compute, then host the actual file after approval;
- exact POST route: implement and give that full route;
- base URL with paths appended: give the specified base, not a guessed suffix;
- MCP or multi-turn agent: implement the protocol and lifecycle, not a static reply.

A console script can prepare an endpoint answer but cannot make localhost reachable
to an external grader. A public tunnel or deployment is needed only when the contract
requires external reachability. Prepare locally while obtaining hosting approval.

## Minimum live contract

Extract before coding:

```text
methods and exact paths
content types, status codes and redirects
request/response schema; fresh randomized fields
authentication; allowed origins and preflight
time/body/file limits; concurrency
state, durability, idempotency and receipts
what is checked now vs later
```

Prefer an existing suitable runtime and a small app. One app may serve several
questions for this student, but isolate conflicting state and middleware profiles.
Do not build multi-tenant registration, billing or a universal portal.

## Fresh input must be processed

For stats, aggregate the incoming numbers. For invoice extraction, parse the actual
vendor/amount/currency/date. For signatures, verify against the assigned algorithm,
key, issuer, audience and expiry. For counters, use the required real storage.
For pagination, return the required catalog without gaps or repeats.

Never hardcode worked examples as responses to unknown future requests. Do not
pretend a dictionary is Redis, a canned response is model inference, or a static
metrics file is a live counter when those mechanisms are required.

## Headers and CORS are task-specific

- Read the exact allowed-origin rule. Some tasks require `*`; others explicitly
  forbid it and test that an unapproved origin gets no ACAO header.
- Support the required OPTIONS preflight without accidentally triggering auth or
  state changes, unless the contract says otherwise.
- Expose response headers needed by a browser checker through
  `Access-Control-Expose-Headers` when necessary.
- Preserve request-ID generation/echo rules and required process-time values.
- Return JSON media type, nonredirecting routes and the expected status codes.

A server-side fetch is not necessarily subject to browser CORS. Do not spend time
fixing CORS when the actual failure is DNS, TLS, path, content type or JSON shape.

## MCP

Use the actual transport/version. A minimal contract may require initialize,
initialized notification, tools/list and tools/call. Headers can change on every
call; read them from the current HTTP request rather than an earlier initialization.
Tool names, schemas, text-block shape, hashing and registered identity must match.

Signature verification described as optional is not a scoring requirement. Never
invent the examiner's private key. A fresh challenge makes a static token invalid.

## Multi-turn agents and receipts

Separate decision logic, state persistence, receipt validation and telemetry.

- Store proposals before returning them.
- Bind identity, task/run/evaluation, proposal, action/call, attempt and receipt.
- Validate all receipt signatures and bindings before applying any effect.
- Accept only current pending transitions; reject changed-content replays atomically.
- Exact replay must not repeat a payment, effect or model call.
- Retain durable state when required; process memory alone cannot survive a restart.
- Rebuild neither past actions nor telemetry from an assumed outcome.
- Handle retry, timeout, approval, cancellation and join rules exactly as published.

Do not cache a model call out of a workflow that explicitly requires actual planning
in each new run. Do not fabricate model names, token usage, action attempts, receipt
nonces or trace spans. Cache only what the current contract allows.

## Model-assisted decisions

Use available, documented providers only after the student authorizes the budget.
Keep credentials in environment/secret settings, out of transcripts and files that
will be published. Use models for interpretation; normal code enforces schemas,
canonical hashing, exact amounts, storage and signature verification.

Bound calls by the remaining request and exam deadlines. Validate model output and
fail explicitly on unsupported/ambiguous input. Do not exhaust an account with
unbounded retries or select a provider merely to evade a refusal.

## Deployment and live verification

1. Implement and test local HTTP requests, malformed input and critical boundaries.
2. Check that the approved host/tunnel can meet the route and runtime requirements.
3. Deploy/expose only after authorization. Do not alter unrelated live services.
4. GET the exact health/answer URL and perform permitted non-scored probes.
5. Verify content type, TLS, redirect behavior, headers and latency.
6. Give one exact submission URL. Clearly label local vs public paths.
7. An official Check is a separate authorized quota-consuming action.

A health 200 does not prove every route works. A local test does not prove deployment.
A free-host warm-up does not guarantee future latency or persistence. Keep the app
reachable for the contract's required period; do not claim hosting is permanent.

## Failure triage

Classify the first failing layer: reachability → path/method → media/schema →
auth/headers → decision semantics → lifecycle/receipts → durability → timing.
Capture the actual failed request and response with sensitive fields redacted.
Fix one supported mismatch and test it locally before spending another official Check.
