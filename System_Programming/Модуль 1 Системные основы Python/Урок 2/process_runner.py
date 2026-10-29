# process_runner.py

import sys
import subprocess


def run_process(
        argv: list[str],
        timeout_s: float
) -> dict:

    if not argv:
        raise ValueError ("Передан пустой список команд")

    if timeout_s <= 0:
        raise ValueError ("Время выполнения команды меньше или равно 0")

    stdout = ""
    stderr = ""

    try:
        result = subprocess.run(
            argv,
            timeout=timeout_s,
            text=True,
            check=False,
            capture_output=True
        )

        returncode = result.returncode
        stdout = result.stdout
        stderr = result.stderr
        status = "success" if returncode == 0 else "failed"

    except subprocess.TimeoutExpired as e:
        status = "timeout"
        returncode = None

    except FileNotFoundError as e:
        status = "not_found"
        stderr = str(e)
        returncode = None


    return  {
        "status": status,
        "returncode": returncode,
        "stdout": stdout,
        "stderr": stderr
    }


# Тест 4
run_process(
    [sys.executable, "-c", "print('Hello')"],
    5
)