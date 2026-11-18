# Завдання 1
"""time_minutes = int(input("Введіть час у хвилинах: "))
if time_minutes >= 0:
    time_seconds = time_minutes * 60
    print(f"Це дорівнює {time_seconds:.0f} секунд.")
else:
    print("Час має бути додатнім.")"""

# Завдання 2
"""password = input("Введіть пароль: ")
secret_password = "OpenSesame123"
if password == secret_password:
    print("Доступ дозволено")
else:
    print("Доступ заблоковано")"""

# Завдання 3
"""length_meter = float(input("Введіть довжину в метрах: "))
suggest = input("Введіть бажану розмірність (см або км): ")
if suggest == "см":
    length_sm = length_meter * 100
    print(f"Довжина в см: {length_sm:.0f}")
elif suggest == "км":
    length_km = length_meter / 1000
    print(f"Довжина в км: {length_km:.3f}")
else:
    print("Неправильна розмірність.")"""

# Завдання 4
"""# Вводимо варіант відповіді.
answer = input("Відповідь на Велике Питання Життя, Всесвіту і Всього Іншого: ")
# Якщо відповідь цифрами
if answer == "42":
    print("Правильно")
# Якщо відповідь словами
elif answer == "сорок два":
    print("Правильно")
# Якщо відповідь словами та дефісом
elif answer == "сорок-два":
    print("Правильно")
# Зайвий блок. Ця умова перевірялося в операторі if
# elif answer == "42":
#    print("Правильно")
# Якщо жодна мова не виконана
else:
    print("Не правильно")"""

# Завдання 5
"""grade = int(input("Введіть оцінку: "))
if grade == 2:
    print("Незадовільно")
elif grade == 3:
    print("Задовільно")
elif grade == 4:
    print("Добре")
elif grade == 5:
    print("Відмінно")
else:
    print("Оцінка має бути від 2 до 5")"""

# Завдання 6
price_pizza = float(input("Введіть ціну піци: "))
count_pizza = int(input("Введіть кількість піц: "))
budget = float(input("Введіть бюджет: "))
need_money = price_pizza * count_pizza
delta = budget - need_money
if delta > 0:
    print(f"Грошей вистачає. Залишиться {delta} грн")
elif delta == 0:
    print("Грошей вистачає. Залишок 0 грн")
else:
    print(f"Грошей не вистачає. Ще потрібно {-delta} грн")

# https://copilot.cloud.microsoft/chat/share/eyJzaGFyZUlkIjoiZjNmNTE3ZDItNDQ2Zi00NDdiLTg4ODktNjExNTEzODM5ZTVmIiwiY29udmVyc2F0aW9uSWQiOiIwNGJlMjg5Yi0yYTZlLTQ0OGItOGI4ZS1mYWNkODFkNTgwOTMifQ%3D%3D
