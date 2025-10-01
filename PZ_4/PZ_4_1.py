# Даны два целых числа A и B (A < B). Найти сумму квадратов всех
# целых чисел от A до B включительно

try:
    # Получаем значения
    A = int(input("Введите A: "))
    B = int(input("Введите B: "))

    # Проверка условия
    if A >= B:
        raise ValueError("A должно быть меньше B.")

    # Вычисляем
    total = 0
    for i in range(A, B + 1):
        total += i ** 2

        # Ответ
        print(f"Сумма квадратов: {total}")

except ValueError as e:
    if str(e) == "A должно быть меньше B":
        print(f"Ошибка: {e}")
    else:
        print(f"Ошибка: Введите нормальные числа")

except Exception as e:
    print(f"Произошло что-то странное: {e}")
