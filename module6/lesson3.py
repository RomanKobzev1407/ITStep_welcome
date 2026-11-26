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
numbers = []
while True:
    number = int(input("Введіть число: "))

    if number == -1:
        print("Завершення введення чисел")
        break

    numbers.append(number)

print(f"{numbers = }")
length_numbers = len(numbers)
print(f"Довжина списку: {length_numbers}")

sum_numbers = sum(numbers)
print(f"Сума елементів списку: {sum_numbers}")

max_numbers = max(numbers)
print(f"Максимальний елемент списку: {max_numbers}")

min_numbers = min(numbers)
print(f"Мінімальний елемент списку: {min_numbers}")

med_numbers = sum_numbers / length_numbers
print(f"Середній елемент списку: {med_numbers}")
