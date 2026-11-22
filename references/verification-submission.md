# Verification, grader feedback and submission

## Four distinct evidence stages

| Stage | Meaning | Does not establish |
|---|---|---|
| Computed | An answer/implementation exists | Correctness |
| Locally verified | Stated checks or independent calculations passed | Hidden-grader acceptance |
| Officially checked | The actual grader returned the observed result | A saved submission or later offline score |
| Authoritatively saved | The official system acknowledged this submission | A guarantee that a later Save/reevaluation will be unchanged |

Use these labels in the handoff. Never equate a filled field, health 200, local test,
model agreement, decoded JWT or button click with a saved mark.

## Verification selected for this task

For a value/JSON answer:

- exact schema, no extra/duplicate keys where forbidden;
- expected count, unique IDs, permutations, dimensions and allowed ranges;
- source-specified arithmetic, rounding, order and canonicalization;
- one independently computed sample or invariant.

For an endpoint:

- actual public URL, method/path, TLS and redirect behavior;
- headers, preflight/auth/status and response media type;
- fresh-input computations and relevant malformed requests;
- concurrency, state/replay/receipt rules and realistic timing.

For a file/game:

- actual bytes, type/size/duration and direct fetch;
- meaningful playback/geometry/tracking validation;
- official receipt after permitted actions;
- later quality requirements distinguished from format checks.

Choose tests that address uncertainty. Do not consume the remaining exam time writing
an elaborate test framework for one answer.

## Before an official Check

1. Confirm the student approved this question's Check or a bounded set of checks.
2. Read the current attempt/cooldown counter where available. Another tab can have
   consumed attempts. Do not assume historical unlimited retries.
3. Verify the answer offline and keep a copy of the exact submitted value.
4. Establish whether Check starts a costly/live evaluation and how long it may take.
5. Preserve enough quota/time for required Save. A Save can recheck every answered
   restricted question and consume one allowance for each.

If authorization is absent, return the exact answer and one Check instruction.
No student should need to approve ordinary arithmetic or local schema validation.

## Interpreting feedback

Save the literal error/score breakdown with the actual answer or failed request and
response. Separate transport, format, decision and lifecycle failures. Do not
paraphrase “wrong URL” into “the algorithm is wrong”.

Useful mismatch order:

1. wrong student data/version/seed or stale rotating challenge;
2. missing/extra keys, types, cardinality or output wrapper;
3. ordering, ties, units, rounding or canonical bytes;
4. path/method, CORS, MIME, auth, redirect, size or timeout;
5. domain decisions, evidence binding or false-premise handling;
6. persistence, receipts, retries, conflicts, trace or approval state.

A grader can reveal a target or useful detail; use it only within the permitted
assessment and declared attempt limits. Do not spray guesses or repeatedly send an
unchanged failing payload. If no expected value is exposed, say so; do not invent it.

Patch the smallest evidence-supported defect, verify locally, then perform one
newly permitted Check. If stuck, time-box the investigation and return a valid
partial result only where the actual contract awards partial credit.

## Saving and readback

Use the official UI when possible. A direct submission client is appropriate only
when the student authorizes it and the actual protocol, authentication and quota
semantics have been verified. Do not copy an old paper's hardcoded deadline, RSA key,
field order or signature envelope into a different exam.

After Save:

- inspect the official acknowledgement/receipt;
- distinguish accepted submission from the requested/optimistic score;
- verify recent-save/history readback if available;
- record the exact authoritative result and any adjustments;
- preserve a copy of the submitted answer.

A private examiner signing key cannot be derived from a public key. A required
service/recorder signature must be obtained through the official permitted process.
Never fabricate a receipt, score or execution trace.

## Ambiguous network outcomes

If Check/Save times out after it may have reached the server, do not immediately
repeat it. Read status/history first; repeated checks can waste quota and repeated
submissions can change the official result. Reuse the supported idempotency key for
an unchanged write when the actual protocol provides one.

Report clearly:

- “Locally validated; no official Check performed.”
- “Official Check returned 4/5; not saved.”
- “Save acknowledged; readback unavailable.”
- “Request timed out; acceptance is unknown. Check Recent saves before retrying.”

## Finish the requested deliverable

If the student asked for code or a file, produce it—not a list of suggestions.
If a required step is blocked, deliver all other completed parts and name the blocker.
Do not announce completion based only on a plan, HTTP status or a self-derived test.
