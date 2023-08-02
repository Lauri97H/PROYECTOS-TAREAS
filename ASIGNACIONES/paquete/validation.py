# Validacion de dato tipo 'int'. (Numero entero)
def valInt(valor, rango=[]):
    validacion = True

    # Bloque try/except para el manejo de los casos que dan errores.
    try:
        # Se verifica que el 2do argumento sea de tipo 'tuple' o 'list'.
        if not isinstance(rango, list) and not isinstance(rango, tuple):
            raise TypeError("TypeError: Tipo no soportado.")
        # Se verifica que el 2do argumento tenga el tamaño correcto y este en orden creciente. 
        elif rango != [] and (len(rango) != 2 or rango[0] > rango[1]):
            raise ValueError("ValueError: Valores incorrectos.")
    except TypeError as error:
        return error
    except ValueError as error:
        return error
    
    # Se verifica que el primer argumento sea del tipo de dato correcto.
    if not isinstance(valor, int):
        validacion = False
    # Se verifica que el 1er argumento este en el intervalo dado por el 2do arrgumento.
    elif rango != [] and (valor < rango[0] or valor > rango[1]):
        validacion = False
    # Se revisa el caso en que el 2do argumento es un 'tuple' y el 1er argumento coincide con alguno de los valores extremos del intervalo.
    elif isinstance(rango, tuple) and (valor == rango[0] or valor == rango[1]):
        validacion = False
    
    return validacion

# Validacion de dato tipo 'float'. (Numero decimal)
def valFloat(valor, rango=[]):
    validacion = True

    # Bloque try/except para el manejo de los casos que dan errores.
    try:
        # Se verifica que el 2do argumento sea de tipo 'tuple' o 'list'.
        if not isinstance(rango, list) and not isinstance(rango, tuple):
            raise TypeError("TypeError: Tipo no soportado.")
        # Se verifica que el 2do argumento tenga el tamaño correcto y este en orden creciente. 
        elif rango != [] and (len(rango) != 2 or rango[0] > rango[1]):
            raise ValueError("ValueError: Valores incorrectos.")
    except TypeError as error:
        return error
    except ValueError as error:
        return error

    # Se verifica que el primer argumento sea del tipo de dato correcto.
    if not isinstance(valor, float):
        validacion = False
    # Se verifica que el 1er argumento este en el intervalo dado por el 2do arrgumento.
    elif rango != [] and (valor < rango[0] or valor > rango[1]):
        validacion = False
    elif isinstance(rango, tuple) and (valor == rango[0] or valor == rango[1]):
        validacion = False

    return validacion

# Validacion de dato tipo 'complex'. (Numero complejo)
def valComplex(valor, rango=[]):
    validacion = True

    # Bloque try/except para el manejo de los casos que dan errores.
    try:
        # Se verifica que el 2do argumento sea de tipo 'tuple' o 'list'.
        if not isinstance(rango, list) and not isinstance(rango, tuple):
            raise TypeError("TypeError: Tipo no soportado.")
        # Se verifica que el 2do argumento tenga el tamaño correcto y este en orden creciente. 
        elif rango != [] and (len(rango) != 2 or rango[0] > rango[1]):
            raise ValueError("ValueError: Valores incorrectos.")
    except TypeError as error:
        return error
    except ValueError as error:
        return error
    
    # Se verifica que el primer argumento sea del tipo de dato correcto.
    if not isinstance(valor, complex):
        return False

    # Se calcula el modulo del numero complejo con |a+bj| = (a^2 + b^2)^1/2.
    conversion = str(valor).split('+')
    conversion[0] = conversion[0].replace('(', '')
    conversion[1] = conversion[1].replace('j)', '')
    valor_1 = int(conversion[0]) ** 2
    valor_2 = int(conversion[1]) ** 2
    # Se guarda el resultado en 'valor_conversion'.
    valor_conversion = (valor_1 + valor_2) ** (1/2)

    # Se verifica que 'valor_convarsion' este en el intervalo dado por el 2do arrgumento.
    if rango != [] and (valor_conversion < rango[0] or valor_conversion > rango[1]):
        validacion = False
    # Se revisa el caso en que el 2do argumento es un 'tuple' y 'valor_conversion coincide con alguno de los valores extremos del intervalo.
    elif isinstance(rango, tuple) and (valor_conversion == rango[0] or valor_conversion == rango[1]):
        validacion = False

    return validacion

# Validacion de dato tipo 'list'. (Lista)
def valList(argumento_1, argumento_2=0, argumento_3=""):
    validacion = True

    try:
        # Se verifica que el 3er argumento sea 'str' y que el 2do argumento sea 'int' o 'list'.
        if not isinstance(argumento_3, str) or (not isinstance(argumento_2, int) and not isinstance(argumento_2, list)):
            raise TypeError("TypeError: Tipo no soportado.")
        # Se verifica que el 3er argumento sea 'len' o 'value'.
        elif argumento_3 != "" and argumento_3 != "len" and argumento_3 != "value":
            raise ValueError("ValueError: Valor incorrecto.")
    except TypeError as error:
        return error
    except ValueError as error:
        return error


    # Se verifica que el 1er argumento sea de tipo 'list'.
    if not isinstance(argumento_1, list):
        validacion = False
    # Se revisa el caso en que el 3er argumento es igual a 'value' y el 2do argumento sea de tipo 'list' y sea igual al 1er argumento.
    elif argumento_3 != "" and argumento_3 == "value" and (not isinstance(argumento_2, list) or argumento_1 != argumento_2):
        validacion = False
    # Se revisa el caso en que el 3er argumento es igual a 'len' y el 2do argumento sea de tipo 'int' y sea igual al tamaño del 1er argumento.
    elif argumento_3 != "" and argumento_3 == "len" and (not isinstance(argumento_2, int) or len(argumento_1) != argumento_2):
        validacion = False

    return validacion
