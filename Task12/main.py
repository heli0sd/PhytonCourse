# Ввод суммы S и произведения P
S = int(input("Введите сумму чисел (S): "))
P = int(input("Введите произведение чисел (P): "))

X, Y = None, None

for X in range(1, 1001):
    Y = S - X
    if Y > 0 and Y <= 1000 and X * Y == P:
        break

if X <= 1000 and Y <= 1000:
    print("Числа, которые задумал Петя: X =", X, "и Y =", Y)
else:
    print("Невозможно определить числа X и Y по заданным подсказкам.")