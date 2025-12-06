
# Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из символов C.

def create_string():
    try:
        # Получаем кол-во символов
        n = int(input("Введите целое число: "))
        if n <= 0:
            raise ValueError("Число должно быть больше 0.")
        # Получаем символ
        c = input("Введите символ: ")
        if len(c) != 1:
            raise ValueError("Необходимо ввести один символ.")

        # Получаем строгу из символов и выводим
        result = c * n
        print("Результат:", result)

    except ValueError as e:
        print("Ошибка:", {e})

create_string()
