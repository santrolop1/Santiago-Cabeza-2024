def solicitar_conjunto(nombre_conjunto):
    """Solicita al usuario los elementos de un conjunto."""
    conjunto = set()
    while True:
        entrada = input(f"Ingrese los elementos del {nombre_conjunto} separados por comas: ").strip()
        if entrada:
            elementos = entrada.split(',')
            for elemento in elementos:
                try:
                    conjunto.add(float(elemento.strip()))
                except ValueError:
                    print(f"Error: '{elemento.strip()}' no es un número válido.")
            break
        else:
            print("La entrada no puede estar vacía. Intente nuevamente.")
    return conjunto

def solicitar_operacion():
    """Solicita al usuario la operación que desea realizar."""
    operaciones = {'unión', 'intersección', 'diferencia', 'diferencia simétrica'}
    while True:
        operacion = input("¿Qué operación desea realizar? (unión, intersección, diferencia, diferencia simétrica): ").strip().lower()
        if operacion in operaciones:
            return operacion
        else:
            print("Operación no válida. Intente nuevamente.")

def realizar_operacion(conjunto1, conjunto2, operacion):
    """Realiza la operación entre dos conjuntos."""
    if operacion == 'unión':
        return conjunto1 | conjunto2
    elif operacion == 'intersección':
        return conjunto1 & conjunto2
    elif operacion == 'diferencia':
        return conjunto1 - conjunto2
    elif operacion == 'diferencia simétrica':
        return conjunto1 ^ conjunto2

def main():
    """Función principal que ejecuta el programa."""
    print("Operaciones con Conjuntos")
    
    # Solicitar elementos para el primer conjunto
    cantidadA = int(input("Cantidad de elementos del conjunto A: "))
    conjuntoA = set()
    for i in range(cantidadA):
        while True:
            try:
                elemento = float(input(f"Elemento {i + 1} para el conjunto A: "))
                conjuntoA.add(elemento)
                break
            except ValueError:
                print("Error: El valor ingresado no es un número válido.")
    
    print("A =", conjuntoA)
    
    # Solicitar elementos para el segundo conjunto
    cantidadB = int(input("Cantidad de elementos del conjunto B: "))
    conjuntoB = set()
    for i in range(cantidadB):
        while True:
            try:
                elemento = float(input(f"Elemento {i + 1} para el conjunto B: "))
                conjuntoB.add(elemento)
                break
            except ValueError:
                print("Error: El valor ingresado no es un número válido.")
    
    print("B =", conjuntoB)

    # Solicitar operación
    operacion = solicitar_operacion()
    
    # Realizar la operación y mostrar el resultado
    resultado = realizar_operacion(conjuntoA, conjuntoB, operacion)
    
    print(f"\nResultado de la {operacion}: {resultado}")
    print(f"Cardinalidad del conjunto resultante: {len(resultado)}")

if __name__ == "__main__":
    main()
