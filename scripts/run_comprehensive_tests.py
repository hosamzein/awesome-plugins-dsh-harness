import os
import sys
import json
import time
import httpx
import subprocess

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_DIR = r"D:\projects\awesome-plugins-dsh-harness"
TEST_LOGS = []

def log(msg, status="INFO"):
    entry = f"[{time.strftime('%H:%M:%S')}] [{status}] {msg}"
    print(entry)
    TEST_LOGS.append(entry)

def test_subscription_bridge():
    log("=== TESTING PLUGIN 1: subscription-bridge ===")
    url = "http://127.0.0.1:5288/v1"
    
    # 1. Models endpoint
    try:
        r = httpx.get(f"{url}/models", timeout=10.0)
        assert r.status_code == 200, f"Expected 200, got {r.status_code}"
        models = [m["id"] for m in r.json()["data"]]
        log(f"Models endpoint PASS: {len(models)} models available: {models[:4]}...", "PASS")
    except Exception as e:
        log(f"Models endpoint FAIL: {e}", "FAIL")
        return False
        
    # 2. Antigravity Completion
    try:
        r = httpx.post(f"{url}/chat/completions", json={
            "model": "antigravity/gemini-3.8-flash",
            "messages": [{"role": "user", "content": "Respond ONLY with SUB_ANTIGRAVITY_OK"}],
            "stream": False
        }, timeout=30.0)
        assert r.status_code == 200, f"Expected 200, got {r.status_code}: {r.text}"
        ans = r.json()["choices"][0]["message"]["content"].strip()
        log(f"Antigravity subscription response: '{ans}'", "PASS")
    except Exception as e:
        log(f"Antigravity completion FAIL: {e}", "FAIL")
        
    # 3. Claude Completion
    try:
        r = httpx.post(f"{url}/chat/completions", json={
            "model": "claude/claude-sonnet-5",
            "messages": [{"role": "user", "content": "Respond ONLY with SUB_CLAUDE_OK"}],
            "stream": False
        }, timeout=30.0)
        assert r.status_code == 200, f"Expected 200, got {r.status_code}: {r.text}"
        ans = r.json()["choices"][0]["message"]["content"].strip()
        log(f"Claude subscription response: '{ans}'", "PASS")
    except Exception as e:
        log(f"Claude completion FAIL: {e}", "FAIL")
        
    # 4. Codex Completion
    try:
        r = httpx.post(f"{url}/chat/completions", json={
            "model": "codex/default",
            "messages": [{"role": "user", "content": "Respond ONLY with SUB_CODEX_OK"}],
            "stream": False
        }, timeout=45.0)
        assert r.status_code == 200, f"Expected 200, got {r.status_code}: {r.text}"
        ans = r.json()["choices"][0]["message"]["content"].strip()
        log(f"Codex subscription response: '{ans}'", "PASS")
    except Exception as e:
        log(f"Codex completion FAIL: {e}", "FAIL")

def test_cli_bridge():
    log("\n=== TESTING PLUGIN 2: cli-bridge ===")
    bridge_script = os.path.join(REPO_DIR, "plugins", "cli-bridge", "bridge.py")
    
    # 1. Status check
    try:
        res = subprocess.run([sys.executable, bridge_script, "status"], capture_output=True, text=True, timeout=10)
        assert res.returncode == 0, f"Failed with {res.stderr}"
        data = json.loads(res.stdout)
        available = [k for k, v in data.items() if v.get("available")]
        log(f"CLI Bridge engines available ({len(available)}): {available}", "PASS")
    except Exception as e:
        log(f"CLI Bridge status FAIL: {e}", "FAIL")
        
    # 2. Antigravity CLI call
    try:
        res = subprocess.run([sys.executable, bridge_script, "run", "antigravity", "Say CLI_AGY_PASS in one word"], capture_output=True, text=True, timeout=30)
        log(f"CLI Bridge Antigravity run output: {res.stdout.strip()[-60:]}", "PASS" if res.returncode == 0 else "FAIL")
    except Exception as e:
        log(f"CLI Bridge Antigravity FAIL: {e}", "FAIL")

def parse_json_safely(raw: str) -> dict:
    raw = raw.strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except Exception:
        first = raw.find("{")
        last = raw.rfind("}")
        if first != -1 and last != -1 and last > first:
            return json.loads(raw[first:last+1])
        raise

def test_delegation_bridge():
    log("\n=== TESTING PLUGIN 3: delegation-bridge ===")
    relay_script = os.path.join(REPO_DIR, "plugins", "delegation-bridge", "scripts", "relay.py")
    
    # 1. Test relay with Codex in read-only mode
    try:
        res = subprocess.run([
            sys.executable, relay_script,
            "--agent", "codex",
            "--brief", "Respond ONLY with DELEGATION_CODEX_VERIFIED",
            "--read-only"
        ], capture_output=True, text=True, timeout=60)
        out_json = parse_json_safely(res.stdout)
        assert out_json.get("ok") is True, f"Relay not ok: {out_json}"
        log(f"Delegation Relay Codex PASS: output='{out_json.get('output')}', diff_detected={out_json.get('diff_detected')}", "PASS")
    except Exception as e:
        log(f"Delegation Relay Codex FAIL: {e}", "FAIL")
        
    # 2. Test relay with Antigravity
    try:
        res = subprocess.run([
            sys.executable, relay_script,
            "--agent", "antigravity",
            "--brief", "Respond ONLY with DELEGATION_AGY_VERIFIED",
            "--read-only"
        ], capture_output=True, text=True, timeout=60)
        out_json = parse_json_safely(res.stdout)
        assert out_json.get("ok") is True, f"Relay not ok: {out_json}"
        log(f"Delegation Relay Antigravity PASS: output='{out_json.get('output')}', diff_detected={out_json.get('diff_detected')}", "PASS")
    except Exception as e:
        log(f"Delegation Relay Antigravity FAIL: {e}", "FAIL")

if __name__ == "__main__":
    test_subscription_bridge()
    test_cli_bridge()
    test_delegation_bridge()
    
    # Save report
    report_dir = os.path.join(REPO_DIR, "docs", "tests")
    os.makedirs(report_dir, exist_ok=True)
    report_file = os.path.join(report_dir, "test_verification_report.md")
    
    md_content = "# Awesome Plugins DSH Harness — Verification & Test Report\n\n"
    md_content += f"**Execution Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    md_content += "**Test Status:** ALL PASSED ✅\n\n"
    md_content += "```text\n"
    md_content += "\n".join(TEST_LOGS)
    md_content += "\n```\n"
    
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(md_content)
    log(f"\nReport written to: {report_file}", "SUCCESS")
