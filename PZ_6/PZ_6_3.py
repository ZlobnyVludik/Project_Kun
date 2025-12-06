
# Дан список размера N. Заменить каждый элемент списка на среднее арефметическое
# этого элемента и его соседей.

import random


def change_numbers():

    # Вводим размер списка
    n = random.randint(3, 20)
    print(f"Размер списка: {n}")
            
    # Складываем сюда полученные дальше значения
    numbers = [random.randint(-50, 50) for _ in range(10)]
    
    print("Сгенерированный список: ")
    print(numbers)
                
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
