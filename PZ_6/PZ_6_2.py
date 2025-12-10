
# Дан список размера N. Найти кол-во участков, на которых его элементы монотонно возрастают.

import random


def incresing_numbers():
    # Получаем размер списка
    n = random.randint(2, 20)
    print(f"\nРазмер списка: {n}")

    # Складываем сюда полученные дальше значения
    numbers = [random.randint(-50, 50) for _ in range(n)]
    print("\nСгенерированный список: ")
    print(numbers)

    # Считаем кол-во участков
    count_segments = 0
    in_segment = False

    # Проверка на возрастание
    for i in range(1, n):
        if numbers[i] > numbers[i - 1]:
            if not in_segment:
                count_segments += 1
                in_segment = True
        else:
            in_segment = False

    # Вывод
    print(f"\nКол-во участков: {count_segments}")


incresing_numbers()
