# Завдання 1
"""# Вводимо радіус кола
radius = float(input("Введіть радіус: "))
# Вводимо константу пі
pi = 3.1415
# Знаходимо площу
area = pi * radius ** 2
# Виводимо результат
print(f"Площа кола: {area:.2f}")"""

# Завдання 2
"""cup_price = float(input("Введіть ціну однієї кружки: "))
total_budget = float(input("Введіть бюджет: "))
cup_count = total_budget // cup_price
print(f"Можна купити: {cup_count:.0f} кружки")"""

# Завдання 3
"""length_m = float(input("Введіть довжину в метрах: "))
meter_to_foot = 3.2808399
meter_to_yard = 1.0936133
length_ft = length_m * meter_to_foot
length_yd = length_m * meter_to_yard
print(f"Довжина у футах: {length_ft:.6f}")
print(f"Довжина у ярдах: {length_yd:.6f}")"""

# Завдання 4
"""cup_price = float(input("Введіть ціну однієї кружки: "))
total_budget = float(input("Введіть бюджет: "))
cup_count = total_budget // cup_price
rest_budget = total_budget % cup_price
print(f"Можна купити: {cup_count:.0f} кружки")
print(f"Залишок коштів: {rest_budget:.2f}")"""

# Завдання 5
"""total_minutes = int(input("Введіть кількість хвилин: "))
count_hours = total_minutes // 60
count_minutes = total_minutes % 60
print(f"Годин: {count_hours}")
print(f"Хвилин: {count_minutes}")"""

# Завдання 6
"""total_apples = int(input("Введіть кількість яблук: "))
total_milk = float(input("Введіть кількість молока (л): "))
pie_count_apple = total_apples // 4
pie_count_milk = total_milk // 1.2
pie_count = min(pie_count_apple, pie_count_milk)
print(f"Можна спекти пирогів: {pie_count:.0f}")
rest_apple = total_apples - (4 * pie_count)
rest_milk = total_milk - (1.2 * pie_count)
print(f"Залишиться яблук: {rest_apple:.0f}")
print(f"Залишиться молока: {rest_milk:.2f}")"""

# Завдання 7
"""sum_money = float(input("Введіть суму вкладу: "))
percent = float(input("Введіть відсоток: "))
sum_money_1 = sum_money * (1 + percent / 100)
sum_money_2 = sum_money_1 * (1 + percent / 100)
sum_money_3 = sum_money_2 * (1 + percent / 100)
sum_money_4 = sum_money_3 * (1 + percent / 100)
sum_money_5 = sum_money_4 * (1 + percent / 100)
print(f"Сума вкладу після 1-го року: {sum_money_1:.2f}")
print(f"Сума вкладу після 2-го року: {sum_money_2:.2f}")
print(f"Сума вкладу після 3-го року: {sum_money_3:.2f}")
print(f"Сума вкладу після 4-го року: {sum_money_4:.2f}")
print(f"Сума вкладу після 5-го року: {sum_money_5:.2f}")"""

# Завдання 8
total_days = int(input("Введіть кількість днів: "))
count_years = total_days // 365
count_weeks = (total_days - count_years * 365) // 7
count_days = total_days - count_years * 365 - count_weeks * 7
print(f"{total_days} днів ")
print(f"— це {count_years:.0f} рік, {count_weeks} тижні та {count_days:.0f} днів.")
