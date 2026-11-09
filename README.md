# Awesome Plugins for DeepSeek Harness (DSH) 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DeepSeek Harness](https://img.shields.io/badge/Runtime-DeepSeek%20Harness%20(DSH)-blue)](https://github.com/deepseek-ai/deepseek-harness)
[![Multi-Engine Bridge](https://img.shields.io/badge/Engines-Cursor%20%7C%20Codex%20%7C%20Antigravity%20%7C%20OpenCode%20%7C%20Claude%20%7C%20Kimi-purple)](#)
[![Zero API Keys](https://img.shields.io/badge/Billing-100%25%20Zero%20Metered%20API%20Keys-brightgreen)](#)
[![Author: Dr. Eng. Hossam Zein](https://img.shields.io/badge/Author-Dr.%20Eng.%20Hossam%20Zein-orange)](https://github.com/hosamzein)

> **Modular, extensible plugin & bridge ecosystem for DeepSeek Harness (DSH). Supercharges your harness with zero-API-key subscription authorization, instant CLI tool execution, and Review-First cross-agent delegation across Cursor, Codex, Google Antigravity, OpenCode, and Kimi.**

---

## 📑 Table of Contents
1. [The Vision & Core Economics](#-the-vision--core-economics)
2. [Architecture Topology & Operational Flows](#-architecture-topology--operational-flows)
3. [The Three Included Plugins](#-the-three-included-plugins)
   - [1. Subscription Bridge (Zero-API-Key Models)](#1-subscription-bridge-plugin)
   - [2. CLI Bridge (Direct CLI Execution)](#2-cli-bridge-plugin)
   - [3. Delegation Bridge (Review-First Delegation & Landing)](#3-delegation-bridge-plugin)
4. [Full Control & Interface How-To Guide](#-full-control--interface-how-to-guide)
5. [Extensibility Guide](#-extensibility-guide-adding-new-plugins)
6. [Installation & Setup](#-installation--setup)
7. [License](#-license)

---

## 🎯 The Vision & Core Economics

<p align="center">
  <img src="docs/diagrams/cost_economics.svg" alt="Cost Comparison" width="850"/>
</p>

```
┌────────────────────────────────────────────────────────────────────────┐
│                   TOTAL MONTHLY AI TOOLING EXPENDITURE                 │
├────────────────────────────────────────────────────────────────────────┤
│ Traditional Metered API:                                               │
│ [Subscriptions: $80/mo] + [Metered API Keys: $450/mo]  ──> [$530/mo]   │
├────────────────────────────────────────────────────────────────────────┤
│ Awesome Plugins DSH Bridge:                                            │
│ [Subscriptions: $80/mo] + [Incremental API Token: $0]  ──> [85% SAVED] │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Financial Arbitrage (Subscriptions vs. Metered API):** Complex coding agent loops burn 500k–2M tokens daily. Under raw API rates ($15–$75 per million tokens), monthly charges easily hit $400–$900+. By dispatching requests to your active paid subscriptions (Cursor Pro, ChatGPT Plus/Pro, Google Antigravity, Kimi VIP), incremental token cost drops to **$0.00**.
2. **Review-First Guardrails:** Inspired by [`amElnagdy/delegate-skills`](https://github.com/amElnagdy/delegate-skills), code is never blindly trusted. Tasks are dispatched to isolated implementer sandboxes, diffs are inspected via `git diff`, and you retain final landing authority.

---

## 📐 Architecture Topology & Operational Flows

### 2.1 Technical Architecture Diagram

The high-resolution SVG diagram below illustrates the end-to-end integration topology between the DeepSeek Harness runtime, our 3 bridge plugins, host subscription sessions, and underlying coding CLI engines:

<p align="center">
  <img src="docs/diagrams/architecture_topology.svg" alt="Architecture Topology" width="900"/>
</p>

#### Interactive Component Flowchart

```mermaid
flowchart TD
    subgraph ClientLayer["🖥️ User & Orchestration Layer"]
        User["Developer / Engineer"]
        DSH["DeepSeek Harness (DSH Runtime)"]
        CordisProfile["Cordis Desktop Profile<br/>(~/.dsh/profiles/desktop/cordis.patch.yml)"]
        DSHSkills["DSH Skills Watcher<br/>(~/.dsh/skills/ & ~/.agents/skills/)"]
    end

    subgraph PluginsLayer["⚡ Awesome DSH Plugins"]
        P1["Plugin 1: subscription-bridge<br/>(OpenAI-Compatible Gateway :5288)"]
        P2["Plugin 2: cli-bridge<br/>(Instant Subprocess CLI Runner)"]
        P3["Plugin 3: delegation-bridge<br/>(Review-First Delegation & Landing)"]
    end

    subgraph AuthSessionLayer["🔑 Host Subscription Auth (100% Zero-API-Key)"]
        S_Codex["OpenAI Codex Session (~/.codex)"]
        S_AGY["Antigravity Subscription (~/.gemini)"]
        S_Claude["Claude Pro Session (~/.claude)"]
        S_Kimi["Kimi VIP Session (~/.kimi-code)"]
        S_Cursor["Cursor Pro License"]
    end

    subgraph EngineLayer["🤖 Target Local Coding Agents"]
        E_Cursor["Cursor Agent (cursor-agent.cmd)"]
        E_Codex["OpenAI Codex CLI (codex.cmd)"]
        E_AGY["Google Antigravity (agy.exe)"]
        E_OpenCode["OpenCode CLI (opencode.cmd)"]
        E_Kimi["Moonshot Kimi (kimi.exe)"]
    end

    subgraph WorkspaceLayer["📁 Local Codebase & Review Guard"]
        GitDiff["Git Diff & Worktree Tracker"]
        ReviewGate["Review-First Inspection Gate"]
        LocalRepo["Production Git Workspace"]
    end

    %% Connections
    User -->|Prompts & Tasks| DSH
    DSH --- CordisProfile
    DSH --- DSHSkills
    
    CordisProfile -->|Provider: subscription-bridge| P1
    DSHSkills -->|Tools: run_cursor, run_codex...| P2
    DSHSkills -->|Tools: delegate_task, review_task...| P3

    P1 -->|Chat & Completions SSE| AuthSessionLayer
    AuthSessionLayer -->|Zero-Token Execution| EngineLayer

    P2 -->|Synchronous Run| EngineLayer
    P3 -->|Dispatch Relay Brief| EngineLayer

    EngineLayer -->|Uncommitted Changes| WorkspaceLayer
    WorkspaceLayer -->|Capture Diff & JSON| ReviewGate
    ReviewGate -->|Approved Only| LocalRepo
```

---

### 2.2 Operational Process Diagram: Review-First Delegation Lifecycle

The dual-path operational flow diagram contrasts standard model queries with task delegation:

<p align="center">
  <img src="docs/diagrams/operational_workflow.svg" alt="Operational Workflow" width="900"/>
</p>

#### Sequence 1: The 5-Step Review-First Delegation Lifecycle

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Developer / User
    participant DSH as DeepSeek Harness
    participant DB as Delegation Bridge (Plugin 3)
    participant Engine as Target Agent (Codex/Cursor/AGY)
    participant Git as Git Workspace Engine
    participant Rev as Review Gate

    Dev->>DSH: Prompt: "Refactor auth logic with Codex"
    DSH->>DB: delegate_task(agent="codex", brief="...")
    
    rect rgb(28, 38, 56)
        note over DB,Git: 1. Snapshot Pre-State
        DB->>Git: git diff --stat (Snapshot before changes)
    end

    rect rgb(35, 45, 65)
        note over DB,Engine: 2. Relay Dispatch (Isolated/Ephemeral)
        DB->>Engine: Run with --ephemeral --sandbox / --mode plan
        Engine->>Engine: Generate code & apply modifications
        Engine-->>DB: Process stdout / stderr
    end

    rect rgb(28, 38, 56)
        note over DB,Git: 3. Diff Capture & Isolation
        DB->>Git: git diff (Capture post-execution modifications)
        Git-->>DB: Modified files & hunk patch
        DB->>DB: Generate result.json (ok, diff_summary, run_id)
    end

    rect rgb(45, 35, 60)
        note over DB,Dev: 4. Review-First Validation
        DB-->>DSH: Structured report with diff preview
        DSH-->>Dev: Display diff summary to Developer
        Dev->>Rev: Inspect changes: Accept or Reject?
    end

    alt Developer Approves
        Dev->>DB: land_task(run_id, commit_msg)
        DB->>Git: git add & git commit (Changes landed)
        DB-->>Dev: Landed successfully ✅
    else Developer Rejects
        Dev->>DB: reject_task(run_id)
        DB->>Git: git restore . (Working tree restored clean)
        DB-->>Dev: Changes rolled back cleanly ❌
    end
```

#### Sequence 2: Subscription Bridge Zero-Key Streaming Gateway Flow

```mermaid
sequenceDiagram
    autonumber
    participant DSH as DeepSeek Harness
    participant Gateway as Subscription Bridge (:5288)
    participant HostAuth as Local Subscription Session
    participant Model as AI Model via Subscription

    DSH->>Gateway: POST /v1/chat/completions (model="codex/o3-mini", stream=true)
    Gateway->>HostAuth: Check auth credentials (~/.codex, ~/.gemini, etc.)
    HostAuth-->>Gateway: Active OAuth / Device Session Validated
    Gateway->>Model: Forward prompt using local CLI runner / session
    loop Streaming Response
        Model-->>Gateway: Token chunks
        Gateway-->>DSH: SSE data: {"choices": [{"delta": {"content": "..."}}]}
    end
    Gateway-->>DSH: data: [DONE] (Cost: $0.00 / Zero API Key)
```

---

## 📦 The Three Included Plugins

### 1. Subscription Bridge Plugin
* **Directory:** `plugins/subscription-bridge/`
* **Skill Definition:** `skills/subscription-bridge/SKILL.md`
* **Role:** Local OpenAI-compatible streaming gateway on port `5288` intercepting model calls from DeepSeek Harness and dispatching them to active subscription sessions.
* **Supported Models:**
  - `codex/default`, `codex/o3`, `codex/o3-mini`, `codex/gpt-4o`, `codex/gpt-5`
  - `antigravity/gemini-3.8-flash`, `antigravity/gemini-3.8-pro`
  - `claude/claude-sonnet-5`, `claude/claude-opus-4.8`
  - `cursor/composer-2.5`
  - `kimi/kimi-code`

### 2. CLI Bridge Plugin
* **Directory:** `plugins/cli-bridge/`
* **Skill Definition:** `skills/cli-bridge/SKILL.md`
* **Role:** Exposes callable tools within DeepSeek Harness to run immediate instructions through local coding client binaries.
* **Tools:** `cli_bridge`, `run_cursor`, `run_codex`, `run_antigravity`, `run_opencode`, `run_kimi`, `list_available_clients`.

### 3. Delegation Bridge Plugin (Review-First Lifecycle)
* **Directory:** `plugins/delegation-bridge/`
* **Skill Definition:** `skills/delegation-bridge/SKILL.md`
* **Role:** Comprehensive delegation workflow implementing the **Implement $\rightarrow$ Diff $\rightarrow$ Review $\rightarrow$ Land** cycle across all 5 engines.
* **Tools:** `delegate_task`, `review_task`, `land_task`, `list_supported_implementers`.

---

## 🎮 Full Control & Interface How-To Guide

Here is the exact reference on how to control and trigger each plugin across all interfaces:

### Interface A: Controlling the Subscription Bridge Gateway
The Subscription Bridge runs as a background service on `http://127.0.0.1:5288/v1`.

```powershell
# 1. Start the service
pwsh .\plugins\subscription-bridge\start-gateway.ps1

# 2. Query available models
Invoke-RestMethod -Uri "http://127.0.0.1:5288/v1/models"

# 3. Stop the service
pwsh .\plugins\subscription-bridge\stop-gateway.ps1
```

#### Configuring in DeepSeek Harness (`~/.dsh/profiles/desktop/cordis.patch.yml`)
Add under `llm-pi-ai.config.providers`:
```yaml
      subscription-bridge:
        displayName: "Subscription Bridge (Zero-Key)"
        apiKeyEnv: SUB_BRIDGE_TOKEN
        api: openai-completions
        baseURL: http://127.0.0.1:5288/v1
        models:
          - id: codex/default
            name: "Codex: Default"
          - id: codex/o3
            name: "Codex: o3"
          - id: antigravity/gemini-3.8-flash
            name: "Antigravity: Gemini 3.8 Flash"
          - id: cursor/composer-2.5
            name: "Cursor: Composer 2.5"
          - id: kimi/kimi-code
            name: "Kimi: Kimi Code"
```

---

### Interface B: Controlling the CLI Bridge
Use the CLI Bridge for immediate tool calls from DeepSeek Harness or terminal:

```bash
# Check presence and health of all engines on host
py plugins/cli-bridge/bridge.py status

# Direct execution syntax:
py plugins/cli-bridge/bridge.py run codex "Write a Python script to sort JSON keys"
py plugins/cli-bridge/bridge.py run antigravity "Analyze this memory leak log"
py plugins/cli-bridge/bridge.py run cursor "Refactor main.ts"
py plugins/cli-bridge/bridge.py run opencode "Review recent git diff"
py plugins/cli-bridge/bridge.py run kimi "Format markdown tables"
```

---

### Interface C: Controlling the Delegation Bridge (Review-First)
Inspired by [`amElnagdy/delegate-skills`](https://github.com/amElnagdy/delegate-skills), this interface enforces safe, review-gated delegation:

#### Step 1: Dispatch a Delegated Task
```bash
# General Syntax:
py plugins/delegation-bridge/scripts/relay.py \
  --agent <cursor|codex|antigravity|opencode|kimi> \
  --brief "Your complete instructions here" \
  --cd /path/to/repo

# Example: Read-only architecture diagnosis (no disk modifications)
py plugins/delegation-bridge/scripts/relay.py \
  --agent cursor \
  --brief "Audit authentication flow for security gaps" \
  --read-only \
  --cd .
```

#### Step 2: Inspect the Structured Output (`result.json`)
The relay outputs execution telemetry and git status:
```json
{
  "ok": true,
  "run_id": "relay-codex-2244b151",
  "agent": "codex",
  "duration_seconds": 15.41,
  "diff_detected": true,
  "diff_summary": " src/auth.ts | 14 +++++++++++---\n 1 file changed, 11 insertions(+), 3 deletions(-)",
  "workspace": "D:\\projects\\my-app"
}
```

#### Step 3: Review and Land the Code
```bash
# Review exact code diffs
git diff

# Land (commit) verified changes
git add .
git commit -m "feat(auth): land delegated changes from Codex"
```

#### Step 4: Continue an Active Thread
To continue the exact thread or session without losing context:
```bash
py plugins/delegation-bridge/scripts/relay.py \
  --agent codex \
  --brief "Now add comprehensive unit tests for the functions you just created" \
  --session <session-id-from-result> \
  --cd .
```

---

## 🛠️ Extensibility Guide: Adding New Plugins

This repository is designed from the ground up as a **modular monorepo** for continuous extension:

```text
plugins/
└── <your-plugin-name>/
    ├── README.md           # Plugin overview and requirements
    ├── plugin.yaml         # DeepSeek Harness / Cordis manifest
    ├── tools.py            # Custom tool functions exposed to LLM
    └── ...                 # Scripts, gateways, or runtime adapters
skills/
└── <your-plugin-name>/
    └── SKILL.md            # Natural language prompt instructions for DSH agents
```

1. Create a new directory under `plugins/<plugin-name>/`.
2. Provide a `plugin.yaml` manifest detailing provided tools and configuration schemas.
3. Add a corresponding `skills/<plugin-name>/SKILL.md` so DSH LLMs automatically learn when and how to call your tool.
4. Run `pwsh .\scripts\install.ps1` to link your new plugin directly into `~/.dsh/plugins/` and `~/.dsh/skills/`.

---

## 🚀 1-Click Installation

```powershell
git clone https://github.com/hosamzein/awesome-plugins-dsh-harness.git
cd awesome-plugins-dsh-harness

# Install all plugins and skills into ~/.dsh and ~/.agents
pwsh .\scripts\install.ps1

# Run verification diagnostics
pwsh .\scripts\test-all.ps1
```

---

## 🧪 Verification & Test Suite

All three plugins are continuously verified against live host runtimes (Cursor, Codex, Antigravity, OpenCode, Claude, Kimi).

To run the automated end-to-end verification suite:

```bash
python scripts/run_comprehensive_tests.py
```

The suite performs real calls against:
- **`subscription-bridge`**: Models catalog and live completion relays for Antigravity, Claude, and Codex with zero metered API keys.
- **`cli-bridge`**: Engine presence validation (5 engines) and direct non-interactive CLI invocation.
- **`delegation-bridge`**: Universal relay dispatch in Review-First read-only mode with diff tracking and structured JSON artifacts.

View the latest certified test report: **[docs/tests/test_verification_report.md](docs/tests/test_verification_report.md)**.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

Developed & Maintained with passion by **Dr. Eng. Hossam Zein**.  
Contributions, issues, and new plugin ideas are welcome!
