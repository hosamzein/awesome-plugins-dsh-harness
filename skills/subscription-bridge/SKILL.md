---
name: subscription-bridge
description: >
  Direct subscription-authorized models for DeepSeek Harness (Cursor, Codex, Antigravity, Claude, Kimi).
  Zero API keys required.
metadata:
  target: deepseek-harness
  version: "1.0.0"
---

# DeepSeek Harness Subscription Bridge

Enables DeepSeek Harness to query models across your active subscriptions:
- **Cursor** (`cursor/composer-2.5`)
- **OpenAI Codex** (`codex/default`, `codex/o3`, `codex/gpt-4o`)
- **Google Antigravity** (`antigravity/gemini-3.8-flash`, `antigravity/gemini-3.8-pro`)
- **Anthropic Claude** (`claude/claude-sonnet-5`, `claude/claude-opus-4.8`)
- **Moonshot Kimi** (`kimi/kimi-code`)

Endpoint: `http://127.0.0.1:5288/v1`
