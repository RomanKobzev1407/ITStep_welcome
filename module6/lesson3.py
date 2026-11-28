# Завдання 1
# numbers = [1, 8, -5, 9]
# print(f"{numbers = }")
#
# for index in range(len(numbers)):
#     numbers[index] *= 3
# print(f"{numbers = }")
#
# for index in range(len(numbers)):
#     if numbers[index] > 10:
#         numbers[index] = 0
# print(f"{numbers = }")

# Завдання 2
# numbers = []
# while True:
#     number = int(input("Введіть число: "))
#
#     if number == -1:
#         print("Завершення введення чисел")
#         break
#
#     numbers.append(number)
#
# print(f"{numbers = }")
# length_numbers = len(numbers)
# print(f"Довжина списку: {length_numbers}")
#
# sum_numbers = sum(numbers)
# print(f"Сума елементів списку: {sum_numbers}")
#
# max_numbers = max(numbers)
# print(f"Максимальний елемент списку: {max_numbers}")
#
# min_numbers = min(numbers)
# print(f"Мінімальний елемент списку: {min_numbers}")
#
# med_numbers = sum_numbers / length_numbers
# print(f"Середній елемент списку: {med_numbers}")

# Завдання 3
# positive = []
# negative = []
# while True:
#     number = int(input("Введіть число (0 для завершення): "))
#
#     if number == 0:
#         print("Завершення введення чисел")
#         break
#
#     if number > 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#
# print(f"Додатні числа: {positive = }")
# print(f"Від'ємні числа: {negative = }")

# Завдання 4
# salaries = []
# while True:
#     salary = int(input("Введіть зарплату працівника: "))
#
#     if salary == -1:
#         print("Завершення введення зарплат")
#         break
#
#     salaries.append(salary)
#
# print(f"список зарплат: {salaries = }")
#
# percent = int(input("Введіть відсоток зміни зарплати: "))
# length_salaries = len(salaries)
# for i in range(length_salaries):
#     salaries[i] *= (100 + percent) / 100
#
# print(f"список нових зарплат: {salaries = }")

# Завдання 5
# temperatures = []
# days = int(input("Введіть кількість днів: "))
#
# for i in range(days):
#     temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
#     temperatures.append(temperature)
#
# print("Температури:", temperatures)
#
# for i in range(1, days):
#     difference = temperatures[i] - temperatures[i - 1]
#     print(f"Різниця температур між {i + 1}-м та {i}-м днями: {difference}")

# Завдання 6
# accounts = []
# clients = 0
#
# while True:
#     print("Варіанти дій")
#     print("1. Додати клієнта")
#     print("2. Видалити клієнта")
#     print("3. Поповнити рахунок")
#     print("4. Зняти кошти")
#     print("5. Вихід")
#
#     action = int(input("Виберіть один з варіантів: "))
#     if action < 1 or action > 5:
#         print("Неправильна дія")
#         continue
#
#     if action == 5:
#         print("Завершення дій")
#         break
#
#     if action == 1:
#         accounts.append(0)
#         clients += 1
#
#     elif action > 1:
#         client_id = int(input("Введіть ID-клієнта: "))
#         if client_id > clients:
#             print("неправильний номер ID")
#             continue
#
#         if action == 2:
#             accounts.pop(client_id)
#             print(f"Рахунок {client_id} видалено")
#
#         elif action == 3:
#             addition = int(input("Введіть суму додавання: "))
#             accounts[client_id] += addition
#             print(f"Рахунок {client_id} тепер {accounts[client_id]}")
#
#         elif action == 4:
#             subtraction = int(input("Введіть суму зняття: "))
#             accounts[client_id] -= subtraction
#             print(f"Рахунок {client_id} тепер {accounts[client_id]}")
#
#     print(f"список рахунків {accounts = }")

# Завдання 7
shop_items = ["яблуко", "груша", "апельсин", "мандарин", "молоко"]
max_items = len(shop_items)
shop_prices = [12, 34, 21, 43, 62]
user_items = []
user_counts = []

while True:
    print("Доступні товари з цінами")
    for i in range(len(shop_items)):
        print(f"{shop_items[i]} {shop_prices[i]}")

    print("Варіанти дій")
    print("1. Додати товар до кошика")
    print("2. Видалити товар з кошика")
    print("3. Очистити кошик")
    print("4. Вивести загальну ціну")
    print("5. Вихід")

    action = int(input("Виберіть один з варіантів: "))
    if action < 1 or action > 5:
        print("Неправильна дія")
        continue

    if action == 5:
        print("Завершення покупок")
        break

    if action == 1:
        user_items.append(0)
        user_counts.append(0)
        user_item = int(input("Введіть індекс товару: "))
        if user_item > max_items:
            print("неправильний індекс товару")
            continue
        user_items[-1] = user_item
        count_item = int(input("Введіть кількість: "))
        user_counts[-1] = count_item
        print(f"Товар {user_item} додано у кошик")
        print(f"{user_items = }")
        print(f"{user_counts = }")

    elif action == 2:
        user_item = int(input("Введіть індекс товару у кошику: "))
        user_items.pop(user_item)
        user_counts.pop(user_item)
        print(f"Товар {user_item} видалено з кошику")
        print(f"{user_items = }")
        print(f"{user_counts = }")

    elif action == 3:
        for j in range(len(user_counts)):
            user_items.pop(j)
            user_counts.pop(j)
        print("Товари з кошику видалені")
        print(f"{user_items = }")
        print(f"{user_counts = }")

    elif action == 4:
        summary = 0
        for k in range(len(user_counts)):
            index = user_items[k]
            summary += user_counts[k] * shop_prices[index]
        print(f"Загальна вартість товарів у кошику: {summary}")
