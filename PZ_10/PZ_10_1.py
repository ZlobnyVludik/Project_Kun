# Средствами языка Python сформировать текстовый файл (.txt), содержащий 
# последовательность из целых положительных и отрицательных чисел. Сформировать 
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую 
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Сумма элементов больших 10 во второй половине: 

numbers = [5, -3, 12, 7, -3, 20, 15, 2, 11, -8]   # можно заменить своими

with open("input.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(map(str, numbers)))

with open("input.txt", "r", encoding="utf-8") as f:
    nums = list(map(int, f.read().split()))

# количество элементов
count = len(nums)

# индекс последнего минимального элемента
min_val = min(nums)
last_min_index = len(nums) - 1 - nums[::-1].index(min_val)

# вторая половина списка
second_half = nums[len(nums)//2:]

# сумма элементов > 10 во второй половине
sum_gt10 = sum(x for x in second_half if x > 10)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"Количество элементов: {count}\n")
    f.write(f"Индекс последнего минимального элемента: {last_min_index}\n")
    f.write(f"Сумма элементов > 10 во второй половине: {sum_gt10}\n")

print("Готово. Результат в output.txt")

