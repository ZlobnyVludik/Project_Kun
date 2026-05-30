# В исходном текстовом файле (Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов.

import re

# Чтение текста из файла
with open("Dostoevsky.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Поиск произведений в кавычках «...»
p = re.compile(r"«.+?»", re.U)
books = p.findall(text)

# Удаление повторов с сохранением порядка
unique = list(dict.fromkeys(books))

print("Произведения:")
for book in unique:
    print(book)

print(f"\nКоличество: {len(unique)}")
