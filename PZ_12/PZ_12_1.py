# В матрице элементы столбца N (N задать с клавиатуры) увеличить в 2 раза.

import random

rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))

matrix = [[random.randint(1, 20) for j in range(cols)] for i in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

n = int(input("Введите номер столбца: "))

for i in range(rows):
    matrix[i][n - 1] *= 2

print("Измененная матрица:")
for row in matrix:
    print(row)
    
