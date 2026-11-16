# Завдання 1
'''PRICE1 = 80
PRICE2 = 200
PRICE3 = 120

age = int(input("Введіть вік: "))
if age < 12:
    ticket = PRICE1
elif age >= 12 and age <= 65:
    ticket = PRICE2
else:
    ticket = PRICE3

print(f"Вартість квитка: {ticket} грн.")
print("Бажаємо приємного перегляду та гарного дня")'''

# Завдання 2

'''weight = float(input("Введіть вагу товару в кг: "))
if weight < 1:
    print("Дрібна посилка")
elif weight < 5:
    print("Середня посилка")
elif weight < 10:
    print("Велика посилка")
else:
    print("Надважка посилка")'''

# Завдання 3
'''month = input("Введіть місяць: ")
date = int(input("Введіть число місяця: "))
if date == 1 and month == "січень":
    print("Сьогодні Новий Рік")
elif date == 14 and month == "лютий":
    print("Сьогодні день Святого Валентина")
elif date == 25 and month == "грудень":
    print("Сьогодні Різдво")
elif date == 1 and month == "квітень":
    print("Сьогодні день сміху")
else:
    print("Сьогодні звичайний день")'''

# Завдання 4
'''PRICE1 = 80
PRICE2 = 200
PRICE3 = 120

age1 = int(input("Введіть вік першої людини: "))
age2 = int(input("Введіть вік другої людини: "))
age3 = int(input("Введіть вік третьої людини: "))

if age1 < 12:
    ticket1 = PRICE1
elif age1 >= 12 and age1 <= 65:
    ticket1 = PRICE2
else:
    ticket1 = PRICE3

if age2 < 12:
    ticket2 = PRICE1
elif age2 >= 12 and age2 <= 65:
    ticket2 = PRICE2
else:
    ticket2 = PRICE3

if age3 < 12:
    ticket2 = PRICE1
elif age3 >= 12 and age3 <= 65:
    ticket3 = PRICE2
else:
    ticket3 = PRICE3

ticket = ticket1 + ticket2 + ticket3

print(f"Вартість першого квитка: {ticket1} грн.")
print(f"Вартість другого квитка: {ticket2} грн.")
print(f"Вартість третього квитка: {ticket3} грн.")
print(f"Загальна вартість: {ticket} грн.")
print("Бажаємо приємного перегляду та гарного дня")'''

# Завдання 5

'''# Введіть назву товару
product = input("Введіть назву товару: ")
# Продукт обмежений в продажу?
if product == "алкоголь" or product == "тютюн":
    # Введіть вік
    age = int(input("Введіть ваш вік: "))
    # Якщо вік більше або дорівнює 18 років
    if age >= 18:
        print("Дозволено до продажу")
    # Якщо молодше за 18 років
    else:
        print("Заборонено до продажу")
# Якщо продукт ліки
elif product == "ліки":
    # Рецепт від лікаря
    prescription = input("У вас є рецепт від лікаря? ")
    # Якщо є рецепт
    if prescription == "так":
        print("Дозволено до продажу")
    # Якщо немає
    else:
        print("Заборонено до продажу")
# Якщо інші товари
else:
    print("Дозволено до продажу")'''

# Завдання 6
'''is_logged_in = input("Ви увійшли в систему? (так/ні): ")
cart_is_empty = input("Ваш кошик порожній? (так/ні): ")
balance = float(input("Введіть баланс: "))
total_price = float(input("Введіть вартість замовлення: "))
if is_logged_in == "ні":
    print("Будь ласка, увійдіть в систему")
else:
    if cart_is_empty == "так":
        print("Ваш кошик порожній")
    else:
        if balance < total_price:
            print("Недостатньо коштів на рахунку")
        else:
            print("Замовлення успішно оформлено!")'''

# Завдання 7

speed = int(input("Введіть швидкість: "))
if speed > 90:
    place = input("Де зараз рухаємось (місто або траса): ")
    if place == "місто":
        print("Штраф за перевищення швидкості!!!")
    else:
        print("Будьте уважним!")
elif speed < 20:
    car_age = int(input("Скільки років машині? "))
    if car_age > 15:
        print("Краще купити нову машину.")
    else:
        print("Може поїхати на СТО?")
else:
    print("Гарної подорожі!!!")