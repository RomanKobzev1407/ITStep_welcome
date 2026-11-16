# Завдання 1

'''name = input("Введіть своє ім'я: ")
while True:
    age = int(input("Введіть свій вік: "))

    if age > 0:
        break

print(f"Привіт, {name}. Тобі {age} років.")'''

# Завдання 2

'''goal = float(input("Цільова сума? "))
total = 0
while total < goal:

    daily_amount = float(input("Сьогоднішній вклад? "))
    total += daily_amount

print(f"Мету досягнуто! У скарбничці {total} грн.")'''

# Завдання 3

'''while True:
    meters = float(input("Введіть довжину в метрах: "))

    yards = meters / 0.9144
    foot = meters / 0.3048

    print(f"{meters} м = {yards:.4f} ярдів")
    print(f"{meters} м = {foot:.4f} футів")

    answer = input("Продовжувати програму? (так/ні): ")
    if not answer == "так":
        print("Робота зупинено.")
        break'''

# Завдання 4

'''goal = float(input("Цільова сума? "))
total = 0
days = 0
while total < goal:

    daily_amount = float(input("Сьогоднішній вклад? "))
    total += daily_amount
    days += 1

print(f"Мету досягнуто за {days} днів! У скарбничці {total} грн.")'''

# Завдання 5

'''total_items = 0
print("Додайте товари. Для завершення введіть \"stop\".")
while True:
    item = input("Введіть товар: ")
    if item == "stop":
        break
        print("Підрахунок завершений")

    total_items += 1
print(f"Всього товарів додано: {total_items}")'''

# Завдання 6

secret_password = "Secret123456"
user_try = 0
while user_try < 3:
    user_password = input("Введіть пароль: ")

    if user_password == secret_password:
        print("Пароль правильний. Доступ дозволено.")
        break
    else:
        print("Пароль неправильний.")
        user_try += 1

if user_try == 3:
    print("Кількість спроб досягла ліміту. Доступ заборонено.")