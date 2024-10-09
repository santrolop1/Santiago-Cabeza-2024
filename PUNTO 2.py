def leer_matriz(filas, columnas, nombre):
    
    print(f"Ingrese los elementos de la matriz {nombre} (separados por espacio):")
    matriz = []
    for i in range(filas):
        while True:
            try:
                fila = list(map(int, input(f"Fila {i+1}: ").split()))
                if len(fila) != columnas:
                    raise ValueError(f"La fila debe tener {columnas} elementos enteros válidos.")
                matriz.append(fila)
                break
            except ValueError as e:
                print(f"Error: {e}")
    return matriz

def imprimir_matriz(matriz):
    
    for fila in matriz:
        print(fila)

def multiplicar_por_escalar(matriz, escalar):
   
    return [[elemento * escalar for elemento in fila] for fila in matriz]

def sumar_matrices(A, B):
    
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Las dimensiones de las matrices no coinciden.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrices(A, B):
    
    if len(A[0]) != len(B):
        raise ValueError("El número de columnas de A no es igual al número de filas de B.")
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

def operar_matrices():
    
    while True:
        try:
            filas_A = int(input("Ingrese el número de filas de la matriz A: "))
            columnas_A = int(input("Ingrese el número de columnas de la matriz A: "))
            filas_B = int(input("Ingrese el número de filas de la matriz B: "))
            columnas_B = int(input("Ingrese el número de columnas de la matriz B: "))
            if filas_A <= 0 or columnas_A <= 0 or filas_B <= 0 or columnas_B <= 0:

                raise ValueError("Las dimensiones de las matrices deben ser números enteros positivos.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    A = leer_matriz(filas_A, columnas_A, 'A')
    B = leer_matriz(filas_B, columnas_B, 'B')

    print("\nMatriz A:")
    imprimir_matriz(A)
    print("\nMatriz B:")
    imprimir_matriz(B)

    while True:
        print("\nMenú de operaciones:")
        print("1. 2A")
        print("2. 3B")
        print("3. A + B")
        print("4. A × B")
        print("5. Salir")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            print("\n2A:")
            imprimir_matriz(multiplicar_por_escalar(A, 2))
        elif opcion == "2":
            print("\n3B:")
            imprimir_matriz(multiplicar_por_escalar(B, 3))
        elif opcion == "3":
            try:
                print("\nA + B:")
                imprimir_matriz(sumar_matrices(A, B))
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "4":
            try:
                print("\nA × B:")
                imprimir_matriz(multiplicar_matrices(A, B))
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "5":
            break
        else:
            print("Error: opción inválida.")

if __name__ == "__main__":
    operar_matrices()

    