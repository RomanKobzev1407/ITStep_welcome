# Завдання 1

"""'# Вводимо масу глини
clay = float(input("Введіть масу глини (кг): "))
# Переводимо масу у грами
clay *= 1000
# Вводимо грамів для фігурки
clay_per_figure = 130
# Знаходимо кількість фігур
figures = clay // clay_per_figure
# Виводимо результат
print(f"Можна зробити: {figures:.0f} фігурок")"""

# Завдання 2
"""fishman_1 = int(input("Введіть кількість риби у 1-го рибалки: "))
fishman_2 = int(input("Введіть кількість риби у 2-го рибалки: "))
fishman_3 = int(input("Введіть кількість риби у 3-го рибалки: "))
average_fish = (fishman_1 + fishman_2 + fishman_3) / 3
max_fish = max(fishman_1, fishman_2, fishman_3)
print(f"Середня кількість риби: {average_fish:.2f}")
print(f"Максимальна кількість риби: {max_fish}")"""

# Завдання 3
"""budget = float(input("Введіть величину бюджету (грн): "))
count_casual = budget // 150
count_vip = budget // 250
print(f"За даний бюджет можна купити {count_casual:.0f} звичайних квитків.")
print(f"За даний бюджет можна купити {count_vip:.0f} VIP квитків.")"""

# Завдання 4
sum_money = float(input("Введіть суму грошей (грн): "))
count_500 = sum_money // 500
rest_money = sum_money - (count_500 * 500)
count_200 = rest_money // 200
rest_money = rest_money - (count_200 * 200)
count_100 = rest_money // 100
rest_money = rest_money - (count_100 * 100)
print(f"Купюр по 500: {count_500:.0f}")
print(f"Купюр по 200: {count_200:.0f}")
print(f"Купюр по 100: {count_100:.0f}")
print(f"Решта: {rest_money:.2f}")
