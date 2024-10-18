import numpy as np

# Datos
X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Y = np.array([15, 11, 13, 7, 9, 6, 5, 2])

# Calcular la media de X y Y
X_mean = np.mean(X)
Y_mean = np.mean(Y)

# Calcular la pendiente (b) y el intercepto (a)
numerator = np.sum((X - X_mean) * (Y - Y_mean))
denominator = np.sum((X - X_mean) ** 2)
b = numerator / denominator
a = Y_mean - b * X_mean

# Imprimir los coeficientes
print(f"Pendiente (b): {b}")
print(f"Intercepto (a): {a}")

# Ecuación de la línea de regresión
print(f"Ecuación de la línea de regresión: Y = {a:.2f} + {b:.2f}X")

# Predecir Y para cada X
Y_pred = a + b * X

# Imprimir los valores predichos
print("Valores predichos de Y:")
for x, y_pred in zip(X, Y_pred):
    print(f"X = {x}, Y_pred = {y_pred:.2f}")

