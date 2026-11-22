while True:
    print("Можливі дії:")
    print("1. Вибрати піцу")
    print("2. Вихід")
    action = int(input("Введіть номер дії: "))
    if action == 1:
        name_pizza = input("Введіть назву піци: ")
        count_pizza = int(input("Введіть кількість: "))
        print(f"Замовлено {name_pizza}, {count_pizza} шт")
    else:
        print("Кінець замовлень.")
        break
