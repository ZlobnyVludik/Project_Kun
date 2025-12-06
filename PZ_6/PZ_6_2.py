
# Дан список размера N. Найти кол-во участков, на которых его элементы монотонно возрастают.

def incresing_numbers():
    while True:
        try:
            # Получаем размер списка
            n = int(input("Введите размер списка: "))
            if n <= 0:
                print("Только положительные.")
                continue
            break
        except ValueError:
            print("Целые числа.")

    # Складываем сюда полученные дальше значения
    numbers = []
    
    print(f"\nВведите {n} значений: ")

    # Вводим числа
    for i in range(n):
        while True:
            try:
                value = int(input(f"Значение {i+1}: "))
                numbers.append(value)
                break
            except ValueError:
                print("Целые числа!!!")

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
    print(f"Кол-во участков: {count_segments}")


incresing_numbers()
