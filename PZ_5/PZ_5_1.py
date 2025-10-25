# Составить программу, в которой функцию построит изображение, в котором в первой строке 1 звездочка,
# во второй - 2, в третьей - 3, ..., в строке с номером m — M звездочек.

def print_stars(m):
    try:
        # Проверяем, что m - целое положительное число
        if not isinstance(m, int) or m <= 0:
            raise ValueError("Параметр m должен быть целым положительным числом")
        
        # Выводим звездочки построчно
        for i in range(1, m + 1):
            print('*' * i)
            
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


def main():
    # Основная функция программы
    try:
        # Запрашиваем у пользователя количество строк
        m = int(input("Введите количество строк m: "))
        print_stars(m)
        
    except ValueError:
        print("Ошибка: Введите целое число!")
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


main()
