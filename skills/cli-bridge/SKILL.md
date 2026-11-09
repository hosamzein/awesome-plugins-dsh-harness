---
name: cli-bridge
description: >
  Delegate and execute tasks in DeepSeek Harness across local CLI coding clients:
  Cursor, OpenAI Codex, Google Antigravity (AGY), OpenCode, and Kimi.
metadata:
  target: deepseek-harness
  version: "1.0.0"
---

# DeepSeek Harness CLI Bridge

Delegate tasks directly from DeepSeek Harness to any installed coding agent on your host:
- **Cursor** (`cursor-agent`)
- **Codex** (`codex exec`)
- **Antigravity** (`agy -p`)
- **OpenCode** (`opencode run`)
- **Kimi** (`kimi -p`)

## CLI Invocation

Check status:
```bash
py C:\Users\Ebda\.dsh\plugins\cli-bridge\bridge.py status
```

Run instructions on a client:
```bash
# Codex
py C:\Users\Ebda\.dsh\plugins\cli-bridge\bridge.py run codex "Your prompt here"

# Antigravity
py C:\Users\Ebda\.dsh\plugins\cli-bridge\bridge.py run antigravity "Your prompt here"

# Cursor
py C:\Users\Ebda\.dsh\plugins\cli-bridge\bridge.py run cursor "Your prompt here"

# OpenCode
py C:\Users\Ebda\.dsh\plugins\cli-bridge\bridge.py run opencode "Your prompt here"

# Kimi
py C:\Users\Ebda\.dsh\plugins\cli-bridge\bridge.py run kimi "Your prompt here"
```
