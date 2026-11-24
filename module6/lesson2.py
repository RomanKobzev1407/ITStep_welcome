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
text = input("Введіть рядок: ")

start = int(input("Введіть початковий індекс: "))
end = int(input("Введіть кінцевий індекс: "))

segment = text[start:end]

print(segment)
