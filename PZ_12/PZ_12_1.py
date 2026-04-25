# В матрице элементы столбца N (N задать с клавиатуры) увеличить в 2 раза.

rows = int(input("Введите кол-во строк: "))

matrix = [list(map(int, input("Введите строку: ").split())) for _ in range(rows)]

N = int(input("Введите номер стобца: ")) - 1

for row in matrix:
    if N < len(row):
        row[N] *= 2

print("Результат: \n")
for row in matrix:
    print(*row)
