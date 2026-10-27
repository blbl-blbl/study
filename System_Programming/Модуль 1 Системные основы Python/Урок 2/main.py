# main

import subprocess
import sys

try:
    result = subprocess.run(
        [sys.executable, "child.py"],
        capture_output=True,
        text=True,
        timeout=1,
        check=True
    )

    print("Успех:", result.stdout)

except subprocess.CalledProcessError:
    print("Ошибка выполнения команды")

except subprocess.TimeoutExpired:
    print("Превышено время ожидания")

print("Работа main.py завершена")
