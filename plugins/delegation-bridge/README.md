# Delegation Bridge Plugin for DeepSeek Harness (DSH)

Review-First delegation engine inspired by [`amElnagdy/delegate-skills`](https://github.com/amElnagdy/delegate-skills), generalized to support **Cursor**, **OpenAI Codex**, **Google Antigravity**, **OpenCode**, and **Moonshot Kimi**.

## The 5-Step Delegation Lifecycle

```
[1. Write Brief] ──> [2. Relay Dispatch] ──> [3. Capture Diffs] ──> [4. Review & Gate] ──> [5. Land & Commit]
```

1. **Write the Brief**: The orchestrator in DeepSeek Harness writes a self-contained task instruction.
2. **Dispatch Relay**: Dispatches headless execution to the selected implementer.
3. **Capture Diffs**: Tracks filesystem changes and captures `result.json`.
4. **Review**: The orchestrator or human reviews the generated `git diff` before anything is landed.
5. **Land**: Stages and commits the verified changes into the git branch.

## Supported Implementers
- `cursor` (`cursor-agent`)
- `codex` (`codex exec`)
- `antigravity` (`agy -p`)
- `opencode` (`opencode run`)
- `kimi` (`kimi -p`)

## Terminal Usage

```bash
# Delegate a refactoring task to Codex
py scripts/relay.py --agent codex --brief "Refactor auth middleware to use async/await" --cd .

# Run read-only architectural diagnosis in Cursor
py scripts/relay.py --agent cursor --brief "Analyze database indexes for performance leaks" --read-only --cd .

# Continue an existing session
py scripts/relay.py --agent codex --brief "Now add comprehensive unit tests" --session <session-id>
```
