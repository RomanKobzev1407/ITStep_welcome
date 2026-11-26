# Завдання 1
numbers = [1, 8, -5, 9]
print(f"{numbers = }")

for index in range(len(numbers)):
    numbers[index] *= 3
print(f"{numbers = }")

for index in range(len(numbers)):
    if numbers[index] > 10:
        numbers[index] = 0
print(f"{numbers = }")
