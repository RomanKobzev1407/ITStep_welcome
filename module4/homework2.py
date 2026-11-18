# Завдання 1
"""while True:
grade = int(input("Введіть оцінку: "))

if grade == 1:
    print("Дуже погано")
    break
elif grade == 2:
    print("Погано")
    break
elif grade == 3:
    print("Задовільно")
    break
elif grade == 4:
    print("Добре")
    break
elif grade == 5:
    print("Чудово")
    break"""

# Завдання 2

"""yes_count = 0
no_count = 0

while True:
    answer = input("Чи потрібно будувати більше дитячих садків у вашому місті? ")
    if answer == "стоп":
        break
    elif answer == "так":
        yes_count += 1
    elif answer == "ні":
        no_count += 1
    else:
        print("Помилка. Введіть \"так\", \"ні\" або \"стоп\".")

print("Результат:")
print(f"\"Так\": {yes_count}")
print(f"\"Ні\": {no_count}")

if yes_count > no_count:
    print("Більшість голосів \"так\".")
if yes_count < no_count:
    print("Більшість голосів \"ні\".")
else:
    print("Голосів \"так\" і \"ні\" порівну.")"""

# Завдання 3

while True:
    num = int(input("Введіть число (0 для виходу): "))
    if num == 0:
        print("Вихід з програми.")
        break

print(f"Ви ввели: {num}")
