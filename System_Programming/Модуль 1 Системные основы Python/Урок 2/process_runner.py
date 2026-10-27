# process_runner.py

import sys
import subprocess


def run_process(
        argv: list[str],
        timeout_s: float
) -> dict:

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



# 1. Успешное выполнение
print(run_process(
    [sys.executable, "-c", "print('Hello')"],
    5
))

# 2. Завершение с ошибкой
print(run_process(
    [sys.executable, "-c", "import sys; sys.exit(7)"],
    5
))

# 3. Превышение времени
print(run_process(
    [sys.executable, "-c", "import time; time.sleep(3)"],
    0.5
))

# 4. Несуществующая программа
print(run_process(
    ["nonexistent_command_xyz_123"],
    5
))