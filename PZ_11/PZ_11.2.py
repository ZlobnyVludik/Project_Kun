# Составить генератор (yield), который преобразует
# все буквенные символы в заглавные.

# Функция для преобрзования символа в верхний регистр
def to_upper(text):
    for char in text:
        yield char.upper()

# Получаем текст
small_text = input("Введите текст: ")
up = to_upper(small_text)

# Помещаем и выводим
big_text = "".join(up)
print(big_text)
