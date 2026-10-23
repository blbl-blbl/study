# child.py

import sys

print("Начинаю работу")
print("Произошла ошибка", file=sys.stderr)

sys.exit(7)