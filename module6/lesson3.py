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
salaries = []
while True:
    salary = int(input("Введіть зарплату працівника: "))

    if salary == -1:
        print("Завершення введення зарплат")
        break

    salaries.append(salary)

print(f"список зарплат: {salaries = }")

percent = int(input("Введіть відсоток зміни зарплати: "))
length_salaries = len(salaries)
for i in range(length_salaries):
    salaries[i] *= (100 + percent) / 100

print(f"список нових зарплат: {salaries = }")
