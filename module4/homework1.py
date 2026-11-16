# Завдання 1

'''total = 0
for number in range(1, 6):
    total += number

print(f"Сума: {total}")'''

# Завдання 2

'''start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

for i in range(start, end+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)'''

# Завдання 3

norm = 50
days = 5

total = 0
for day in range(1 , days+1):
    deliv = int(input(f"Введіть кількість доставок за {day}-й день: "))
    total += deliv

print(f"Загальна кількість доставок за тиждень: {total}")

delta = norm - total

if delta <= 0:
    print("Тижневу норму виконано!")
else:
    print(f"Тижневу норму не виконано! Не вистачає {delta} доставок")

