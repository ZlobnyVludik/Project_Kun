# В матрице элементы последней строки заменить на 0.

rows = int(input("Введите кол-во строк: "))

matrix = [list(map(int, input("Введите строку: ").split())) for _ in range(rows)]
    
matrix[-1] = [0 for _ in matrix[-1]]

print("Результат: \n")
for row in matrix:
    print(*row)
