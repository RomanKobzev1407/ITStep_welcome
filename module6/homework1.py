# Завдання 1
text = input("Введіть рядок англійською мовою: ")

count = 0
for letter in text:
    if (
        "a" in letter
        or "e" in letter
        or "i" in letter
        or "o" in letter
        or "u" in letter
    ):
        count += 1

print(f"Кількість голосних літер: {count}")
