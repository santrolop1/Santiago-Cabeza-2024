import copy

def imprimirSistema(a, b, etiqueta):
    
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(f"{a[i][j]:8.4f}", end=" ")
        print(f"| {b[i]:8.4f}")
    print()

def gaussJordan(ao, bo):
    
    for i in range(n):
        pivote = a[i][i]
        
        
        if abs(pivote) < 1e-10:
            raise ValueError(f"El pivote en la fila {i+1} es cero. El sistema no tiene solución única")
        for j in range(n):
            a[i][j] /= pivote
        b[i] /= pivote
        imprimirSistema(a, b, f"División en fila {i+1}")

        for k in range(n):
            if i != k:
                valorAux = a[k][i]
                for j in range(n):
                    a[k][j] -= a[i][j] * valorAux
                b[k] -= b[i] * valorAux
        imprimirSistema(a, b, f"Reducción en fila {i+1}")
    
    return b

s
a = [[1, 1, 0], [3, 3, 4], [4, 1, 0]]
b = [2.5, 11.5, 15]

x = gaussJordan(a, b)


print("Solución del sistema:")
for i in range(len(x)):
    print(f"x{i+1} = {x[i]:.4f}")


print("\nVerificación de la solución:")
for i in range(len(b)):
    valorAux = sum(ao[i][j] * x[j] for j in range(len(b)))
    print(f"Ecuación {i+1}: {valorAux:.4f} ≈ {bo[i]} (Error: {abs(valorAux-bo[i]):.2e})")
