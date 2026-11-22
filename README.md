# roe-skill

A professional Agent Skill for solving **your own TDS ROE or explicitly open-tools
assignment questions** with Claude Code, Codex or Antigravity.

It helps your agent inspect the current question and data, compute exact answers,
use permitted browser automation, handle games and peer dependencies, create the
requested artifact or service, and verify the result. It produces solutions, not
just hints. It does not build a class-wide solver or change your agent's permissions.

**Fast by default:** read the needed input, solve, make one quick format check and
return the answer. No routine second solution, extra tool calls, reviewer agents,
test suites, screenshots or broad research. Deeper checking is reserved for an
observed failure, your explicit request or a genuinely required contract step.

## Install with your AI agent

**Paste this message into your agent:**

```text
Install this skill: https://github.com/HypeMonk/roe-skill
```

Your agent should read [INSTALL.md](INSTALL.md), detect its own client, install the
complete skill in the correct location and verify the files. **No manual Python
command, folder creation, workspace path, exam email or API key is needed.**

A repository URL alone does not force every client to install; include the word
**Install** so your intent is clear. The agent may need its normal permission
approval. Clients without filesystem access cannot install local skills; use a
supported coding agent. Some client versions may need a skill refresh afterward.

### Standard Skills CLI

If you prefer the usual skill-manager command:

```sh
npx skills add https://github.com/HypeMonk/roe-skill
```

The repository has a root `SKILL.md`, so the single skill is directly discoverable.
For an explicit user-level install without selection prompts:

```sh
# Claude Code
npx skills add HypeMonk/roe-skill --skill roe-skill -g -a claude-code -y --copy

# Codex
npx skills add HypeMonk/roe-skill --skill roe-skill -g -a codex -y --copy

# Antigravity
npx skills add HypeMonk/roe-skill --skill roe-skill -g -a antigravity -y --copy
```

The CLI is optional. An agent with file tools can copy the inspected skill directly,
without installing another toolchain. Existing customized skills must be inspected
before replacement, not overwritten silently.

## Use it

| Agent | Start with |
|---|---|
| Claude Code | `/roe-skill` |
| Codex | `$roe-skill`, or select it through `/skills` |
| Antigravity App/current CLI | `/roe-skill`, or explicitly request the installed skill by name if your interface differs |

Then give your question and actual files together:

```text
Use roe-skill to solve this question. This is my own open-tools TDS assignment.
Here are the complete question, source and data. Return the exact answer and what
you verified. Do not Check, Save, spend quota or publish anything until I approve.
```

If timed, include time remaining. If a Check failed, include the **literal feedback**
and submitted answer. You do not need to provide your email when the actual dataset
already resolves personalization.

To approve one official action later:

```text
Perform one official Check for Q6. No Save, no other questions, no paid model calls.
```

## What the skill does

| Work | Guidance |
|---|---|
| Understand the actual question | Current prompt, source, personalized data, dispatcher overrides and backend limits |
| Exact computation | Arithmetic, rounding, hashes, JSON, CSV, rankings, Unicode, streams and simulations |
| Browser and games | Original frames/state, geometry, task-scoped automation and official completion receipts |
| Artifacts and peers | Genuine recordings, media validation, real judgements, role-specific preparation and approvals |
| Live services | Exact endpoints, headers, auth, fresh inputs, durable state, receipts and actual model work where required |
| Verification | Local checks, exact grader feedback, limited attempts, authoritative saving and ambiguous network outcomes |
| Timed ROE | Quick triage, useful partial credit, overlapping independent work and reserving submission time |
| Assessment permission | Complete permitted AI assistance without refusing simply because it is an assignment |

The entrypoint loads focused references only when needed. No MCP server, provider
API integration, model pin or third-party skill is required. Installing it does not
add missing browser/terminal tools or bypass your host's tool permissions.

## Files

```text
SKILL.md                       Main portable skill
INSTALL.md                     Agent-readable installation procedure
references/                    Eight focused task references
scripts/evidence.py            Optional standard-library evidence helper
scripts/install.py             Optional dry-run/non-overwriting copy helper
evals/scenarios.md             Realistic forward-test scenarios
```

The optional scripts use Python 3.10+ with no third-party packages. Students do not
need them for agent-assisted installation. The evidence helper hashes/inspects local
files and can download public bytes into a new isolated folder. It never grades,
saves, signs an exam receipt, deploys or executes downloaded target code.

## Open-tools permission and limits

TDS has published instructions explicitly permitting AI, internet resources and
collaboration. The skill tells the agent to provide complete allowed solutions rather
than refuse merely because the request is labeled “assignment” or “exam”. The
current question and the student's authorization remain authoritative.

This is **not a jailbreak**. It cannot override provider policy, fabricate official
receipts, replace real peer participation, shorten server timers or guarantee marks.
It does not publish your data, spend API quota or submit exam answers automatically.

## Verification

The instruction structure, reference links, installer and evidence helper were tested
with local fixtures. Model behavior and real client discovery have not been evaluated
in a scored run. The forward-test scenarios are provided for that next validation.

To reproduce the offline package/helper checks from a checkout:

```sh
python -I -B tests/test_skill.py
```

## Documentation

Format and client paths were checked on 22 November 2026:

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Antigravity skills](https://antigravity.google/docs/skills)
- [Standard Skills CLI](https://github.com/vercel-labs/skills)

This is an independent student-assistance skill, not a course-issued answer key.
