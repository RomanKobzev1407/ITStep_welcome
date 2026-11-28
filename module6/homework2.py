# Завдання 1
text = input("Введіть текст та число: ")
length_text = len(text)

for i in range(length_text):
    if text[i].isdigit() or text[i] == "-":
        word = text[:i]
        word = word.replace(" ", "")
        length_word = len(word)
        count = int(text[i:])
        break

if count >= 0:
    result = text[:count] + "*" + text[(count + 1) :]
else:
    result = text[: (length_word + count)] + "*" + text[(length_word + count + 1) :]

print(result)
