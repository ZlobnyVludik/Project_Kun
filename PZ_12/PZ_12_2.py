
# Ввод размеров матрицы
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

# Ввод матрицы
matrix = [list(map(int, input(f"Строка {i + 1}: ").split())) for i in range(n)]

# Последнюю строку заменяем на 0
matrix[-1] = [0 for _ in range(m)]

# Вывод результата
print("Изменённая матрица:")
for row in matrix:
    print(*row)
