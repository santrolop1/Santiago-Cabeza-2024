import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2.2, 3.3, 3.7, 4.0, 4.2, 4.4, 4.5, 4.7])


def modelo_exponencial(x, a, b):
    return a * np.exp(b * x)


def modelo_logaritmico(x, a, b):
    return a * np.log(x) + b


param_exponencial, _ = curve_fit(modelo_exponencial, x, y)
param_logaritmico, _ = curve_fit(modelo_logaritmico, x, y)


y_pred_exponencial = modelo_exponencial(x, *param_exponencial)
y_pred_logaritmico = modelo_logaritmico(x, *param_logaritmico)


plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='black', label='Datos originales')
plt.plot(x, y_pred_exponencial, label=f'Modelo Exponencial: y={param_exponencial[0]:.2f}e^{param_exponencial[1]:.2f}x', color='green')
plt.plot(x, y_pred_logaritmico, label=f'Modelo Logarítmico: y={param_logaritmico[0]:.2f}ln(x) + {param_logaritmico[1]:.2f}', color='purple')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Modelo Exponencial y Modelo Logarítmico')
plt.show()
