
# Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из символов C.

def make_string()
    try:
        # Получаем число N
        N = int(input("Введите целое число N (>0): "))
        if N <= 0:
            raise ValueError("Число должно быть больше 0")
        # Получаем число C
        C = input("Введите символ C: ")
        if len(C) != 1:
            raise ValueError("Введено более одного символа")
        
        # Получаем строку из символов
        result = C * N
        
        # Вывод результата
        print(f"Строка длины {N} из символов '{C}':")
        print(result)
        return result
        
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return None

make_string()
