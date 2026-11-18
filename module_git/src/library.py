# Завдання 14

while True:
    print("Введіть номер дії")
    print("1. Отримати книжку")
    print("2. Вихід")
    action = int(input())
    if action == 1:
        name = input("Введіть ім'я: ")
        book_name = input("Введіть назву книжки: ")
        print(f"Книжку {book_name} видано читачеві {name}")
    else:
        print("Дію програми завершенно")
        break
