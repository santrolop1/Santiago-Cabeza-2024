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
                    print(f"Error: {elemento.strip()} no es un número válido.")
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
        resultado = conjunto1 | conjunto2
    elif operacion == 'intersección':
        resultado = conjunto1 & conjunto2
    elif operacion == 'diferencia':
        resultado = conjunto1 - conjunto2
    elif operacion == 'diferencia simétrica':
        resultado = conjunto1 ^ conjunto2
    return resultado

def main():
    """Función principal que ejecuta el programa."""
    print("Operaciones con Conjuntos")
    
    conjunto1 = solicitar_conjunto("primer conjunto")
    conjunto2 = solicitar_conjunto("segundo conjunto")
    
    operacion = solicitar_operacion()
    resultado = realizar_operacion(conjunto1, conjunto2, operacion)
    
    print(f"\nResultado de la {operacion}: {resultado}")
    print(f"Cardinalidad del conjunto resultante: {len(resultado)}")

if __name__ == "__main__":
    main()
