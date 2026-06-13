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

numbers = [random.randint(-10, 25) for _ in range(n)]

f1 = open('data_8.txt', 'w')
f1.write(' '.join(map(str, numbers)))
f1.close()

f1 = open('data_8.txt', 'r')
content = f1.read()
f1.close()
nums = list(map(int, content.split()))

min_val = min(nums)
last_min_index = 0
for i in range(len(nums) - 1, -1, -1):
    if nums[i] == min_val:
        last_min_index = i
        break

sum_10 = sum(x for x in nums[len(nums) // 2:] if x > 10)

f2 = open('result_8.txt', 'w', encoding="utf-16")
f2.write("Исходные данные:\n")
f2.write(' '.join(map(str, nums)) + '\n')
f2.write("Количество элементов: " + str(len(nums)) + '\n')
f2.write("Индекс последнего минимального элемента: " + str(last_min_index) + '\n')
f2.write("Сумма элементов больших 10 во второй половине: " + str(sum_10) + '\n')
f2.close()
