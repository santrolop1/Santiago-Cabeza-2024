import numpy as np
from sklearn.linear_model import LinearRegression

# Datos proporcionados
x1 = np.array([1, 1, 2, 3, 1, 2, 3, 3])
x2 = np.array([0, 0.5, 0.5, 1, 1, 1.5, 1.5, 0.5])
y = np.array([1.2, 4, 0.2, 0.6, 4.5, 4.6, 1.5, -2])

# Matriz X de variables independientes
X = np.column_stack((x1, x2))

# Ajuste del modelo de regresión lineal
model = LinearRegression().fit(X, y)

# Coeficientes del modelo
coef = model.coef_
intercept = model.intercept_

# Cálculo del coeficiente de correlación
y_pred = model.predict(X)
correlation_matrix = np.corrcoef(y, y_pred)
correlation_coefficient = correlation_matrix[0, 1]

# Resultados
print("Ecuación ajustada: y = {:.2f} + {:.2f} * x1 + {:.2f} * x2".format(intercept, coef[0], coef[1]))
print("Coeficiente de correlación (r):", correlation_coefficient)
