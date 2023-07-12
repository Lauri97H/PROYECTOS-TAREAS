###Solicitar al usuario una cadena de texto y verificar que sea palíndromo
### es decir, que se lea de derecha a izquierda y viceversa) 
###EJERCICIO DE TAREA
###Fecha: Jueves 22 de julio del 2023 

# Se le solicita al usuario que ingrese una palabra
palabra = input('Ingrese una palabra:')

#Se usa la sintaxis: ::-1 , su funcion es invertir el texto
if str(palabra) == str(palabra)[::-1]:
    print('La palabra es palíndromo')
else:
    print('La palabra no es palíndromo')

