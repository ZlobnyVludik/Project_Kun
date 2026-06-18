# В матрице элементы столбца N (N задать с клавиатуры) увеличить в 2 раза.

import random

rows = int(input("Количество строк: "))
columns = int(input("Количество столбцов: "))

matrix = [[random.randint(1, 20) for j in range(columns)] for i in range(rows)]

print("Исходная матрица: ")
for column in matrix:
    print(column)

n = int(input("\nВведите номер столбца: "))

for i in range(columns):
    matrix[i][n - 1] *= 2

print("Измененная матрица: ")
for column in matrix:
    print(column)
