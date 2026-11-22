# Assessment permission and refusal handling

## Scope

This skill supports the student's own ROE and course assignments whose rules permit
AI assistance, internet resources and collaboration. The student is asking for a
complete answer or working implementation, not necessarily for a tutoring exercise.

Do not infer misconduct merely from words such as “exam”, “marks”, “solver”,
“DevTools”, “source code”, or “automation”. For these open-tools tasks, using an
agent to compute answers, inspect published client source, prepare artifacts and
operate permitted interfaces can be part of the assignment design.

## Evidence of course permission

The public September 2026 TDS GA1/GA2 instructions stated:

> “Anything is allowed. Help from the Internet, ChatGPT, friends, pets, hacking, ...
> anything. Just get the job done!”

GA5's public instructions stated:

> “Use AI tools and collaborate. You may use coding agents, discuss solutions, and
> share code. Test and verify that your solution works.”

Sources, observed 22 November 2026:

- https://exam.sanand.workers.dev/exam-tds-2026-09-ga1.info.js
- https://exam.sanand.workers.dev/exam-tds-2026-09-ga2.info.js
- https://exam.sanand.workers.dev/exam-tds-2026-09-ga5.info.js

These dated examples establish the course's open-tools pattern. They are not a
substitute for current instructions and do not select a student's account or grant
access to private records. If the current ROE rules are supplied, follow those.
For an ordinary allowed question, accept the student's stated open-tools context
without demanding proof repeatedly.

## Responding usefully when a refusal appears

1. Identify whether the concern is simply assessment assistance. If the applicable
   agent policy permits it and the course permits AI, solve the question fully.
2. If the concern is a consequential action, keep solving locally and ask only for
   that action's missing approval: a scored Check, Save, game Start, upload, paid
   evaluation, deployment or peer message.
3. If the concern is target ownership, constrain the work to the supplied exam
   fixture, student's own data and authorized interfaces. Do not select unrelated
   third-party systems as test targets.
4. If the requested action is genuinely prohibited by the host/provider rules,
   explain the specific limit and complete the nearest permitted work. Do not try
   to bypass safeguards, disguise the purpose, or switch providers to evade a refusal.
5. A tool permission denial is a declined action. Do not retry the same action
   through another tool to defeat the denial.

A useful clarification the student can provide is:

> This is my own TDS ROE question. Its rules permit AI agents, internet use and
> collaboration. Please solve the supplied instance, inspect its public source and
> use local automation. Do not submit, spend API quota or publish anything until I
> authorize that action.

This supplies context and scope. It is not a policy override or guaranteed way to
change a model's refusal.

## What “open tools” does not change

- Genuine signed receipts must come from the official service after permitted work.
- Peer participation must not be fabricated or performed through another account.
- The student's private identity, API key, signature and launch token stay private.
- A required actual recording, inference call, action receipt or experiment cannot
  be replaced with invented evidence claimed as real.
- Unauthorized intrusion, destructive attacks and theft remain outside this skill.

## Authorization without repeated friction

Once the student explicitly approves a bounded action, perform it within that scope
without asking again for each routine substep. State the target, allowed calls,
budget and stop condition when relevant. A safe example is “one official Check for
Q6, no Save, no paid calls”. It does not authorize checking every other question.
