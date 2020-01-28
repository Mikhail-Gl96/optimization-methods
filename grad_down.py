import math

#  условие выполнения
#  Минимизировать в Е2 функцию
#  f(x1, x2)=α(x2+β-x12)2+(γ-x1)2+δx12→min
#  методом градиентного спуска, завершив вычисления при │∂f(x(k))/∂xi│≤0,05,  i=1, 2.
alpha = 29
betta = 15
gamma = 12
delta = 2
x10 = 2
x20 = 0
acc = 0.001
#  частные производные
dfdx1 = 2 * alpha * (x20 + betta - x10**2) * (-2 * x10) - 2 * (gamma - x10) + 2 * delta * x10
dfdx2 = 2 * alpha * (x20 + betta - x10**2)
def dfdx1(x1,x2):
    pr1=[]



def grad(x10, x20, acc):
    i=0
    x1 = []
    x2 = []
    ak = []
    pr1 = []
    pr2 = []
    f = []
    x1[1] = x10
    x2[i] = x20
    ak[i] = 1
    pr1[i] =
    ans = x1+x2*acc
    return ans

f = lambda x1, x2: alpha * (x2 + betta - x1**2)**2 + (gamma - x1)**2 + delta * x1**2


var = fabs(dfdx)
# параметрический шаг




#  цикл пересчета
while var <= 0.05:
    x1[k+1] = x1[k] - alpha[k] * dfdx1[k]
    x2[k+1] = x2[k] - alpha[k] * dfdx2[k]
#  условие конца программы
if fabs(dfdx) <= 0.05:
    print('Программа выполнена')
else:
    print('Недостаточная точность \nПродолжаем считать')
