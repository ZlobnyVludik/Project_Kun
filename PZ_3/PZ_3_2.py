# Единицы длины пронумерованы следующим образом: 1 - дециметр,
# 2 - километр, 3 - метр, 4 - милиметр, 5 - сантиметр.
# Дан номер единицы длины (целое число в диапазоне 1-5)
# и длина отрезка в этих единицах (вещественное число).
# Найти длину отрезка в метрах.

try:
    # Ввод цифры
    unit_number = int(input("Введите номер единицы длины (1-5): "))

    # Проверка
    if unit_number < 1 or unit_number > 5:
        raise ValueError("От 1 до 5 нужно.")

    # Длина
    length = float(input("Введите длину отрезка: "))

    # Проверка положительного числа
    if length < 0:
        raise ValueError("Только положительные числа.")

    # Конвертирую в метры
    if unit_number == 1:
        result = length / 10
        unit_name = "ДМ"
    elif unit_number == 2:
        result = length * 1000
        unit_name = "КМ"
    elif unit_number == 3:
        result = length
        unit_name = "М"
    elif unit_number == 4:
        result = length / 1000
        unit_name = "ММ"
    elif unit_number == 5:
        result = length / 100
        unit_name = "СМ"

    # Вывод результата
    print(f"Длина отрезка в метрах равна {result:.2f} метрам")

# Ошибки
except ValueError as e:
    if "Что-то не так." in str(e):
        print("Ошибка: Введите нормальное число.")
    else:
        print(f"Ошибка: {e}")
except Exception as e:
    print(f"Ошибка: {e}")
