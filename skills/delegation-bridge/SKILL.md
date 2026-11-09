---
name: delegation-bridge
description: >
  Review-First task delegation across Cursor, Codex, Antigravity, OpenCode, and Kimi.
  Follows the 5-step lifecycle: write brief, dispatch relay, capture diffs, review changes, and land code.
  Inspired by amElnagdy/delegate-skills. Use whenever you want an implementer agent to do the typing in isolation
  while DeepSeek Harness reviews and commits the result.
metadata:
  version: "1.0.0"
---

# Delegation Bridge Skill

You are the **orchestrator** in DeepSeek Harness. This skill enables you to delegate bounded coding or diagnostic tasks to separate **implementer** agents (`cursor`, `codex`, `antigravity`, `opencode`, `kimi`), inspect what they changed via `git diff`, and land the code yourself.

## The 5-Step Loop

### 1. Write the Brief
The implementer agent sees only the text you provide. State:
- The exact objective.
- Files to modify vs. files to leave untouched.
- Test commands to verify before declaring completion.
- Instruct the implementer **not to commit** (you will review and commit).

### 2. Dispatch
Invoke the relay runner:
```bash
py "C:\Users\Ebda\.dsh\plugins\delegation-bridge\scripts\relay.py" --agent <cursor|codex|antigravity|opencode|kimi> --brief "<brief text>" --cd /path/to/repo
```
Options:
- `--read-only`: For code review, audits, or diagnosis with zero file edits.
- `--model <model>`: Specify model override.
- `--session <id>`: Continue an existing agent thread.

### 3. Review Diffs
Check the generated `result.json` and review the diff:
```bash
git diff --stat
git diff
```

### 4. Land Code
Once verified, commit the changes:
```bash
git add .
git commit -m "feat(module): description of landed change"
```
