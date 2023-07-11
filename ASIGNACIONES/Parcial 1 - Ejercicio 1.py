#PARCIAL1. Ejercicio 1.
#Realizado por: Maria Jose Vásquez y Laurimar Hernández 


# Primero se le dan 3 oportunidades al usuario para ingresar un numero de 4 digitos
numero = 0
for i in range(3):
    # Se verifica primero que el numero sea un dato valido
    while True:
        numero = input("Introduzca numero de 4 digitos o mas: ")
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print("Ingreso un dato invalido, intente de nuevo.")

    # Aqui se verifica que el numero sea de 4 digitos exactamente
    if numero >= 1000 and numero <= 9999:
        break
    else:
        print("Numero incorrecto, intente de nuevo")

# Luego se realiza el procedimiento de obtener los numeros aleatorios 3 veces
for i in range(3):
    cuadrado = numero * numero
    # Se muestra en pantalla el numero elevado al cuadrado
    print("Numero al cuadrado:", cuadrado)
    if cuadrado > 0:
        # Se pasa el cuadrado a string para asi poder obtener los 4 caracteres del medio
        numero = str(cuadrado)[2:6]
        # Se convierten esos 4 caracteres a numero entero para poder seguir realizando la operacion
        numero = int(numero)
    else:
        # Si por algun motivo el cuadrado da 0 pues decimos directamente que el numero es 0
        numero = 0
    # Se muestra en pantalla el nuevo numero aleatorio (Los 4 digitos del medio del numero al cuadrado)
    print("4 digitos del medio:", numero)
