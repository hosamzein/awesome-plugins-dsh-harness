"""
Delegation Bridge Tools for DeepSeek Harness (DSH)
Implements Review-First Delegation across Cursor, Codex, Antigravity, OpenCode, and Kimi.
"""

import json
import os
import subprocess
import sys
from typing import Dict, Any, Optional

scripts_dir = os.path.join(os.path.dirname(__file__), "scripts")
if scripts_dir not in sys.path:
    sys.path.append(scripts_dir)

from relay import run_relay, AGENTS

def delegate_task(agent: str, brief: str, cd: str = ".", model: str = None, read_only: bool = False, session: str = None) -> Dict[str, Any]:
    """
    Delegate a coding or analysis task to a specific implementer CLI agent.
    
    Args:
        agent: Target implementer ('cursor', 'codex', 'antigravity', 'opencode', 'kimi').
        brief: Complete self-contained instructions for the implementer.
        cd: Target workspace directory.
        model: Optional model override.
        read_only: If True, executes in diagnosis/plan mode with no file edits.
        session: Optional session ID to continue.
    """
    return run_relay(
        agent=agent,
        brief=brief,
        cd=cd,
        model=model,
        read_only=read_only,
        session=session
    )

def review_task(run_id: str, workspace: str = ".") -> Dict[str, Any]:
    """Inspect the git diff and results produced by a delegated task."""
    try:
        diff = subprocess.run(["git", "diff"], cwd=workspace, capture_output=True, text=True, timeout=10).stdout.strip()
        stat = subprocess.run(["git", "diff", "--stat"], cwd=workspace, capture_output=True, text=True, timeout=10).stdout.strip()
        status = subprocess.run(["git", "status", "-s"], cwd=workspace, capture_output=True, text=True, timeout=10).stdout.strip()
        return {
            "run_id": run_id,
            "has_changes": bool(diff or status),
            "summary_stat": stat,
            "status": status,
            "full_diff": diff
        }
    except Exception as e:
        return {"error": str(e)}

def land_task(workspace: str = ".", commit_message: str = "chore: land delegated task") -> Dict[str, Any]:
    """Stage and land (commit) the verified changes produced by the implementer."""
    try:
        subprocess.run(["git", "add", "."], cwd=workspace, check=True)
        res = subprocess.run(["git", "commit", "-m", commit_message], cwd=workspace, capture_output=True, text=True, check=True)
        return {
            "landed": True,
            "output": res.stdout.strip()
        }
    except Exception as e:
        return {"landed": False, "error": str(e)}

def list_supported_implementers() -> list:
    """Return list of supported implementer agents."""
    return list(AGENTS.keys())
