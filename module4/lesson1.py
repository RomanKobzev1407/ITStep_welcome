# Завдання 1
"""# Вводимо кількість печива
cookies = int(input("Введіть кількість печива: "))
# Виводимо текст
print("Вміст кошика:")
# Починаємо цикл
for cookie in range(cookies):
    # виводимо емоджи
    print("🍪", end="")"""


# Завдання 2

"""clients = int(input("Введіть кількість клієнтів: "))
print("Рахунки: ")
for i in range(1001, 1001+clients):
    print(f"INV-{i:.0f}")"""

# Завдання 3

"""days = int(input("Раз на скільки днів тренуватися: "))
for i in range(1, 30, days):
    print(f"День тренування: {i:.0f}")"""

# Завдання 4
"""# Вводимо кількість печива
products = int(input("Введіть кількість: "))
type = input("Введіть тип товару: ")
# Виводимо текст
print("Вміст кошика:")
# Починаємо цикл
for i in range(products):
    if type == "печиво":
        # виводимо емоджи
        print("🍪", end="")
    elif type == "капкейк":
        print("🧁", end="")
    elif type == "яблуко":
        print("🍏", end="")
    elif type == "груша":
        print("🍐", end="")
    elif type == "виноград":
        print("🍇", end="")
    elif type == "вишня":
        print("🍒", end="")
    else:
        print("Такого товару немає")
        break"""

# Завдання 5
"""print("Починаю зворотній відлік")
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("Запуск!!!")"""

# Завдання 6

"""num = int(input("Введіть число: "))
for i in range(1, 11):
    result = i * num
    print(f"{i} * {num} = {result}")"""

# Завдання 7
sum_money = float(input("Введіть суму вкладу: "))
percent = float(input("Введіть відсоток: "))
for year in range(1, 6):
    sum_money = sum_money * (1 + percent / 100)
    print(f"Сума вкладу після {year}-го року: {sum_money:.2f}")
