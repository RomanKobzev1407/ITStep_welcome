# Завдання 1
"""age = int(input("Введіть вік: "))
if age >= 18 and age <= 65:
    print("Працездатний")
else:
    print("Непрацездатний")"""

# Завдання 2
"""password = input("Введіть пароль: ")
login = input("Введіть логін: ")
secret_password = "OpenSesame123"
secret_login = "AliBaba"
if password == secret_password and login == secret_login:
    print("Доступ дозволено")
else:
    print("Доступ заблоковано")"""

# Завдання 3
"""price = float(input("Введіть ціну за одиницю товару: "))
count = int(input("Введіть кількість товару: "))
age = int(input("Введіть вік: "))
total_money = price * count
if age < 18 or age > 65:
    discount_money = total_money * 0.15
else:
    discount_money = 0
total_money -= discount_money
print(f"Ціна за одиницю: {price:.2f}")
print(f"Кількість: {count:.0f}")
print(f"Знижка: {discount_money:.2f}")
print(f"Сума покупки: {total_money:.2f}")"""

# Завдання 4
"""age = 17
has_license = "ні"
accidents = 0

if age >= 18 and has_license == "так" and accidents == 0:
    print("Оренда дозволена")
else:
    print("Оренда заборонена")"""

# Завдання 5
"""price = float(input("Введіть ціну покупки: "))
delivery = 120
if price < 500:
    discount = 0
elif 500 <= price < 1000:
    discount = 0.05 * delivery
elif 1000 <= price < 2000:
    discount = 0.2 * delivery
else:
    discount = delivery
print(f"Знижка на доставку: {discount:.2f}")
delivery -= discount
total_price = price + delivery
print(f"Загальна вартість: {total_price:.2f}")"""

# Завдання 6
credit = float(input("Введіть суму крединту: "))
year = int(input("Введіть термін: "))
if credit <= 10000 and year < 3:
    percent = 8
elif credit <= 10000 and year >= 3:
    percent = 10
elif 10000 < credit < 50000 and year < 3:
    percent = 12
elif 10000 < credit < 50000 and year >= 3:
    percent = 14
else:
    percent = 20

total = credit * ((1 + (percent / 100)) ** year)
month_pay = total / (year * 12)
print(f"Відсоткова ставка: {percent:.0f}")
print(f"Загальна сума кредиту: {total:.2f}")
print(f"Щомісячний платіж: {month_pay:.2f}")
