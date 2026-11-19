# Завдання 1
# text = input("Введіть текст: ")
# symbol = input("Введіть символ: ")
#
# result1 = text.count(symbol)
# print(f"Символ {symbol} зустрічається {result1} разів")
#
# result2 = 0
# for c in text:
#     if c == symbol:
#         result2 += 1
# print(f"Символ {symbol} зустрічається {result2} разів")


# Завдання 2

# text = input("Введіть текст: ")
# length = len(text)
# print(f"Кількість символів: {length}")
#
# isword = "Python" in text
# if isword:
#     print("Слово \"Python\" є в тексті")
# else:
#     print("Слова \"Python\" немає в тексті")
#
# count_letters = 0
# for ch in text:
#     if ch == "s" or ch == "z" or ch == "h":
#     count_letters += 1
# print(f"Кількість шиплячих у тексті: {count_letters}")

# Завдання 3
# text = input("Введіть текст: ")
#
# result = text.replace(" ", "-")
# print(f"Змінений текст: {result}")

# Завдання 4
# text = input("Введіть текст: ")
# word = input("Введіть слово: ")
#
# result = text.count(word)
# print(f"Слово {word} зустрічається {result} разів")

# Завдання 5
items = input("Введіть ваші речі: ")
items = items.lower()

condition1 = "ніж" in items
condition2 = "гроші" in items
condition3 = "отрута" in items

if condition1 or condition2 or condition3:
    print("У вас є речі які заборонено перевозити")
else:
    print("Оформлено доставку")

# Завдання 6
# text = input("Введіть текст: ")
#
# count_alpha = 0
# count_digit = 0
#
# for ch in text:
#     if ch.isalpha():
#         count_alpha += 1
#     elif ch.isdigit():
#         count_digit += 1
#
# print(f"Кількість літер: {count_alpha}")
# print(f"Кількість цифр: {count_digit}")

# Завдання 7
# while True:
#     password = input("Введіть пароль: ")
#
#     length_pass = len(password)
#     if length_pass < 8:
#         print("Недостатня довжина")
#         continue
#
#     count_alpha = 0
#     count_digit = 0
#     for ch in password:
#         if ch.isalpha():
#             count_alpha += 1
#         elif ch.isdigit():
#             count_digit += 1
#
#     if count_alpha == 0:
#         print("Пароль повинен містити хоча б одну літеру")
#         continue
#
#     if count_digit == 0:
#         print("Пароль повинен містити хоча б одну цифру")
#         continue
#
#     print("Пароль відповідає вимогам")
#     break
