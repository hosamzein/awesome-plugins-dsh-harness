# Subscription Bridge Plugin for DeepSeek Harness (DSH)

Direct zero-API-key model provider bridge connecting DeepSeek Harness to your existing paid subscriptions across **OpenAI ChatGPT Plus/Pro (Codex)**, **Google Antigravity (Gemini)**, **Anthropic Claude**, **Cursor**, and **Moonshot Kimi**.

## Features

- **Zero API Tokens**: Dispatches requests through your active authenticated sessions on your host.
- **OpenAI-Compatible Gateway**: Serves an async FastAPI `/v1/chat/completions` and `/v1/models` daemon on `127.0.0.1:5288`.
- **Full Streaming Support**: SSE event stream streaming responses token-by-token directly to DeepSeek Harness UI.
- **Cordis Profile Injection**: Integrated directly into `~/.dsh/profiles/desktop/cordis.patch.yml`.

## Available Models

- `codex/default`, `codex/o3`, `codex/o3-mini`, `codex/gpt-4o`, `codex/gpt-5`
- `antigravity/gemini-3.8-flash`, `antigravity/gemini-3.8-pro`
- `claude/claude-sonnet-5`, `claude/claude-opus-4.8`
- `cursor/composer-2.5`
- `kimi/kimi-code`

## Quick Start

```powershell
# Start the Gateway
pwsh .\start-gateway.ps1

# Stop the Gateway
pwsh .\stop-gateway.ps1
```
