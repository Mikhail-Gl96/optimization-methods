import math
# import matplotlib.pyplot as plt
# from matplotlib import mlab

# начальные условия
x0 = float(1)
y0 = float(0.69314718056)
# отрезок [x0, b], где x0 = 1, b = 2
b = float(2)
# шаг
h = float((b - x0)/10)


f = lambda x, y: math.e**(float(y)/float(x))
ilist = [0, 10, 1]
print(ilist)
xlist = [(x0 + h * i) for i in ilist]
ylist = []

prev = y0
print("метод Эйлера")
for x in xlist:
    y = prev + h * f(x, y0)
    prev = y
    ylist.append(prev)
    print("Номер итерации (x): " + str(x) + "  Значение (y): " + str(y))

# массив со значениями точного решения
lst = []
print("\nТочное решение:", )
func = y0
for x in xlist:
    print("func=  " + str(func))
    func = math.e**(float(func)/x)  # точное решение

    lst.append(func)
    print("Номер итерации (x): " + str(x) + "  Значение (y): " + str(func))


print(" \n метод Рунге-Кутты четвертого порядка")
# массив со значениями решения метода Рунге-Кутты четвертого порядка
rk4 = []
yn = y0
for x in xlist:
    k1 = f(x, yn)
    print("y в подстановке сейчас=  " + str(yn))
    print("k1=  " + str(k1))
    k2 = f(x + h / 2, yn + h / 2 * k1)
    print("k2=  " + str(k2))
    k3 = f(x + h / 2, yn + h / 2 * k2)
    print("k3=  " + str(k3))
    k4 = f(x + h, yn + h * k3)
    print("k4=  " + str(k4))
    yn = yn + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4) # решение метода Рунге-Кутты четвертого порядка
    rk4.append(yn)
    print("Номер итерации (x): " + str(x) + "  Значение (y): " + str(yn))



print(" \n метод Адамса-Башфорта")
   # массив со значениями решения метода Адамса-Башфорта
ab4 = []
print("y0=  " + str(y0) + "\ny1= " + str(rk4[0]) + "\ny2= " + str(rk4[1]) + "\ny3= " + str(rk4[2]))
 #  i1list = mlab.frange(0, 3, 1)
falist = [0, 0, 0, 0]
xnlist = []
y1 = rk4[0]
y2 = rk4[1]
y3 = rk4[2]
y4 = rk4[3]
yx = [y1, y2, y3, y4]
yy = [rk4[0], rk4[1], rk4[2], rk4[3]]
x4 = x0 + h * 4
alist = mlab.frange(4, 10, 1)
xalist = [(x0 + h * i) for i in alist]
print(" x3 =  " + str(x4))
xa = [x0, x0 + h * 1, x0 + h * 2, x0 + h * 3, x4]
xxlist = xa + xalist
xxlist.remove(1.4)
print("xxlist = " + str(xxlist))

for x in xalist:
        # falist[x] = x + yx[x]9
        falist[0] = xa[0] + yx[0]
        falist[1] = xa[1] + yx[1]
        falist[2] = xa[2] + yx[2]
        falist[3] = xa[3] + yx[3]

        df3 = falist[3] - falist[2]
        d2f3 = falist[3] - 2 * falist[2] + falist[1]
        d3f3 = falist[3] - 3 * falist[2] + 3 * falist[1] - falist[0]
        ya = yx[3] + h * falist[3] + h ** 2 * df3 / 2 + 5 * h ** 3 * d2f3 / 12 + 3 * h ** 4 * d3f3 / 8

        #  print("F0= " + str(falist[0]) + "\nF1= " + str(falist[1]) + "\nF2= " + str(falist[2]) + "\nF3= " + str(falist[3]))
        z2 = xa[1]
        z3 = xa[2]
        z4 = xa[3]
        xa[3] = x
        xa[2] = z4
        xa[1] = z3
        xa[0] = z2

        w2 = yx[1]
        w3 = yx[2]
        w4 = yx[3]
        yx[3] = ya
        yx[2] = w4
        yx[1] = w3
        yx[0] = w2
        ab4.append(ya)
        print("Номер итерации (x): " + str(x) + "  Значение (y): " + str(ya))
abb4 = yy + ab4
print("abb4 = " + str(abb4))
"""
plt.rc('font', **{'family': 'verdana'})
plt.xlabel("ось абцисс")
plt.ylabel("ось ординат")
plt.plot(xlist, ylist, "b-", label="метод Эйлера")
plt.plot(xlist, lst, "g-", label="точное решение")
plt.plot(xlist, rk4, "r-", label="Рунге-Кутты четвертого порядка")
plt.plot(xxlist, abb4, "y-", label="Адамс Башфорт 4 порядка")
plt.legend()
plt.grid()
plt.show()
"""