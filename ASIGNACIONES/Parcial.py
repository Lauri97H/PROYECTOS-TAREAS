# Se importa el modulo 'json' para poder trabajar con los archivos .json
import json

# Se crea la variable global 'ruta_archivo' con la que siempre sabemos como se llama el archivo y donde esta para su uso.s
ruta_archivo = 'clase.json'

# Se define la funcion 'agregar_alumno'.
def agregar_alumno():
    # Se crea el diccionario vacio 'alumno'.
    alumno = {}
    # Se agrega 'nombre' y su valor al diccionario.
    alumno['nombre'] = input("Ingrese el nombre del alumno: ")
    # Se agrega 'edad' y su valor al diccionario.
    alumno['edad'] = input("Ingrese la edad del alumno: ")
    # Se agrega 'notas' y sus valores al diccionario.
    alumno['notas'] = input("Ingrese las notas del alumno separadas por espacios: ").strip().split()
    for i in range(len(alumno['notas'])):
        alumno['notas'][i] = int(alumno['notas'][i])
    # Fin de la funcion. Se retorna 'alumno'.
    return alumno

# Se define la funcion 'promedio_notas'.
def promedio_notas(clase):
    # Se crean las variables 'suma_notas' y 'numero_alumnos' que nos ayudaran a calcular el promedio.
    suma_notas = 0
    numero_alumnos = len(clase)
    # Iteramos por cada alumno de 'clase'.
    for alumno in clase:
        # Creamos la variable 'promedio_alumno' y ' cantidad_notas' que nos ayudaran a sacar el promedio individual de cada alumno.
        promedio_alumno = 0
        cantidad_notas = len(alumno['notas'])
        # Iteramos por las notas del alumno.
        for nota in alumno['notas']:
            # Sumamos cada nota a 'promedio_alumno'.
            promedio_alumno += nota
        # Se calcula el promedio del alumno y luego se suma a 'suma_notas'.
        promedio_alumno = promedio_alumno / cantidad_notas
        suma_notas += promedio_alumno

    # Fin de la funcion. Se retorna el promedio de la clase (suma_notas/numero-alumnos).
    return suma_notas / numero_alumnos

# Se define la funcion 'nota_maxima_minima'.
def nota_maxima_minima(clase):
    # Se crean las variables 'maxima' y 'minima'.
    maxima = 0
    # La variable minima se guarda con un numero grande porque se esta buscando el numero mas pequeno de la clase.
    minima = 100000
    # Iteramos por los alumnos de la clase y luego iteramos por las notas de cada alumno.
    for almuno in clase:
        for nota in almuno['notas']:
            # Si la nota es mayor a 'maxima' se reemplaza el valor de 'maxima'.
            if nota > maxima:
                maxima = nota
            # Si la nota es menor a 'minima' se reemplaza el valor de 'minima'.
            if nota < minima:
                minima = nota
            
    # Fin de la funcion. Se retorna una lista con 'maxima' y 'minima'
    return [maxima, minima]

# Se define la funcion 'guardar_datos'.
def guardar_datos(clase):
    # Se abre el archivo .json
    with open(ruta_archivo, 'a') as archivo:
        # Se itera por los alumnos de la clase y se agrega al archivo.
        for alumno in clase:
            json.dump(alumno, archivo, indent=2)
    
    # Fin de la funcion.
    return

# Se crea la variable 'alumnos' que es una lista donde se guardan los alumnos con sus respectivos datos.
alumnos = []
# Se define el menu principal.
while True:
    # Se le muestra al usuario sus posibles acciones y se le pide que seleccione una.
    print("Menu de Acciones\n1. Agregar Alumno\n2. Calcular Promedio de Notas\n3. Obtener Nota Maxima y Minima\n4. Guardar Datos\n5. Salir")
    accion = input("Ingrese el numero de la accion que desea realizar: ")

    # Caso 1: Agregar alumno
    if accion == '1':
        # Se llama a la funcion 'agregar_alumno' y se agrega el resultado a la lista 'alumnos'.
        alumnos.append(agregar_alumno())
        print("Alumno agregado con exito.\n")
    # Caso 2: Calcular promedio de notas.
    elif accion == '2':
        # Se llama la funcion 'promedio_notas' y se guarda el resultado en la variable 'promedio'.
        promedio = promedio_notas(alumnos)
        # Se muestra el resultado en pantalla redondeado a 2 decimales.
        print(f"El promedio de la clase es {promedio:.2f}\n")
    # Caso 3: Obtener nota maxima y minima.
    elif accion == '3':
        # Se llama a la funcion 'nota_maxima_minima' para obtener el resultado y se guarda en la variable 'maxima_minima'.
        maxima_minima = nota_maxima_minima(alumnos)
        # Se muestra el resultado en pantalla.
        print(f"La nota maxima de la clase es {maxima_minima[0]} y la nota minima es {maxima_minima[1]}.\n")
    # Caso 4: Guardar datos.
    elif accion == '4':
        # Se llama al metodo 'guardar_datos'.
        guardar_datos(alumnos)
        print("Datos guardados con exito.\n")
    # Caso 5: Salir.
    elif accion == '5':
        # Si el usuario escoge la opcion 5 nos salimos del bloque 'while', es decir, nos salimos del menu.
        break
    # Caso invalido: Si el usuario coloca cualquier otra cosa que no sea una opcion permitida se le muestra un mensaje de error.
    else:
        print("Accion invalida, intente de nuevo.\n")
