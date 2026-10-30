import sys
import subprocess


def execute_and_report(
        argv: list[str],
        timeout_s: float
) -> None:

    try:
        result = run_process(argv, timeout_s)
    except ValueError as e:
        print("Ошибка аргументов:", e)
    else:
        print(f"Статус: {result['status']}")
    finally:
        print("Попытка выполнения завершена")


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


# Некорректные аргументы
execute_and_report([], 5)

# Успешное выполнение
execute_and_report(
    [sys.executable, "-c", "print('Hello')"],
    5
)

# Неуспешное выполнение команды
execute_and_report(
    [sys.executable, "-c", "import sys; sys.exit(7)"],
    5
)