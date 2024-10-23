import numpy as np
import matplotlib.pyplot as plt


X = np.array([1, 2, 3, 4, 5, 6, 7])
Y = np.array([0.1, 0.3, 0.9, 1.7, 2.8, 4.5, 6.9])


n = len(X)

X_mean = np.mean(X)
Y_mean = np.mean(Y)


numerador = np.sum((X - X_mean) * (Y - Y_mean))
denominador = np.sum((X - X_mean) ** 2)
b = numerador / denominador
a = Y_mean - b * X_mean


Y_pred = a + b * X


sy = np.std(Y, ddof=1)


s_yx = np.sqrt(np.sum((Y - Y_pred)**2) / (n - 2))


SSR = np.sum((Y_pred - Y_mean)**2)
SST = np.sum((Y - Y_mean)**2)
r_squared = SSR / SST


r = np.sqrt(r_squared)

print(f"Pendiente (b): {b:.4f}")
print(f"Intercepto (a): {a:.4f}")
print(f"Ecuación de la línea de regresión: Y = {a:.4f} + {b:.4f}X")
print(f"Desviación estándar (sy): {sy:.4f}")
print(f"Error estándar de la estimación (s Τ y x): {s_yx:.4f}")
print(f"Coeficiente de determinación (r²): {r_squared:.4f}")
print(f"Coeficiente de correlación (r): {r:.4f}")


print("\nValores predichos de Y:")
for x, y_pred in zip(X, Y_pred):
    print(f"X = {x}, Y_pred = {y_pred:.4f}")


print("\nTabla de valores:")
print("X\tY_real\tY_pred")
for x, y_real, y_pred in zip(X, Y, Y_pred):
    print(f"{x}\t{y_real:.4f}\t{y_pred:.4f}")


plt.scatter(X, Y, color='blue', label='Datos reales')
plt.plot(X, Y_pred, color='red', label='Línea de regresión')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión Lineal')
plt.legend()
plt.show()