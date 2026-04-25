# В матрице элементы столбца N (N задать с клавиатуры) увеличить в 2 раза.

matrix = [list(map(int, input().split())) for _ in range(int(input()))]
N = int(input()) - 1

for row in matrix:
    row[N] *= 2

for row in matrix:
    print(row)
