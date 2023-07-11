###Solicitar al usuario una cadena de texto y que se imprima invertida 
###EJERCICIO HECHO EN CLASE. 
###Fecha: Jueves 22 de julio del 2023 

acu = ''
palabra = input ('Ingrese una palabra')
for i in range(len(palabra)):
    print(palabra[i])
    acu = palabra [i] + acu
print(acu)


###Uso de la funcion Reverse() para invertir una cadena de caracteres 
###EJERCICIO DE TAREA.
 
#Se le pide al usuario que ingrese una palabra
palabra = input('Ingrese una palabra:')

# Se usa el metodo de la cadena de caracteres: ' '.join , este concatena todos los elementos de la lista 
# dejando un espacio entre ellos
# La funcion reverse( ) invierte la palabra que el usuario ingrese 

palabra_invertida = ' '.join(reversed(palabra))
print(palabra_invertida)
