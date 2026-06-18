# В матрице элементы последней строки заменить на 0.

import random

rows = int(input("Количество строк: "))
columns = int(input("Количество столбцов: "))

matrix = [[random.randint(1, 20) for a in range(columns)] for i in range(rows)]

print("Исходная матрица: ")
for row in matrix:
    print(row)

matrix[-1] = [0 for _ in matrix[-1]]

print("\nИзмененная матрица: ")
for row in matrix:
    print(row)
