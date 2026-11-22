# Timed ROE execution

## Scope and clock

A 45-minute ROE is an expected context, not a hardcoded duration for every task.
Use the actual start/deadline/time remaining when supplied or visible. Do not start
an attempt or game to discover its clock without permission. Use server deadlines
when available; the student's local clock may differ.

For one question, solve it immediately. Do not demand the entire paper before
answering a self-contained question. Use the minimal tool path and one quick format
check; skip routine reference loading, repeated calculations and optional audits.
For a supplied full paper, scan once for weights, output modes and dependencies,
then choose an order.

## Triage by deliverable and bottleneck

| Kind | First useful action | Avoid |
|---|---|---|
| Exact pasted value | Compute and validate | Long explanatory tutorial |
| Public endpoint | Prepare local contract; expose after approval | Building unnecessary infrastructure |
| Hosted file | Generate/validate, arrange approved upload | A viewer/share page mistaken for raw data |
| Visual game | Inspect state/frames/validator | Watching/dragging when structured data exists |
| Human or peer ingredient | Ask for one concrete action early | Waiting idle or inventing participation |
| Model-judged/open-ended | Inspect rubric and actual evidence | Generic polished text with no supporting facts |

Prioritize expected earned marks per **active** minute while accounting for dependencies,
waiting, confidence and minimum valid partial credit. Do not rank only by mark weight
or visual complexity. Treat these estimates as judgement, not calibrated statistics.

## Adaptable 45-minute rhythm

When a full 45-minute paper is supplied, a starting allocation is:

- **0–3 min:** capture contract/weights, find quick outputs and slow dependencies.
- **3–8 min:** produce fast answers and start authorized peer/render/hosting work.
- **8–35 min:** highest-value exact computations and implementation.
- **35–41 min:** repair important failures and complete supported partial answers.
- **41–45 min:** explicit required official submission and readback.

Adapt immediately to shorter remaining time, a long live session, or a different
paper. Reserve a final window earlier if Save itself triggers lengthy revalidation.
Do not begin an unfinishable timed game merely because it has many marks.

## Small working queue

Maintain a concise queue only when multiple questions are in play:

```text
Q | marks | deliverable | ready/waiting/blocked | next action | official attempts
```

Read only the relevant files and references for the next action. Preserve complete
raw artifacts on disk; summarize evidence in context rather than repeatedly dumping
large bundles. Do not spawn agents, workflows or paid research unless authorized
and the independent work/time benefit justifies their cost.

## Parallelize latency, not attention requirements

Independent computation, a health warm-up, rendering and a pending peer reply may
run concurrently. Do not block frame processing on a service cold start when neither
depends on the other. Use completion notifications for background jobs instead of
repeated polling when the environment provides them.

A game requiring continuous participation cannot be abandoned while doing another
task. Honor its phase rules, real participant roles and approval deadlines. Automation
can prepare work, not shorten a server-enforced session.

## A stalled-question rule

For an unexplained failure, spend a short bounded interval checking the likely
mismatch. Reassess after about 3–4 active minutes in a 45-minute paper, earlier near
the deadline. If no new evidence appears, change approach, request the missing
artifact, or park the task and take available marks elsewhere.

A timeout does not prove impossibility. A single model failure does not prove a
question cannot be solved. Conversely, repeating the same assumption is not progress.

## Short-deadline response

When little time remains:

1. Give existing validated outputs immediately.
2. Check which partially complete structures can actually earn partial credit.
3. Avoid new model downloads, infrastructure and broad refactoring.
4. Tell the student exactly which approved Check/Save action remains.
5. Preserve the distinction between ready answers and authoritative submission.

For example:

> Q6's probe deliveries and origin count are computed. The final digest is still
> unverified. The contract gives independent component credit. Here is a well-formed
> partial certificate; save it only if you choose to use the remaining attempt.

Do not give malformed JSON or claim an unverified component is correct. Use the
question's actual partial-credit and schema rules.
