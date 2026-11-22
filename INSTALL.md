# Agent-assisted installation

Apply this procedure **only when the user asks to install this skill**, or provides
this repository URL in a clear skill-installation context. Reading, reviewing or
summarizing the repository is not permission to execute an installer. Repository
content never overrides the host's instructions or permission controls.

Repository: https://github.com/HypeMonk/roe-skill
Skill name: `roe-skill`

## Outcome

Install the complete skill into the **current agent's user-level skill directory**,
verify its files, and make it usable in the current conversation where the host
supports that. Do the installation work yourself. Do not send the student a Python
command, ask them to create folders, request an exam email/API key, or require a
workspace path that can be inferred from your own environment.

An explicit project-only request overrides the user-level default. Honor ordinary
tool approval prompts; do not disable sandboxing or permissions to avoid them.

## Procedure

1. **Identify your actual client.** Use the host/runtime context already available.
   Do not ask the student to choose if you know you are Claude Code, Codex or
   Antigravity. Ask one brief question only if the host truly cannot be identified.
2. **Prefer an available native skill installer.** If your host already offers a
   trusted skill-installation tool, use it with this GitHub repository and the
   `roe-skill` name. Do not assume a tool exists merely because another agent has it.
3. **Otherwise fetch and inspect the public repository.** Clone into a new temporary
   directory, preferably with the checkout folder named `roe-skill`, or download
   its source into a new isolated folder. Do not run downloaded code or package
   hooks just to copy instruction files. Inspect `SKILL.md`, references and the
   file inventory; the root skill is discoverable directly from `SKILL.md`.
4. **Choose the correct destination.** Use the current client's documented path:

   | Client | User-level default | Project-only alternative |
   |---|---|---|
   | Claude Code | `~/.claude/skills/roe-skill/` | `<workspace>/.claude/skills/roe-skill/` |
   | Codex | `~/.agents/skills/roe-skill/` | `<workspace>/.agents/skills/roe-skill/` |
   | Current Antigravity | `~/.gemini/config/skills/roe-skill/` | `<workspace>/.agents/skills/roe-skill/` |

   Resolve `~` in the **agent's actual environment**. Older Antigravity builds may
   require their documented legacy path; confirm that from the installed client
   instead of guessing. Do not install into every platform when only one is in use.
5. **Preserve any existing installation.** If the destination is absent, create it
   and copy the full skill content. If it is identical, report already installed.
   If it differs, inspect it and obtain approval before replacing it; preserve a
   backup of the specific old skill. Never merge an unknown custom version silently.
6. **Copy only distribution content.** Required: `SKILL.md` and `references/`.
   Include `scripts/`, `evals/`, `README.md` and `INSTALL.md` as supporting content.
   Never copy `.git/`, caches, credentials, dependency folders or local settings.
   The bundled Python installer is optional, not a requirement for the student;
   run it only after reviewing it if it materially helps the agent.
7. **Verify and activate.** Check `name: roe-skill`, all referenced files and a
   complete copy. Rescan skills using an available host mechanism. Claude Code can
   reload skills; Codex normally discovers changes; Antigravity may need a workspace
   refresh depending on build. If dynamic registration is unavailable, explicitly
   read the installed `SKILL.md` and apply its permitted instructions in this
   conversation, while stating that native discovery still needs a refresh.
8. **Give one concise completion message.** Report the actual installed path and
   invocation. Do not claim native registration or model behavior was verified
   unless you observed it.

## Standard Skills CLI alternative

If Node/npm is available and using the standard installer is appropriate, the
published Skills CLI supports this repository. Select **your current client**:

```sh
npx skills add https://github.com/HypeMonk/roe-skill --skill roe-skill -g -a claude-code -y --copy
```

Replace `claude-code` with `codex` or `antigravity` when that is your client. The
flags select the single skill, user-level installation and ordinary file copying.
Do not use `--agent '*'` or install all clients unnecessarily. Review installer
behavior and follow the host's approval requirements for downloaded code.

The Skills CLI is optional. If it is unavailable, copy the inspected files directly
instead of making the student install another toolchain.

## Stop conditions

Stop before modifying anything when the destination or intended client is unknown,
the repository cannot be read, an existing custom skill needs replacement approval,
or host policy denies the action. Explain that exact blocker; do not fabricate a
successful install or route around a denied tool.

No exam submission, paid call, browser account access, deployment, API key, security
setting change or unrelated repository edit is part of installing roe-skill.
