# Se define la funcion que realiza la multiplicacion de matrices
def multiplicacion_matrices(matriz_a, matriz_b):
    # Se calcula cuantas filas y columnas tiene cada matriz.
    filas_a = len(matriz_a)
    filas_b = len(matriz_b)
    columnas_a = len(matriz_a[0])
    columnas_b = len(matriz_b[0])

    # Se revisa que las matrices sean comptibles para multiplicarse.
    if (columnas_a == filas_b):
        # Se crea la matriz 'resultado' con el tamano adecuado y todos sus valores igual a 0.
        resultado = []
        for fila in range(filas_a):
            # Por cada fila de la matriz_a se crea una nueva fila.
            nueva_fila = []
            for columna in range(columnas_b):
                # Por cada columna de la matriz_b se agrega un valor a la fila, se agrega una columna.
                nueva_fila.append(0)
            # Cuando la nueva fila esta completa se agrea a la matriz 'resultado'.
            resultado.append(nueva_fila)

        # Se itera por las filas de matriz_a. 
        for fila_a in range(filas_a):
            # Se itera por las columnas de matriz_b.
            for columna_b in range(columnas_b):
                # Se itera por las filas de matriz_b
                for fila_b in range(filas_b): 
                    # Se multiplican las filas de matriz_a por las columnas de matriz_b y se guarda en 'resultado' con su respectiva posicion.
                    resultado[fila_a][columna_b] += matriz_a[fila_a][fila_b] * matriz_b[fila_b][columna_b]
    
    # Si las matrices no son compatibles se muestra un mensaje de error.
    else:
        print("Las matrices no son compatibles para realizar la operacion.")
        return

    # Fin de la funcion. Se devuelve 'resultado'.
    return resultado


# Se define la funcion que realiza el producto vectorial.
def producto_vectorial(vector_a, vector_b):
    # Se verifica que el tamano de los vectores sea el mismo para poder realizar el producto vectorial.
    if len(vector_a) == len(vector_b):
        # Se calula el producto_cruz entre los 2 vectores.
        producto_cruz = [vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1],
                         vector_a[0] * vector_b[2] - vector_a[2] * vector_b[0],
                         vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]]
         
        # Se suman los elementos del producto_cruz y se guarda en 'resultado'.
        resultado = 0
        for elemento in producto_cruz:
            resultado += elemento

    # Si los vectores no son del mismo tamano se muestra un mensaje de error.
    else:
        print("Los vectores no son compatibles para sacar el producto entre ambos.")
        return 

    # Fin de la funcion. Se devuelve 'resultado'.
    return resultado


# Se define la funcion que realiza la traspuesta de una matriz.
def traspuesta_matriz(matriz):
    # Se calcula el tamano de las filas y columnas de la matriz.
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Se calcula la transpuesta de la matriz y se guarda en la matriz 'resultado'.
    resultado = []
    for columna in range(columnas):
        # Por cada columna de la matriz inicial se crea una nueva fila.
        nueva_fila = [] 
        for fila in range(filas):
            # Cada valor dentro de dicha columna se agrega a la nueva fila.
            nueva_fila.append(matriz[fila][columna])
        # Cuando la fila esta completa se agrega a la matriz 'resultado'.  
        resultado.append(nueva_fila)

    # Fin de la funcion. Se devuelve 'resultado'.
    return resultado


# Se define la funcion que calcula el determinante de una matriz.
def determinante(matriz):
    # Se calcula el tamano de las filas y columna de la matriz.
    filas = len(matriz)
    columnas = len(matriz[0])

    # Caso en el que tenemos una matriz 2x2.
    if filas == 2 and columnas == 2:
        resultado = matriz[0][0]*matriz[1][1] - matriz[1][0]*matriz[0][1]
        return resultado

    # Se inicializa la varible matriz_complemento que nos ayudara al calcular el determinante.
    matriz_complemento = []
    for fila in range(filas):
        # Por cada fila de la matriz inicial se crea una nueva fila.
        nueva_fila = []
        # Necesitamos que los valores dentro de cada fila se repitan 2 veces por lo que agregamos un for i in range(2).
        for i in range(2):
            for columna in range(columnas):
                # Cada valor de la fila se agrega a la nueva fila, como se repiten los valores 2 veces queda asi. Ej: [1, 2, 3, 1, 2, 3]
                nueva_fila.append(matriz[fila][columna])
        # Cuando la fila esta completa se agrega a la 'matriz_complemento'.
        matriz_complemento.append(nueva_fila)
    
    # Se calcula la cantidad de columnas de 'matriz_complemento' y su respectivo medio.
    mitad = columnas
    columnas = 2*mitad

    # Se calcula la primera parte del determinante. Suma de diagonales de izquierda a derecha.
    parte_1 = 0
    # Vamos desde la primera columna hasta la mitad de 'matriz_complemento'.
    for columna in range(mitad):
        elemento = 1
        # Se itera por las filas de 'matriz_complemento'.
        for fila in range(filas):
            # Se multiplican los elementos de la diagonal.
            elemento = elemento * matriz_complemento[fila][fila+columna]
        # Se suma la diagonal a 'parte_1'.
        parte_1 += elemento

    # Se calcula la segunda parte del determinante. Suma de diagonales de derecha a iquierda.
    parte_2 = 0
    # Como queremos ir de derecha a izquierda, es decir de mayor a menor, se cambia como itera el for para que cumpla estos requisitos. Comenzamos desde la penultima columna hasta la mitad de nuestra matriz_complemento y se itera con -1.
    for columna in range(columnas-2, mitad-2, -1):
        elemento = 1
        # Se itera por las filas de 'matriz_complemento'.
        for fila in range(filas):
            # Se multiplican los elementos de la diagonal.
            elemento = elemento * matriz_complemento[fila][columna-fila]
        # Se suma la diagonal a 'parte_2'.
        parte_2 += elemento

    # Se calcula el resultado restando 'parte_1' y 'parte_2'.
    resultado = parte_1 - parte_2
    return resultado

