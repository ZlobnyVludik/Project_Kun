# Составить генератор (yield), который преобразует
# все буквенные символы в заглавные.

def to_upper(text):
    for char in text:
        yield char.upper()

small_text = input("Введите текст: ")
up = to_upper(small_text)

big_text = "".join(up)
print(big_text)
    
