PRICE_PILLOW = 650
PRICE_BLANKET = 1700
PRICE_LAMP = 500
PRICE_KEYCHAIN = 60

count_pillow = 0
count_blanket = 0
count_lamp = 0
count_keychain = 0
print("Можливі дії:")
print("1. додати товар")
print("2. видалити товар")
print("3. очистити кошик")
print("4. показати вміст кошики та суму покупки")
print("5. вихід")

while True:
    action = int(input("Введіть номер дії: "))
    if action == 3:
        print("Кошик очистенно.")
        count_pillow = count_lamp = count_blanket = count_keychain = 0
        continue
    elif action == 4:
        total = (
            count_pillow * PRICE_PILLOW
            + count_blanket * PRICE_BLANKET
            + count_lamp * PRICE_LAMP
            + count_keychain * PRICE_KEYCHAIN
        )
        if total == 0:
            print("Кошик порожній.")
            continue
        print("Вміст кошика:")
        if count_pillow > 0:
            print(f"{count_pillow}×{PRICE_PILLOW}={count_pillow * PRICE_PILLOW}")
        if count_blanket > 0:
            print(f"{count_blanket}×{PRICE_BLANKET}={count_blanket * PRICE_BLANKET}")
        if count_lamp > 0:
            print(f"{count_lamp}×{PRICE_LAMP}={count_lamp * PRICE_LAMP}")
        if count_keychain > 0:
            print(
                f"{count_keychain}×{PRICE_KEYCHAIN}={count_keychain * PRICE_KEYCHAIN}"
            )
        print(f"Сума покупки: {total} грн")
        continue
    elif action == 1:
        order = input("Введіть товар: ")
        if order == "подушка":
            count_pillow += 1
            continue
        elif order == "ковдра":
            count_blanket += 1
            continue
        elif order == "лампа":
            count_lamp += 1
            continue
        elif order == "брелок":
            count_keychain += 1
            continue
        else:
            print("Товар не знайдено")
    elif action == 2:
        remove_order = input("Введіть товар: ")
        if remove_order == "подушка":
            count_pillow -= 1
            continue
        elif remove_order == "ковдра":
            count_blanket -= 1
            continue
        elif remove_order == "лампа":
            count_lamp -= 1
            continue
        elif remove_order == "брелок":
            count_keychain -= 1
            continue
        else:
            print("Товар не знайдено")
            continue
    else:
        print("Кінець сеансу.")
        break
