#PARCIAL1. Ejercicio 2.
#Realizado por: Maria Jose Vásquez y Laurimar Hernández 


# Se le pide al usuario que ingrese la profundidad del pozo, cuantos metros asciende el caracol durante el dia y cuatros metros resbala en la noche
# Tambien se verifica que los datos ingresados sean validos, si no lo son se le pide al usuario que lo intente de nuevo.
profundidad = 0
while True:
    profundidad = input("Ingrese la profundidad del pozo: ")
    verificar_dato = profundidad.split('.')
    valido = True
    for elemento in verificar_dato:
        if not elemento.isnumeric():
            valido = False
    if valido:
        profundidad = float(profundidad)
        break
    else:
        print("Ingreso un dato invalido, intente de nuevo.")

metros_asciende = 0
while True:
    metros_asciende = input("Ingrese cuantos metros asciende el caracol: ")
    verificar_dato = metros_asciende.split('.')
    valido = True
    for elemento in verificar_dato:
        if not elemento.isnumeric():
            valido = False
    if valido:
        metros_asciende = float(metros_asciende)
        break
    else:
        print("Ingreso un dato invalido, intente de nuevo.")

metros_resbala = 0
while True:
    metros_resbala = input("Ingrese cuantos metros resbala el caracol: ")
    verificar_dato = metros_resbala.split('.')
    valido = True
    for elemento in verificar_dato:
        if not elemento.isnumeric():
            valido = False
    if valido:
        metros_resbala = float(metros_resbala)
        break
    else:
        print("Ingreso un dato invalido, intente de nuevo.")

recorrido = 0
dias = 0

'''
Si los metros que asciende el caracol son menor o igual a los metros que resbala
y la profundidad  del pozo es mayor a los metros que asciende, entonces el caracol
no lograra salir del pozo.
'''
if metros_asciende <= metros_resbala and profundidad > metros_asciende:
    print("El caracol no lograra salir del pozo")
# Si los metros que asciende el caracol son mayor o igual a la profundidad del pozo, el caracol saldra en 1 dia
elif profundidad <= metros_asciende:
    print("El caracol tardo 1 dia en salir del pozo")
# Cualquier otro caso en el que salga el caracol, se calcula cuantos dias se tarda en salir
else:
    while recorrido < profundidad:
        recorrido += metros_asciende
        if recorrido < profundidad:
            recorrido -= metros_resbala
        dias +=1
    print(f"El caracol tardo {dias} dias en salir del pozo")
