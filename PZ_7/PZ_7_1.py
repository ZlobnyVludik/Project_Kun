
# Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из символов C.

def make_string(n, c):
    try:
        # Проверяем, чтобы N был больше 0
        n = int(n)
        if n <= 0:
            raise ValueError("Больше 0.")
        # Проверяем, чтобы C было 1 символом.
        if len(c) != 1:
            raise ValueError("Только 1 символ.")
        # Возвращаем ответ
        return c * n
    except ValueError:
        return print("Ошибка!")
        
# Получаем значения
n_input = input("Введите число: ")
c_input = input("Введите символ: ")

# Вывод
result = make_string(n_input, c_input)
print(result)
