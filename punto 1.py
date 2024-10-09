def producto_escalar(n):
    
    vector1 = [float(input(f" ingrese elementos {i+1} de el  vector 1: ")) for i in range(n)]
    vector2 = [float(input(f"ingrese elementos {i+1} de el vector 2: ")) for i in range(n)]

    producto = sum(x*y for x, y in zip(vector1, vector2))

    print(f"el producto escalar es : {producto}")
    
n = int(input("Introduzca la longitud de los vectores: "))

producto_escalar(n)