# Завдання 14

while True:
    print("Введіть номер дії")
    print("1. Отримати книжку")
    print("2. Повернути книжку")
    print("3. Вихід")
    action = int(input())
    if action == 1:
        name = input("Введіть ім'я: ")
        book_name = input("Введіть назву книжки: ")
        days = int(input("Кількість днів: "))
        print(f"Книжку {book_name} видано читачеві {name} на {days} днів")
    elif action == 2:
        name = input("Введіть ім'я: ")
        book_name = input("Введіть назву книжки: ")
        print(f"Читач {name} повернув книжку {book_name}")
    else:
        print("Дію програми завершено")
        break
