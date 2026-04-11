# В матрице элементы столбца N (N задать с клавиатуры) увеличить в 2 раза.

# Ввод размеров матрицы
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

# Ввод номера столбца N
N = int(input("Номер столбца N: "))

# Ввод матрицы
matrix = [list(map(int, input(f"Строка {i + 1}: ").split())) for i in range(n)]

# Увеличиваем элементы столбца N в 2 раза
matrix = [
    [elem * 2 if j == N - 1 else elem for j, elem in enumerate(row)]
    for row in matrix
]

# Вывод результата
print("Изменённая матрица:")
for row in matrix:
    print(*row)
