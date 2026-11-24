# Завдання 1
# text = input("Введіть текст: ")
# index = int(input("Введіть індекс: "))
# length_text = len(text)
#
# if index >= length_text:
#     print("Неправильний індекс.")
# else:
#     print(text[index])

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
word = input("Введіть слово: ")
word2 = word[::-1]
if word == word2:
    print("Це слово паліндром")
else:
    print("Це слово не паліндром")
