def TDMA(a,b,c,f):
    a, b, c, f = map(lambda k_list: map(float, k_list), (a, b, c, f))

    alpha = [0]
    beta = [0]
    n = len(f)
    x = [0] * n

    for i in range(n-1):
        alpha.append(-b[i]/(a[i]*alpha[i] + c[i]))
        beta.append((f[i] - a[i]*beta[i])/(a[i]*alpha[i] + c[i]))

    x[n-1] = (f[n-1] - a[n-2]*beta[n-1])/(c[n-1] + a[n-2]*alpha[n-1])

    for i in reversed(range(n-1)):
        x[i] = alpha[i+1]*x[i+1] + beta[i+1]

    return x
A = 0
B = 0
C = 0
F = 0
print('Введите a = ', input(float(A)))
print('Введите b = ', input(float(B)))
print('Введите c = ', input(float(C)))
print('Введите f ( это n) = ', input(float(F)))
TDMA(A, B, C, F)

