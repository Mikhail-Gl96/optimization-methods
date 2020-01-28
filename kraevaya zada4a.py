import math

y0 = 0
y2 = 1
a = 0
b = 1
n = 10
h = (float(b) - float(a)) / float(n)
for i in range(1, n):
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    q = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x[i] = 0
    x[i] = x[i] + i * h
    x[0] = a
    x[n] = b
    p[i] = p[x[i]]
    q[i] = q[x[i]]
    f[i] = 0
    y[i] = y[x[i]]

A = alpha0 * y0 + alpha1 * yd(a)
B = betta0 * y2 + betta1 * yd(b)
if fabs(alpha0) + fabs(alpha1) == 0 and fabs(betta0) + fabs(betta1) == 0:
        print(' альфа0 + альфа1 = ' + str(fabs(alpha0) + fabs(alpha1)) + '\nбетта0 + бетта1 = ' + str(fabs(betta0) + fabs(betta1)))
else:
        print('метод прогонки работает, приступаем к решению')


fd = lambda x, y: ydd + y * cosh(x)
# yd -  производная

# проверка альфы и бэтты

# f[i] = (y[i + 2] - 2 * y[i +1] + y[i]) / h**2 + p[i] * (y[i + 1] - y[i]) / h + q[i] * y[i]
for i in range(1, n):
    m[i] = h * p[i] - 2
    n[i] = 1 - h * p[i] + h**2 * q[i]
    f[i] = (y[i + 2] + m[i] * y[i + 1] + n[i] * y[i]) / h**2

A = alpha0 * y0 + alpha1 * (y1 - y0) / n
B = betta0 * y[n] + betta1 * (y[n] - y[n - 1]) / h

# прямой ход
'''m[i] = h * p[i - 2]
n[i] = 1 - h * p[i] + h ** 2 * q[i]'''
c0 = (alpha1 - alpha0 * h) / (m[0] * (alpha1 - alpha0 * h) + n[0] * alpha1)
d0 = (n[0] * A * h) / (alpha1 - alpha0 * h) + f[0] * h**2
for i in range(1, n-1):
    c[i] = 1 / (m[i] - n[i] * c[i-1])
    d[i] = f[i] * h**2 - n[i] * c[i - 1] * d[i-1]

y[n] = (betta1 * c[n - 2] * d[n - 2] + B * h) / (betta1 * (1 + c[n - 2]) + betta0 * h)

# обратный ход
for n in range(0, n):
    y[n - 1] = c[n - 2] * (d[n - 2] - y[n])
    y[n - 2] = c[n - 3] * (d[n - 3] - y[n - 1])
y[1] = c[0] * (d[0] - y[2])
y[0] = (alpha1 * y[1] * A * h) / (alpha1 - alpha0 * h)

for i in range(a, b):
    print("x[" + str(i) + ']  y[' + str(i) + '] = ' + str(y[i]))
