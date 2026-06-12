# Средствами языка Python сформировать текстовый файл (.txt), содержащий 
# последовательность из целых положительных и отрицательных чисел. Сформировать 
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую 
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Сумма элементов больших 10 во второй половине: 

import random

n = int(input("Введите количество элементов: "))

numbers = [random.randint(-30, 30) for _ in range(n)]

file1 = open('data_8.txt', 'w')
file1.write(' '.join(map(str, numbers)))
file1.close()

file1 = open('data_8.txt', 'r')
data_str = file1.read()
file1.close()
numbers_list = list(map(int, data_str.split()))

total_count = len(numbers_list)

product = 1
for num in numbers_list:
    product *= num

pair_count = 0
for i in range(total_count - 1):
    if (numbers_list[i] * numbers_list[i + 1]) % 3 == 0:
        pair_count += 1

file2 = open('result_8.txt', 'w')
file2.write('Исходные данные:\n')
file2.write(' '.join(map(str, numbers_list)) + '\n')
file2.write('Количество элементов: ' + str(total_count) + '\n')
file2.write('Произведение элементов: ' + str(product) + '\n')
file2.write('Количество пар, для которых произведение элементов делится на 3: ' + str(pair_count) + '\n')
file2.close()
