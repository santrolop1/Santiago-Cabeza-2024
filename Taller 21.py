import numpy as np


x = np.array([1, 3, 5, 7, 9, 11, 13])
y = np.array([14.9, 3.6, -2, -3.6, -2.4, 4.4, 14.4])


n = len(x)
sum_x = np.sum(x)
sum_x2 = np.sum(x**2)
sum_x3 = np.sum(x**3)
sum_x4 = np.sum(x**4)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2y = np.sum((x**2) * y)


A = np.array([
    [sum_x4, sum_x3, sum_x2, sum_x2y],
    [sum_x3, sum_x2, sum_x, sum_xy],
    [sum_x2, sum_x, n, sum_y]
], dtype=float)


def gauss_jordan(matriz):
    n = len(matriz)
    for i in range(n):

        matriz[i] = matriz[i] / matriz[i, i]
      
        for j in range(n):
            if i != j:
                matriz[j] = matriz[j] - matriz[j, i] * matriz[i]
    return matriz[:, -1] 


solucion = gauss_jordan(A)
a, b, c = solucion
print("Coeficientes del polinomio:")
print("a =", a)
print("b =", b)
print("c =", c)


y_ajustado = a * x**2 + b * x + c
ss_res = np.sum((y - y_ajustado) ** 2) 
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - (ss_res / ss_tot)
print("Coeficiente de determinación (R^2):", r2)
