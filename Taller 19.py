import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([0.8, 1.2, 1.7, 2.2, 3.2, 4.5])


log_y = np.log(y)


coeficientes = np.polyfit(x, log_y, 1)  
b = coeficientes[0]
A = coeficientes[1]
a = np.exp(A)  


log_y_pred = A + b * x


ss_res = np.sum((log_y - log_y_pred) ** 2)  
ss_tot = np.sum((log_y - np.mean(log_y)) ** 2)  
r_squared = 1 - (ss_res / ss_tot)

y_pred = a * np.exp(b * x)


print(f"El valor de a es: {a:.4f}")
print(f"El valor de b es: {b:.4f}")
print(f"El coeficiente de determinación R^2 es: {r_squared:.4f}")


plt.scatter(x, y, label='Datos originales')
plt.plot(x, y_pred, color='red', label='Ajuste exponencial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
