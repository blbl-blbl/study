# greeting.py

import sys

try:
    name = sys.argv[1]
    age = sys.argv[2]
except IndexError:
    sys.exit("Не все параметры указаны")

try:
    age = int(age)
except ValueError:
    sys.exit("Возраст должен быть целым числом")

print(f"Привет, {name}! Тебе {age} лет.")