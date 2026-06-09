# В последовательности на n целых элементов найти количество пар,
# для которых произведение элементов делится на 3
# (элементы пары в последовательности являются соседними).

from random import randint

n = int(input('n = '))

a = [randint(-20, 20) for _ in range(n)]

pairs = list(zip(a, a[1:]))
count = sum(1 for x, y in pairs if (x * y) % 3 == 0)

print('Последовательность:', a)
print('Количество пар:', count)
