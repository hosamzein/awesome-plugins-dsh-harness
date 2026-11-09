"""
DeepSeek Harness Tool Definitions for CLI Bridge
Allows DeepSeek Harness to delegate tasks directly to Cursor, Codex, Antigravity, OpenCode, and Kimi.
"""

from bridge import run_client, check_status

def cli_bridge(client: str, prompt: str, model: str = None, workspace: str = None) -> str:
    """Delegate execution to a specific local CLI coding agent (cursor, codex, antigravity, opencode, kimi)."""
    return run_client(client=client, prompt=prompt, model=model, workspace=workspace)

def run_cursor(prompt: str, model: str = None) -> str:
    """Run a prompt through the local Cursor Agent CLI."""
    return run_client(client="cursor", prompt=prompt, model=model)

def run_codex(prompt: str, model: str = None) -> str:
    """Run a prompt through the local OpenAI Codex CLI."""
    return run_client(client="codex", prompt=prompt, model=model)

def run_antigravity(prompt: str, model: str = None) -> str:
    """Run a prompt through the local Google Antigravity CLI."""
    return run_client(client="antigravity", prompt=prompt, model=model)

def run_opencode(prompt: str, model: str = None) -> str:
    """Run a prompt through the local OpenCode CLI."""
    return run_client(client="opencode", prompt=prompt, model=model)

def run_kimi(prompt: str, model: str = None) -> str:
    """Run a prompt through the local Kimi CLI."""
    return run_client(client="kimi", prompt=prompt, model=model)

def list_available_clients() -> dict:
    """List the detected local coding CLI clients and their availability status."""
    return check_status()
