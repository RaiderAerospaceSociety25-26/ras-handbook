#!/usr/bin/env python3
# File: tools/freeze_batch.py

import json, shlex, subprocess, sys
from pathlib import Path

def ensure_dir(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)

def run_shell(cmd_str: str, dry=False):
    print(">", cmd_str)
    if not dry:
        # shell=True allows the base string to include quotes exactly as you wrote them
        subprocess.run(cmd_str, shell=True, check=True)

def main():
    manifest_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("tools/freeze.json")
    dry_run = "--dry-run" in sys.argv
    data = json.loads(manifest_path.read_text(encoding="utf-8"))

    base = data.get("defaults", {}).get("freeze_base")
    if not base:
        sys.exit("Error: defaults.freeze_base is required in the manifest.")

    tasks = data.get("tasks", [])
    if not tasks:
        sys.exit("Error: no tasks found in the manifest.")

    for i, t in enumerate(tasks, 1):
        cmd = t.get("cmd")
        out = t.get("out")
        if not cmd or not out:
            print(f"[skip {i}] missing cmd or out")
            continue

        outp = Path(out)
        ensure_dir(outp)

        # Compose the full freeze command exactly once per task
        # Base + output + command-to-execute
        full = f'{base} -o {shlex.quote(str(outp))} --execute {shlex.quote(cmd)}'
        run_shell(full, dry=dry_run)

if __name__ == "__main__":
    main()
