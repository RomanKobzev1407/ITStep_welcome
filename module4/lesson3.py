# Завдання 1

'''while True:
    numb = int(input("Введіть число (1-9): "))
    if numb < 1 or numb > 9:
        print("Введено неправильне число")
        continue
    else:
        for multi in range(1, 11):
            result = numb * multi
            print(f"{numb} * {multi} = {result}")
        break'''

# Завдання 2

'''total = 0
count = 0
while True:
    grade = int(input("Введіть оцінку (1-12; 0 - кінець розрахунку): "))
    if grade == 0:
        break
    elif grade > 12 or grade < 0:
        print("Оцінка поза межами інтервалу.")
        continue
    else:
        total += grade
        count += 1

average_grade = total / count
print(f"середня оцінка: {average_grade:.2f}")'''

# Завдання 3
'''while True:

    print("Можливі дії з числами:")
    print("1. додавання")
    print("2. віднімання")
    print("3. множення")
    print("4. ділення")
    print("5. вихід")
    action = int(input("Введіть номер дії: "))
    
    if action < 1 or action > 5:
        print("Неправильний номер дії")
        continue
    elif action == 5:
        print("Кінець розрахунків")
        break
    else:
        value1 = float(input("Введіть перше число: "))
        value2 = float(input("Введіть друге число: "))

    if action == 1:
        result = value1 + value2
        print(f"Результат розрахунків: {result}")
    elif action == 2:
        result = value1 - value2
        print(f"Результат розрахунків: {result}")
    elif action == 3:
        result = value1 * value2
        print(f"Результат розрахунків: {result}")
    else:
        if value2 == 0:
            print("На 0 ділити не можна")
            continue
        else:
            result = value1 / value2
            print(f"Результат розрахунків: {result}")'''

# Завдання 4
'''i = 1
while True:
    name = input("Введіть ім'я: ")
    if name == "admin":
        print("Це ім'я недоступне")
    else:
        print(f"Учасник №{i}: {name}")
        i += 1
    if i > 3:
        break'''

# Завдання 5 (в завданні два номера - 4)

'''import random
secret_num = random.randint(0, 100)
count = 0

while True:
    user = input("Введіть число (stop - кінець розрахунків): ")
    if user == "stop":
        print(f"Загадане число: {secret_num:.0f}, Кількість спроб: {count:.0f}")
        break
    else:
        num_user = int(user)
    if num_user == secret_num:
        print("Вірно")
        print(f"Загадане число: {secret_num:.0f}, Кількість спроб: {count:.0f}")
        break
    elif num_user > secret_num:
        print("Більше ніж загадане число")
        count += 1
    elif num_user < secret_num:
        print("Меньше ніж загадане число")
        count += 1'''

# Завдання 6

import random

count_win = 0
count_loss = 0
count_draw = 0

while True:
    print("Можливі дії:")
    print("1. Нова гра")
    print("2. вихід")
    action = int(input("Введіть номер дії: "))
    if action == 1:
        rounds = int(input("Введіть кількість раундів: "))
        for i in range(rounds):
            print(f"Раунд №{i+1}")
            word = input("Введіть слово (камінь, ножиці, папір): ")
            if word != "камінь" and word != "ножиці" and word != "папір":
                print("Неправильне слово - програш")
                count_loss += 1
                continue

            computer_choice = random.choice(["камінь", "ножиці", "папір"])
            print("Вибір компа - ",computer_choice)
            if computer_choice == "камінь":
                if word == "ножиці":
                    print("Програш")
                    count_loss += 1
                elif word == "папір":
                    print("Перемога")
                    count_win += 1
                else:
                    print("Нічия")
                    count_draw += 1
            elif computer_choice == "ножиці":
                if word == "папір":
                    print("Програш")
                    count_loss += 1
                elif word == "камінь":
                    print("Перемога")
                    count_win += 1
                else:
                    print("Нічия")
                    count_draw += 1
            elif computer_choice == "папір":
                if word == "ножиці":
                    print("Перемога")
                    count_win += 1
                elif word == "камінь":
                    print("Програш")
                    count_loss += 1
                else:
                    print("Нічия")
                    count_draw += 1

        print("Кінець гри.")
        print(f"Кількість перемог: {count_win}")
        print(f"Кількість програшів: {count_loss}")
        print(f"Кількість нічиїх: {count_draw}")
    else:
        print("Кінець сеансу.")
        break

# Завдання 7
# Дане завдання одразу було виконанно в процесі розробки програми до попереднього завдання.