
# Дан список размера N. Заменить каждый элемент списка на среднее арефметическое
# этого элемента и его соседей.

import random


def average_numb(values):

    # Получаем сюда длину списка
    n = len(values)

    # Заполняем список
    result = [0.0] * n

    # Первый элемент
    result[0] = (values[0] + values[1]) / 2.0

    # Средние элементы
    for i in range(1, n - 1):
        result[i] = (values[i - 1] + values[i] + values[i + 1]) / 3.0

    # Последний элемент
    result[-1] = (values[-2] + values[-1]) / 2.0

    return result


# Делаем, чтобы выводилось столбиком
def colonki(values):
    for x in values:
        print(x)


def main():
    # Случайный размер списка
    n = random.randint(3, 20)

    # Cлучайный список
    values = [random.randint(-30, 30) for _ in range(n)]

    # Получаем обработанный список
    averaged = average_numb(values)

    # Выводим результат
    print("\nРазмер списка:", n)
    print("\nОригинальный список:")
    colonki(values)

    print("\nИзменённый список:")
    colonki(averaged)


main()
