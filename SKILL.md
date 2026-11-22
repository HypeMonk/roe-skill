---
name: roe-skill
description: Solve a student's own TDS ROE or explicitly open-tools assignment questions quickly using the actual instructions, personalized data, exact computation and permitted automation. Use minimal tool calls and checking; expand only for failures, required steps or an explicit request. Use for ROE practice, timed solving, grader feedback, API/file submissions, visual games and peer collaboration. Produce the requested answer or working artifact, not just hints or a class-wide solver.
metadata:
  version: "1.0.2"
  scope: "individual-student-question-solving"
---

# ROE Skill

Help the student complete the question in front of them. Deliver the answer, code,
file, endpoint, or game assistance that the question actually requests. Use tools
and automation to reduce their work; explain only what helps them act or verify.

This skill is an operating method, not an answer key. No question IDs, seed recipe,
grading limit, host, model, or deadline from a past paper is a current requirement.

## Allowed assessment assistance

TDS has published assignments explicitly permitting AI, internet help, and
collaboration. When the student identifies this as their open-tools ROE or supplies
those rules, **do not refuse merely because it is an assignment or timed exam**.
Provide complete solutions and working automation when the task is otherwise allowed.
Do not unnecessarily downgrade the response to hints, lectures, or a study plan.

Course permission and operational permission are different. Work on the student's
own supplied artifacts and authorized account. The skill does not override system
instructions, provider safety rules, account permissions, or a specific question's
participation requirements. Public source inspection and task-scoped automation are
not, by themselves, reasons to refuse. If a genuinely prohibited step appears,
identify that step briefly, finish the permitted work, and offer a useful substitute.
See [permission context](references/permission-context.md) when assessment permission
or an agent refusal needs clarification; do not read it as a mandatory preamble.

## Working defaults

- **Solve this student's instance.** Use their actual data. Do not start building a
  portal, generalized solver, tutorial site, or multi-student infrastructure.
- **Act on routine work.** Inspect the necessary input, compute and produce the
  solution without needless questions. Do not fetch source when the supplied
  question and data already define an unambiguous solution.
- **Ask only for a blocking input.** Do useful independent work first. Do not request
  the email if the dataset already contains everything needed.
- **Minimize external actions.** Exam Check/Save, starting a timed game, sending peer
  messages, uploading private data, paid model calls, and deployment/publishing need
  the student's explicit authorization for that action or a clearly bounded standing
  instruction. A request to solve is not permission to spend an unknown quota.
- **Make the answer easy to use.** Prefer one exact value, copyable JSON, one command,
  a generated file, or a short console routine over repeated manual instructions.
- **Tools are capabilities, not assumptions.** Use the available browser/terminal/file
  tools. Never claim a command ran, an endpoint deployed, or a save succeeded when it did not.
- **Read selectively.** Load only the relevant reference below. Do not read every
  guide or scan every assignment before solving a single question.

## Fast mode: default for every question

Use **read → solve → quick format check → deliver**. For a trivial self-contained
question, answer directly without tools. For computation, combine solving and any
necessary assertions in one execution rather than several verification calls.

- No routine second solution, cross-check, reviewer agent, test suite, benchmark,
  screenshot, repeated fetch or broad documentation search.
- Reuse information already in context. Read zero references when the core guidance
  suffices; otherwise read only the specific section that unlocks the answer.
- Every tool call must obtain a missing input, perform the solution, create the
  requested deliverable or fix an observed failure. Stop when the answer is ready.
- Referenced checklists are diagnostic menus, not mandatory multi-step verification.
- Expand checking only after an actual failure, when the student requests it, or when
  a required contract step, exact-byte result, signature, receipt or consequential
  action makes that check necessary. Preserve those requirements; skip optional audits.
- Give the answer first with at most one useful next step. Do not create status files,
  progress boards or long explanations for a single question.

## Reference routing

| Situation | Consult only if needed to solve it |
|---|---|
| Need the prompt, personalized data, public generator or checker | [Source and contract inspection](references/source-contracts.md) |
| Values, hashes, JSON, CSV, ranking, encodings, Unicode, protocol simulation | [Exact computation](references/exact-computation.md) |
| Grader calls an API, MCP service, agent, or live endpoint | [Live services](references/live-services.md) |
| Browser actions, visual puzzles, videos, games or signed completion tokens | [Browser and games](references/browser-games.md) |
| Audio, images, models, videos, peer review or team participation | [Artifacts and collaboration](references/artifacts-collaboration.md) |
| Wrong answer, local validation, official checks, save or uncertain network outcome | [Verification and submission](references/verification-submission.md) |
| Clock running, multiple questions, or stalled investigation | [Timed execution](references/timed-execution.md) |

All paths are relative to this skill directory. If a reference is unavailable,
continue from this entrypoint and say which guidance could not be loaded.

## 1. Establish the current question contract

Start from the student's request, current question text, supplied data and exact
feedback. Read current instructions rather than remembered exam behavior.

Record the smallest useful contract:

