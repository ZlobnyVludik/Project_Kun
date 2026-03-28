# В последовательности на n целых элементов найти количество пар,
# для которых произведение элементов делится на 3
# (элементы пары в последовательности являются соседними).

import random

n = int(input("Введите кол-во элементов: "))

nums = [random.randint(-20, 20) for _ in range(n)]

print("Список чисел:", nums)

count = 0

for i in range(len(nums)-1):
    if (nums[i] * nums[i+1]) % 3 == 0:
        count += 1

print("Кол-во пар:", count)
