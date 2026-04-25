# В матрице элементы столбца N (N задать с клавиатуры) увеличить в 2 раза.

rows = int(input("Введите кол-во строк: "))

matrix = []
for i in range(rows):
    row = list(map(int, input("Введите элементы строки (через пробел): ").split()))
    matrix.append(row)

N = int(input("Введите номер стобца: ")) - 1

for row in matrix:
    if N < len(row):
        row[N] *= 2

print("Результат: \n")
for row in matrix:
    print(*row)
    
