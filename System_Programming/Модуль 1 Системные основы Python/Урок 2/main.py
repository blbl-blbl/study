# main

import subprocess
import sys

try:
    result = subprocess.run(
        [sys.executable, "child.py"],
        capture_output=True,
        text=True,
        check=True
    )

    print("Команда выполнена успшено")

except subprocess.CalledProcessError as error:
    print("Ошибка выполнения команды")
    print("Код:", error.returncode)
    print("Сообщение:", error.stderr)


print("Работа main.py завершена")
