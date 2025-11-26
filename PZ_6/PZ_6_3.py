
# Дан список размера N. Заменить каждый элемент списка на среднее арефметическое
# Этого элемента и его соседей.

def change_numbers():
    while True:
        try:
            # Вводим размер списка
            n = int(input("Введите размер списка: "))
            if n <= 0:
                print("Только положительные.")
                continue
            break
        except ValueError:
            print("Целые числа.")
            
    # Складываем сюда полученные дальше значения
    numbers = []
    
    print(f"\nВведите {n} целых чисел: ")
    
    # Получаем числа
    for i in range(n):
        while True:
            try:
                value = int(input(f"Номер {i + 1}: "))
                numbers.append(value)
                break
            except ValueError:
                print("Целые числа!")
                
    # Список для измененных чисел
    new_numbers = []
    
    # Изменяем числа
    for i in range(n):
        if i == 0:
            average = (numbers[i] + numbers[i + 1]) / 2
            
        elif i == n - 1:
            average = (numbers[i] + numbers[i - 1]) / 2
            
        else:
            average = (numbers[i - 1] + numbers[i] + numbers[i + 1]) / 3
            
        new_numbers.append(average)
    
    # Вывод
    print("\nИзмененные числа: ")
    for i in range(n):
        print(f"Номер {i + 1}: {new_numbers[i]}")
        
change_numbers()
