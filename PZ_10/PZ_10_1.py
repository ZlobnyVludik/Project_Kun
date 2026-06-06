# Средствами языка Python сформировать текстовый файл (.txt), содержащий 
# последовательность из целых положительных и отрицательных чисел. Сформировать 
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую 
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Сумма элементов больших 10 во второй половине: 

import random

# Формируем список случайных чисел
numbers = [random.randint(-20, 30) for _ in range(15)]

# Записываем исходные данные в файл
file1 = open("data_8.txt", "w", encoding="utf-8")
file1.write(" ".join(map(str, numbers)))
file1.close()

# Читаем данные из файла
file1 = open("data_8.txt", "r", encoding="utf-8")
data = list(map(int, file1.read().split()))
file1.close()

# Количество элементов
count_elements = len(data)

# Индекс последнего минимального элемента
min_element = min(data)
last_min_index = len(data) - 1 - data[::-1].index(min_element)

# Вторая половина списка
second_half = data[len(data) // 2:]

# Сумма элементов больше 10 во второй половине
sum_more_than_10 = 0
for num in second_half:
    if num > 10:
        sum_more_than_10 += num

# Запись результата в новый файл
file2 = open("result_8.txt", "w", encoding="utf-8")

file2.write("Исходные данные:\n")
file2.write(" ".join(map(str, data)) + "\n")
file2.write(f"Количество элементов: {count_elements}\n")
file2.write(f"Индекс последнего минимального элемента: {last_min_index}\n")
file2.write(f"Сумма элементов больших 10 во второй половине: {sum_more_than_10}\n")

file2.close()

print("Файл result_8.txt успешно создан.")
