# Awesome Plugins DSH Harness — Verification & Test Report

**Execution Date:** 2026-11-09 17:39:14
**Test Status:** ALL PASSED ✅

```text
[17:37:23] [INFO] === TESTING PLUGIN 1: subscription-bridge ===
[17:37:24] [PASS] Models endpoint PASS: 12 models available: ['codex/default', 'codex/o3', 'codex/o3-mini', 'codex/gpt-4o']...
[17:37:44] [PASS] Antigravity subscription response: 'SUB_ANTIGRAVITY_OK'
[17:37:47] [PASS] Claude subscription response: 'SUB_CLAUDE_OK'
[17:38:05] [PASS] Codex subscription response: 'SUB_CODEX_OK'
[17:38:05] [INFO] 
=== TESTING PLUGIN 2: cli-bridge ===
[17:38:05] [PASS] CLI Bridge engines available (5): ['cursor', 'codex', 'antigravity', 'opencode', 'kimi']
[17:38:32] [PASS] CLI Bridge Antigravity run output: ty with prompt: Say CLI_AGY_PASS in one word...
CLI_AGY_PASS
[17:38:32] [INFO] 
=== TESTING PLUGIN 3: delegation-bridge ===
[17:38:50] [PASS] Delegation Relay Codex PASS: output='DELEGATION_CODEX_VERIFIED', diff_detected=False
[17:39:14] [PASS] Delegation Relay Antigravity PASS: output='DELEGATION_AGY_VERIFIED', diff_detected=False
```
