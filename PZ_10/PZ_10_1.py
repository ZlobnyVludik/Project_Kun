# Средствами языка Python сформировать текстовый файл (.txt), содержащий 
# последовательность из целых положительных и отрицательных чисел. Сформировать 
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую 
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Сумма элементов больших 10 во второй половине: 

from random import randint

# Формирование исходного файла
numbers = []

for i in range(15):
    numbers.append(randint(-50, 50))

file1 = open('data_8_1.txt', 'w', encoding='utf-8')
file1.write(' '.join(map(str, numbers)))
file1.close()

# Чтение данных из файла
file1 = open('data_8_1.txt', 'r', encoding='utf-8')
data = list(map(int, file1.read().split()))
file1.close()

# Индекс последнего минимального элемента
min_elem = min(data)
last_min_index = 0

for i in range(len(data)):
    if data[i] == min_elem:
        last_min_index = i

# Сумма элементов > 10 во второй половине
sum_gt_10 = 0
second_half = data[len(data) // 2:]

for num in second_half:
    if num > 10:
        sum_gt_10 += num

# Формирование итогового файла
file2 = open('data_8_2.txt', 'w', encoding='utf-8')

file2.write('Исходные данные:\n')
file2.write(' '.join(map(str, data)))
file2.write('\n')

file2.write(f'Количество элементов: {len(data)}\n')
file2.write(f'Индекс последнего минимального элемента: {last_min_index}\n')
file2.write(f'Сумма элементов больше 10 во второй половине: {sum_gt_10}\n')

file2.close()
