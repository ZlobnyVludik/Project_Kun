
# Дана строка-предложение с избыточными пробелами между словами.
# Преобразовать ее так, чтобы между словами был ровно один пробел.

def normalize_spaces():
    try:
        # Получаем предложение
        text = input("Введите строку с лишними пробелами: ").strip()
        if not text:
            raise ValueError("Пустая строка.")

        # Исправляем пробелы
        normalized = " ".join(text.split())

        # Выводим результат
        print("Результат:", normalized)

    except ValueError as e:
        print("Ошибка:", {e})

normalize_spaces()
