# Завдання 1
# text = input("Введіть рядок англійською мовою: ")
#
# count = 0
# for letter in text:
#     if (
#         "a" in letter
#         or "e" in letter
#         or "i" in letter
#         or "o" in letter
#         or "u" in letter
#     ):
#         count += 1
#
# print(f"Кількість голосних літер: {count}")

# Завдання 2
text = input("Введіть текст англійською мовою: ")

while True:
    word = input("Введіть слово: ")
    if word == "EXIT":
        print("Завершення коригувань.")
        break
    upper_word = word.upper()
    if word in text:
        new_text = text.replace(word, upper_word)
        print(new_text)
        text = new_text
