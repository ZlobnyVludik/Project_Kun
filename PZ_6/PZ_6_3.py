
# Дан список размера N. Заменить каждый элемент списка на среднее арефметическое
# этого элемента и его соседей.

import random


def replace_with_neighbor_average(values):
    """Создать новый список, где каждый элемент заменён средним
    арифметическим самого элемента и его соседей.
    """
    n = len(values)
    if n == 0:
        return []
    if n == 1:
        return [float(values[0])]

    result = [0.0] * n

    # Первый элемент
    result[0] = (values[0] + values[1]) / 2.0

    # Средние элементы
    for i in range(1, n - 1):
        result[i] = (values[i - 1] + values[i] + values[i + 1]) / 3.0

    # Последний элемент
    result[-1] = (values[-2] + values[-1]) / 2.0

    return result


def main():
    # Случайный размер списка N
    n = random.randint(5, 15)

    # Генерация случайного списка
    values = [random.randint(0, 20) for _ in range(n)]

    print("Размер списка N:", n)
    print("Оригинальный список:", values)

    averaged = replace_with_neighbor_average(values)
    print("Изменённый список:", averaged)


main()
