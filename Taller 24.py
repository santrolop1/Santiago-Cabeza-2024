from sympy import symbol, simplify
import sympy as sp

x = symbols('x')


puntos = [(0, 1), (1, 0.9), (2, -1), (3, -2.3), (4, 1.8)]

def lagrange_polynomial(puntos):
    n = len(puntos)
    polinomio = 0
    for i in range(n):
        xi, yi = puntos[i]


        li = 1
        for j in range(n):
            if i != j:
                xj, _ = puntos[j]
                li *= (x - xj) / (xi - xj)

        polinomio += yi * li

    return simplify(polinomio)


polinomio = lagrange(puntos)
print(f"El polinomio de interpolación de Lagrange es: {polinomio}")

valor_en_2_5 = polinomio.subs(x, 2.5)
print(f"El valor del polinomio en x = 2.5 es: {valor_en_2_5}")


print("\nVerificación de puntos de interpolación:")
for xi, yi in puntos:
    valor = polinomio.subs(x, xi)
    print(f"En x = {xi}, L(x) = {valor}, valor esperado = {yi}")



