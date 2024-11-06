import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2.2, 3.3, 3.7, 4.0, 4.2, 4.4, 4.5, 4.7])


def modelo_lineal(x, a, b):
    return a * x + b


def modelo_potencias(x, a, b):
    return a * np.power(x, b)


param_lineal, _ = curve_fit(modelo_lineal, x, y)
param_potencias, _ = curve_fit(modelo_potencias, x, y)


y_pred_lineal = modelo_lineal(x, *param_lineal)
y_pred_potencias = modelo_potencias(x, *param_potencias)


plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='black', label='Datos originales')
plt.plot(x, y_pred_lineal, label=f'Modelo Lineal: y={param_lineal[0]:.2f}x + {param_lineal[1]:.2f}', color='blue')
plt.plot(x, y_pred_potencias, label=f'Modelo de Potencias: y={param_potencias[0]:.2f}x^{param_potencias[1]:.2f}', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Regresión Lineal y Modelo de Potencias')
plt.show()