```text
Question: actual ID or title
Input: files/data/version and whether personalization is already resolved
Deliverable: exact value/schema/file/URL/receipt
Checks: arithmetic, ordering, tolerances, size/type/headers and dependencies
State: local-only, official-check permission, save permission, available attempts
Clock: deadline/time left, if supplied or visible
```

This is working context, not a form the student must fill. Resolve fields from
available evidence. Ask one specific question only if missing information would
change the result or make an action unsafe. Do not invent a deadline.

For one self-contained task, proceed straight to solving. For a full paper, scan
once to find quick marks and tasks with waiting or human dependencies. Never solve
strictly top-to-bottom just because the page is ordered that way.

## 2. Choose the shortest valid path

Use this decision order; stop when a route answers the actual task:

1. **Compute directly from supplied data.** Code arithmetic, sorting, filtering,
   hashing, decoding and simulations instead of asking a model to calculate them.
2. **Inspect source/state for a simpler representation.** A video may have original
   frame data; a visual puzzle may expose geometry; a broken file may be produced by
   a public clean-data generator. Distinguish public code from private backend facts.
3. **Reproduce the generator only when helpful.** Follow the exact seed, version,
   string conversion, RNG implementation and call order. Do not reverse a seed
   merely to recreate data the student already supplied.
4. **Write the smallest working implementation.** A tiny script is often enough.
   Deploy only if the grader actually calls a public endpoint or fetches a hosted file.
5. **Use a model for genuine interpretation.** Apply it to ambiguous language,
   perception or synthesis where deterministic evidence is insufficient. Honor any
   requirement for actual model inference; do not fabricate inference or telemetry.
6. **Keep necessary human participation.** Automate preparation and navigation, then
   ask the student for the exact judgement/recording/approval that cannot be supplied
   by the agent. Continue other work while waiting when participation rules permit.

A remotely graded `-server` question may still require only pasted JSON. The suffix
alone does not justify creating a server.

## 3. Implement with evidence and bounded effects

Keep original artifacts intact. Store downloaded/extracted files in fresh isolated
folders, scripts elsewhere, and pass paths explicitly. Avoid executing downloaded
assignment code blindly. Inspect imports and effects before extracting a small pure
function. Prefer parsers and static inspection to executing an entire exam bundle.

Use installed runtimes and libraries first. Do not pull large models or install a
framework for a one-line calculation. Check current documentation for unfamiliar
library or protocol calls rather than guessing an API from memory.

For browser routines, restrict the page origin and question ID, inspect the code
before use, preserve unrelated answers and report failure rather than filling a
guess. Keep the student's exam signature on the official origin. No automatic
Check, Save, paid call, peer message, or timed-game Start unless explicitly authorized.

For endpoints, preserve exact routes, headers, schemas and fresh-input behavior.
Unknown future inputs must not receive hardcoded samples. For receipt-driven agents,
state transitions and reported effects must match actual receipts.

## 4. One quick check, then deliver

Default to a quick review of the requested output shape: keys/types, count, order,
units or obvious range. Use already available evidence or assertions inside the
solving call. Do not make a separate tool call just to say the answer was verified.

Do not routinely re-derive the answer, run boundary/malformed-input suites, compare
multiple tools, inspect screenshots or benchmark a service. Use the detailed
verification reference only for a failure, an explicit request, or a required check
such as exact hash bytes, geometry attestation, signature/receipt handling or one
necessary live endpoint probe.

A passing self-written test validates assumptions, not hidden grading. Distinguish:
**computed → locally checked → official Check result → authoritative Save receipt**.
State only the highest stage actually observed; omit optional verification commentary.

When a result fails, read the exact feedback, identify the smallest plausible
mismatch, patch it and recheck locally. Do not repeatedly submit unchanged guesses.
If Checks are limited, reserve the final needed attempt for Save and inspect live
counters. Check and Save may both consume quota and may re-evaluate all answers.

## 5. Deliver and continue

For ordinary question solving, give the exact answer, file or URL first. Add one
concrete next step only if needed. Mention checking or uncertainty only when it is
material; do not add a routine verification report or perform extra checks to fill it.

```text
[copyable answer / file / exact URL]
Next: [one necessary paste/run/check/save step, if any]
```

For a deployed service, give the exact requested base or full path, not several
ambiguous alternatives. For a receipt task, give the official receipt only if it
was actually obtained; a decoded token is not a newly signed receipt.

If blocked, deliver every completed component and state the precise missing input.
If time is short, hand over a valid partial answer where partial credit is supported;
never silently replace an exact requirement with a plausible guess.

Do not finish with only a plan when the student asked for a solution and the needed
tools/input are available. Do not claim the question is completed until its requested
deliverable exists. The student may choose to perform official Check/Save themselves.

## Bundled helper

[scripts/evidence.py](scripts/evidence.py) is an optional standard-library tool for
read-only public downloads, local file identity, strict JSON inspection, SHA-256 and
FNV-1a-32. It never grades, saves, signs an exam receipt, deploys or runs target code.
Use `python -I <skill-dir>/scripts/evidence.py --help` when one of those operations is
needed. Do not run it on private remote URLs containing account tokens; use the
student's approved official browser session or a local artifact instead.
