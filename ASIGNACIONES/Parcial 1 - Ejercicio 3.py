#PARCIAL 1. ejercicio 3.
#Realizado por: Maria Jose Vásquez y Laurimar Hernández 

# Se le pide al usuario que ingrese los dos numeros y se verifica que ambos sean datos validos
n = 0
while True:
    n = input("Ingrese el primer numero: ")
    if n.isnumeric():
        n = int(n)
        break
    else:
        print("Ingreso un dato invalido, intente de nuevo.")

m = 0
while True:
    m = input("Ingrese el segundo numero: ")
    if m.isnumeric():
        m = int(m)
        break
    else:
        print("Ingreso un dato invalido, intente de nuevo.")

# Se declara la variable matriz
matriz = []
# Se itera por cada fila de la matriz 
for i in range(n):
    lista = []
    # Se itera por cada columna
    for j in range(m):
        # Si estamos en una fila de posicion par se llena con los numeros de manera ascendente
        if i%2 == 0:
            lista.append((i*m)+j+1)
        # Si estamos en una fila de posicion impar se llena de manera descendente
        else:
            lista.append((i+1)*m-j)
    # Se agrega la lista a la variable matriz
    matriz.append(lista)

# Se muestra en pantalla el resultado
for i in range(n):
    print(matriz[i])
