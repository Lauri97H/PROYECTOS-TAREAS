var1 = input("Introduzca el primer numero: ")
if var1.isnumeric():
    var1 = int(var1)
else:
    print("Error, por favor introduzca un valor numerico.")
    exit()

var2 = input("Introduzca el segundo numero: ")
if var2.isnumeric():
    var2 = int(var2)
else:
    print("Error, por favor introduzca un valor numerico.")
    exit()

print("Resultado:", var1 + var2)
