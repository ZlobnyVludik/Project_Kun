
# Дана строка-предложение с избыточными пробелами между словами.
# Преобразовать ее так, чтобы между словами был ровно один пробел.

def probel(sentence):
    try:
        # Проверяем, чтобы кд был строкой
        if not isinstance(sentence, str):
            raise ValueError("Только строка.")
        # Исправляем пробелы
        return " ".join(sentence.split())
    except Exception:
        return "Ошибка!"
        
# Вывод
input_sentence = input("Введите предложение с лишними пробелами: ")
result = probel(input_sentence)
print(result)
