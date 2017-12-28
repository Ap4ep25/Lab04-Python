from math import sin, cos

res = []

print(" 1 - Вычислить функцию G\n "
      " 2 - Вычислить функцию F\n "
      " 3 - Вычислить функцию Y\n "
      " 0 - Выход из программы \n ")
num1 = float(input('Значение\n'))
if num1 == 0:
    print("До свидания!")
else:
    a = float(input("Введите а: "))

    x_min = float(input("Введите минимальное значение x: "))

    x_max = float(input("Введите макcимальное значение х: "))

    step_c = int(input("Введите число шагов: "))
    step = int

    step = (x_max - x_min) / (step_c - 1)

    x = x_min

    if num1 == 1:
        while x_min <= x_max:
            T = (-10 * a ** 2 + 11 * a * x + 3 * x ** 2)
            if T < 0.000000001:
                print(" Такого значения не существует... ")
            else:
                G = ((-2 * (-5 * (a ** 2) + 3 * a * x_min + 2 * (x_min ** 2))) / T)
                res.append(G)
                print("x =", x, "\tG =", G)
                x_min += step

    elif num1 == 2:
        while x_min <= x_max:
                F = sin(10 * a ** 2 - 7 * a * x + x ** 2)
                res.append(F)
                print("x =", x, "\tF =", F)
                x_min += step
    elif num1 == 3:
        while x_min <= x_max:
            Y = sin(1) / cos(45 * a ** 2 - 79 * a * x + 30 *x ** 2)
            res.append(Y)
            print("x =", x, "\tY =", Y)
            x_min += step

    print("Max.res. = ", max(res))
print("Min.res. = ", min(res))