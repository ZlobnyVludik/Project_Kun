# Дан целочисленный список размера 10. Вывести все содержащиеся в данном списе
# четные числа в порядке убывания их индексов, а также их количество K.

def chet_chisla():
    
    # Создаем список
    numbers = []
    print("Введите 10 чисел: ")

    # Получаем значения
    for i in range(10):
        while True:
            try:
                value = int(input(""))
                numbers.append(value)
                break
            except ValueError:
                print("Нужны целые числа.")

    # Сохраняем чётные числа
    cel_numbers = []
    count_numbs = 0

    # Перебираем индексы
    for index in range(9, -1, -1):
        if numbers[index] % 2 == 0:
            cel_numbers.append(numbers[index])
            count_numbs += 1

    # Выводим
    print("\nЧётные цифры в порядке индекса: ")
    for num in cel_numbers:
        print(num)
    print(f"\nКол-во чётных чисел: {count_numbs}")


chet_chisla()
