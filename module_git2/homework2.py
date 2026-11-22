while True:
    print("Можливі дії:")
    print("1. Вибрати піцу")
    print("2. Вихід")
    action = int(input("Введіть номер дії: "))
    if action < 1 and action > 2:
        print("Неправильний номер дії")
        continue
    if action == 1:
        print("Меню з цінами піц")
        print("Маргарита – 150 грн")
        print("Пепероні – 180 грн")
        print("Чотири сири – 200 грн")
        name_pizza = input("Введіть назву піци: ")
        if (
            name_pizza != "Маргарита"
            or name_pizza != "Пепероні"
            or name_pizza != "Чотири сири"
        ):
            print("Неправильна назва піци")
            continue
        count_pizza = int(input("Введіть кількість: "))
        print(f"Замовлено {name_pizza}, {count_pizza} шт")
    else:
        print("Кінець замовлень.")
        break
