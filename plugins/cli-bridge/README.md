# CLI Bridge Plugin for DeepSeek Harness (DSH)

Cross-agent CLI execution and delegation bridge that enables DeepSeek Harness to delegate coding, refactoring, and command-line tasks directly to your installed local agents:

- **Cursor Agent** (`cursor-agent`)
- **OpenAI Codex CLI** (`codex exec`)
- **Google Antigravity CLI** (`agy -p`)
- **OpenCode CLI** (`opencode run`)
- **Moonshot Kimi CLI** (`kimi -p`)

## Exposed Tools

- `cli_bridge(client, prompt, model, workspace)`: General delegation dispatcher.
- `run_cursor(prompt, model)`: Dedicated Cursor agent runner.
- `run_codex(prompt, model)`: Dedicated Codex CLI runner.
- `run_antigravity(prompt, model)`: Dedicated Antigravity CLI runner.
- `run_opencode(prompt, model)`: Dedicated OpenCode CLI runner.
- `run_kimi(prompt, model)`: Dedicated Kimi CLI runner.
- `list_available_clients()`: Diagnoses path and availability for all 5 engines.

## Usage from Terminal

```bash
# Check status of local engines
py bridge.py status

# Run a task through Codex
py bridge.py run codex "Write a unit test for user authentication"

# Run a task through Antigravity
py bridge.py run antigravity "Analyze project architecture"

# Run a task through Cursor
py bridge.py run cursor "Refactor main.ts"
```
