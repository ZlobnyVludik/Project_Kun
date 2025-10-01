# Единицы длины пронумерованы следующим образом: 1 - дециметр,
# 2 - километр, 3 - метр, 4 - милиметр, 5 - сантиметр.
# Дан номер единицы длины (целое число в диапазоне 1-5)
# и длина отрезка в этих единицах (вещественное число).
# Найти длину отрезка в метрах.

try:
    # Ввод цифры
    unit_number = int(input("Введите номер единицы длины: "))

    # Провера от 1 до 5
    if unit_number < 1 or unit_number > 5:
        raise ValueError("От 1 до 5 цифры.")

    # Ввод длины
    length = int(input("Введите длину: "))

    # Проврка на отрицательные значения
    if length < 0:
        raise ValueError("Без отрицательных значений нужно.")

    # Определение коэффциента
    factor = 0.1 if unit_number == 1 else \
             1000 if unit_number == 2 else \
             1 if unit_number == 3 else \
             0.001 if unit_number == 4 else \
             0.01 if unit_number == 5 else None

    # Считаем
    result = length * factor
    print(f"Длина отрезка в метрах: {result}")

# Проверка на ошибку
except ValueError as e:
    print(f"Ошибка: {e}")