# Se define una funcion para determinar la matriz menor.
def matriz_menor(matriz, fila_saltar, columna_saltar):
    # Se calcula el tamano de las filas y columnas de la matriz.
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Se inicializa la variable 'resultado'.
    resultado = []
    # Iteramos por las filas de la matriz.
    for fila in range(filas):
        # Si la fila es diferente a la fila que nos debemos saltar realizamos las acciones.
        if fila != fila_saltar:
            # Se crea la variable temporal nueva_fila.
            nueva_fila = []
            # Iteramos por las columnas de la matriz.
            for columna in range(columnas):
                # Si la columna es diferente a la columna que nos debemos saltar agregamos el elemento a 'nueva_fila'.
                if columna != columna_saltar:
                    nueva_fila.append(matriz[fila][columna])
            # Cuando ya la fila esta completa se agrega la fila a 'resultado'.
            resultado.append(nueva_fila)

    # Fin de la funcion. Devolvemos 'resultado'.
    return resultado

# Se define la funcion que calcula la inversa de una matriz.
def matriz_inversa(matriz):
    # Primero calculamos el determinante de la matriz.
    det = determinante(matriz)

    # Si el determinante es igual a 0 se muestra un mensaje de error y se termina la funcion.
    if det == 0:
        print("Error! El determinante de la matriz es cero.")
        print("No se puede calcular la inversa de la matriz.")
        return
    
    # Se incializa la variable cofactores
    cofactores = []
    # Se calcula el tamano de las filas y columnas de la matriz.
    filas = len(matriz)
    columnas = len(matriz[0])
    # Iteramos por las filas de la matriz.
    for fila in range(filas):
        # Se incializa la variable nueva_fila.
        nueva_fila = []
        # Iteramos por las columnas de la matriz.
        for columna in range(columnas):
            # Conseguimos la matriz menor dada la fila y columna actual.
            menor = matriz_menor(matriz, fila, columna)
            # Se agrega el valor dado por la formula del cofactor a 'nueva_fila'.
            nueva_fila.append(((-1) ** (fila+columna)) * determinante(menor))
        # Cuando la lista esta completa se agrega a 'cofactores'.
        cofactores.append(nueva_fila)
    
    # Se crea la variable 'inversa'.
    inversa = traspuesta_matriz(cofactores)

    # Iteramos por las filas y columnas de 'inversa'.
    filas = len(inversa)
    columnas = len(inversa[0])
    for fila in range(filas):
        for columna in range(columnas):
            # Se divide cada valor de 'inversa' entre el determinante de la matriz inicial. (Se ulitiza la funcion round() para redondear a 3 decimales el valor obtenido.)
            inversa[fila][columna] =  round(inversa[fila][columna] / det, 3)

    # Fin de la funcion. Devolvemos 'inversa'.
    return inversa

# Se define la funcion que calcula la solucion para un sistema de ecuaciones lineales.
def resolver_sistema_ecuacion(sistema_ecuacion, valores_independientes):
    # Primero se calcula la inversa de 'sistema_ecuacion'.
    inversa = matriz_inversa(sistema_ecuacion)
    # Se multiplica la matriz inversa por los valores independientes del sistema de ecuaciones para obtener el resultado.
    resultado = multiplicacion_matrices(inversa, valores_independientes)

    # Se redondean los valores de 'resultado' para que sean solo 3 decimales.
    for fila in range(len(resultado)):
        for columna in range(len(resultado[0])):
            resultado[fila][columna] = round(resultado[fila][columna], 1)

    # Fin de la funcion. Se devuelve 'resultado'.
    return resultado
