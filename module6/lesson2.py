# Завдання 1
# text = input("Введіть текст: ")
# index = int(input("Введіть індекс: "))
# length_text = len(text)
#
# if index >= length_text:
#     print("Неправильний індекс.")
# else:
#     print(text[index])
#
# Завдання 2
# text = input("Введіть рядок: ")
#
# start = int(input("Введіть початковий індекс: "))
# end = int(input("Введіть кінцевий індекс: "))
#
# segment = text[start:end]
#
# print(segment)

# Завдання 3
# text = input("Введіть текст: ")
#
# index = int(input("Введіть індекс: "))
#
# segment1 = text[:index]
# segment2 = text[-index:]
#
# print(f"Перші {index} символів: {segment1}")
# print(f"Останні {index} символів: {segment2}")

# Завдання 4
# text = input("Введіть текст: ")
# if text[-1] in ".!?":
#     print("Цей текст є реченям.")
# else:
#     print("Цей текст не є реченням.")

# Завдання 5
# text = input("Введіть рядок: ")
#
# if text[0].isupper():
#     print("Перший символ — велика літера")
# else:
#     print("Перший символ — не велика літера")

# Завдання 6
# word = input("Введіть слова: ")
# word_modified = word.replace(" ", "")
# word_reversed = word_modified[::-1]
# if word_modified == word_reversed:
#     print("Це слово паліндром")
# else:
#     print("Це слово не паліндром")

# Завдання 7
# text = input("Введіть текст: ")
# symbol = input("Введіть символ: ")
#
# print(text.index(symbol))

# Завдання 8
# text = input("Введіть текст: ")
# symbol = input("Введіть символ: ")
# length_text = len(text)
# for index in range(length_text):
#     if symbol == text[index]:
#         print(index)

# Завдання 9
# while True:
#     word = input("Введіть слово: ")
#
#     if word == "END":
#         print("Завершення вводу")
#         break
#
#     if word[-3:] == "ing":
#         print("Це слово відноситься до герундіїв.")
#     elif word[-2:] == "ed":
#         print("Це слово відноситься до дієслова past tense.")
#     elif word[0] in "aeiou":
#         print("Це слово починається з голосної.")
#     else:
#         print("Це слово не відноситься до перших 3-х груп.")

# Завдання 10
# while True:
#     text = input("Введіть математичний вираз: ")
#     if text == "EXIT":
#         print("Розрахунки завершено.")
#         break
#
#     length_text = len(text)
#     isresult = False
#
#     for i in range(length_text):
#         if text[i] in "+-*/":
#             action = text[i]
#             value1 = float(text[:i])
#             value2 = float(text[(i + 1) :])
#
#             if action == "+":
#                 result = value1 + value2
#             elif action == "-":
#                 result = value1 - value2
#             elif action == "*":
#                 result = value1 * value2
#             elif action == "/":
#                 if value2 == 0:
#                     print("На 0 ділити не можна")
#                     continue
#                 else:
#                     result = value1 / value2
#
#             print(f"Результат: {result}")
#             isresult = True
#
#     if not isresult:
#         print("Знак дії не знайдено")

# Завдання 11
# text = input("Введіть текст та число: ")
# length_text = len(text)
#
# for i in range(length_text):
#     if text[i].isdigit() or text[i] == "-":
#         word = text[:i]
#         length_word = len(word)
#         word = word.replace(" ", "")
#         count = int(text[i:])
#         break
#
# if count > 0:
#     part1 = word[(length_word - count - 1) :]
#     part2 = word[: (length_word - count - 1)]
# else:
#     new_count = -count
#     part1 = word[new_count:]
#     part2 = word[:new_count]
#
# result = part1 + part2
# print(result)

# Завдання 12
text = input("Введіть текст: ")
count = int(input("Введіть зміщення: "))

print("Меню дій")
print("1. Зашифрувати")
print("2. Розшифрувати")
action = int(input("Введіть дію: "))
length_text = len(text)

result = ""
for i in range(length_text):
    temp = ord(text[i])

    if action == 1:
        temp += count
    elif action == 2:
        temp -= count

    result += chr(temp)

print(result)
