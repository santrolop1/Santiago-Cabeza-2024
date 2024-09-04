import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def coseno_taylor(x, es):
    iteracion = 0
    suma = 0
    termino_anterior = 1
    ea = 100  

    while ea > es:
        if iteracion == 0:
            termino = 1
        else:
            termino = ((-1) ** iteracion) * (x ** (2 * iteracion)) / factorial(2 * iteracion)
        
        suma += termino
        
        if termino != 0:
            ea = abs((termino - termino_anterior) / termino) * 100
        
        termino_anterior = termino
        iteracion += 1

    return suma, ea, iteracion

x = float(input("Ingrese el valor en radianes: "))
es = 0.5 * 10**(-8)  
resultado, error, iteraciones = coseno_taylor(x, es)


print(f"\nResultados:")
print(f"Valor estimado de cos({x}): {resultado:.8f}")
print(f"Error aproximado relativo porcentual: {error:.8f}%")
print(f"Número de iteraciones realizadas: {iteraciones}")

cos_real = math.cos(x)
print(f"\nValor real de cos({x}) (usando math.cos): {cos_real:.8f}")
print(f"Error relativo respecto a math.cos: {abs(resultado - cos_real) / cos_real * 100:.8f}%")


