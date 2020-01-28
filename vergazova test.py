import math


# начальные условия
x0 = float(0)
y0 = float(1)
# отрезок [x0, xn], где x0 = 0, xn = 1
b = float(1)
# шаг
h = float((b - x0)/10)



f = lambda x, y: float(y) + float(x)
ilist = range(0, 10, 1)
xlist = [(x0 + h * i) for i in ilist]
ylist = []

prev = y0
print("метод Эйлера")
for x in xlist:
    y = prev + h * f(x, y0)
    prev = float(y)
    ylist.append(prev)
    print("Номер итерации (x): " + str(x) + "  Значение (y): " + str(y))

# массив со значениями точного решения
lst = []
print("\nТочное решение:", )
for x in xlist:
    func = 2 * math.e**x-(x+1) # точное решение
    lst.append(func)
    print("Номер итерации (x): " + str(x) + "  Значение (y): " + str(func))

print(" \n метод Рунге-Кутты четвертого порядка")
# массив со значениями решения метода Рунге-Кутты четвертого порядка
rk4 = []
for x in xlist:
    k1 = f(x, y)
    k2 = f(x+h/2, y + h / 2 * k1)
    k3 = f(x + h / 2, y + h / 2 * k2)
    k4 = f(x + h, y + h * k3)
    prev1 = y0
    yn = prev1 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4) # решение метода Рунге-Кутты четвертого порядка
    rk4.append(yn)
    print("Номер итерации (x): " + str(x) + "  Значение (y): " + str(yn))


