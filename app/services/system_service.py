import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _run_safe_command(command: list[str]) -> dict[str, object]:
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as exc:
        return {
            "command": command,
            "ok": False,
            "error": str(exc),
        }

    result: dict[str, object] = {
        "command": command,
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }

    if completed.returncode != 0:
        result["error"] = "Command failed"

    return result


def get_current_user() -> dict[str, object]:
    return _run_safe_command(["whoami"])


def get_uptime() -> dict[str, object]:
    return _run_safe_command(["uptime"])


def get_disk_usage() -> dict[str, object]:
    return _run_safe_command(["df", "-h"])


def list_project_files() -> dict[str, object]:
    try:
        entries = sorted(path.name for path in PROJECT_ROOT.iterdir())
    except OSError as exc:
        return {
            "ok": False,
            "project_root": str(PROJECT_ROOT),
            "error": str(exc),
        }

    return {
        "ok": True,
        "project_root": str(PROJECT_ROOT),
        "files": entries,
    }


def get_python_version() -> dict[str, object]:
    result = _run_safe_command(["python3", "--version"])
    result["runtime"] = sys.version
    return result
