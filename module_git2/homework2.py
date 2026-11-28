PRICE_MARGARITA = 150
PRICE_PEPERONI = 180
PRICE_4CHEESE = 200

count_margarita = 0
count_peperoni = 0
count_4cheese = 0

order_margarita = 0
order_peperoni = 0
order_4cheese = 0

while True:
    print("Можливі дії:")
    print("1. Вибрати піцу")
    print("2. Завершення замовлень")
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
        if name_pizza == "Маргарита":
            count_margarita = int(input("Введіть кількість (0 - 15): "))
            if count_margarita < 0 or count_margarita > 15:
                print("Неправильна кількість")
                continue
            order_margarita += count_margarita * PRICE_MARGARITA
            print(
                f"Замовлено {name_pizza}, {count_margarita} шт, {order_margarita} грн"
            )
        elif name_pizza == "Пепероні":
            count_peperoni = int(input("Введіть кількість (0 - 15): "))
            if count_peperoni < 0 or count_peperoni > 15:
                print("Неправильна кількість")
                continue
            order_peperoni += count_peperoni * PRICE_PEPERONI
            print(f"Замовлено {name_pizza}, {count_peperoni} шт, {order_peperoni} грн")
        elif name_pizza == "Чотири сири":
            count_4cheese = int(input("Введіть кількість (0 - 15): "))
            if count_4cheese < 0 or count_4cheese > 15:
                print("Неправильна кількість")
                continue
            order_4cheese += count_4cheese * PRICE_4CHEESE
            print(f"Замовлено {name_pizza}, {count_4cheese} шт, {order_4cheese} грн")
        else:
            print("Неправильна назва піци")
            continue
    else:
        summary = order_margarita + order_peperoni + order_4cheese
        if summary > 0:
            print("========== ВАШЕ ЗАМОВЛЕННЯ ==========")
            print("")
            print("Піца Кількість Вартість")
            print("--------------------------------------")
            if count_margarita > 0:
                print(f"Маргарита {count_margarita} {order_margarita}")
            if count_peperoni > 0:
                print(f"Пепероні {count_peperoni} {order_peperoni}")
            if count_4cheese > 0:
                print(f"Чотири сири {count_4cheese} {order_4cheese}")
            print("--------------------------------------")
            print(f"Загальна вартість: {summary} грн")
            print("======================================")
            print("Дякуємо за замовлення!")
        else:
            print("Замовлення немає.")
        break
