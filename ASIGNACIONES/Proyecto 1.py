#PROYECTO 1. 
#REALIZADO POR: MARIA JOSE VÁSQUEZ Y LAURIMAR HERNÁNDEZ

inventario = {}
lista_compra = []
while True:
    print("Acciones Disponibles \n\
    1. Registrar producto \n\
    2. Realizar compra \n\
    3. Salir")
    accion = input("Ingrese el numero de la accion a realizar: ")

    # Accion 1: Registro de nuevo producto
    if accion == '1':
        # Se inicializan las variables de nombre, precio y cantidad del producto que se va a registrar
        nombre_producto = ""
        precio_producto = 0
        cantidad_producto = 0

        # Se guarda el nombre del nuevo producto
        registro_nombre = True
        while registro_nombre:
            # El '.lower()' se coloca en el input para que todas las letras de la entrada del usuario esten en minuscula 
            nombre_producto = input("Ingrese el nombre del producto a registrar: ").lower()
            while True:
                verificar = input("Seguro que desea guardar el nombre del producto? (s/n): ").lower()
                if verificar == "s":
                    registro_nombre = False
                    break
                elif verificar == "n":
                    break
                else:
                    print("Opcion erronea intente de nuevo")

        # Se guarda el precio del nuevo producto
        registro_precio = True
        while registro_precio:
            precio_producto = input("Ingrese el precio del nuevo producto: ")

            # Se verifica que el precio que ingreso el usuario sea un valor numerico valido
            verificar_precio = precio_producto.split('.')
            valido = True
            for elemento in verificar_precio:
                if not elemento.isnumeric():
                    valido = False
            # Si el valor de precio es valido se convierte a float y se guarda
            if valido:
                precio_producto = float(precio_producto)
                while True:
                    if precio_producto > 0.00:
                        verificar = input("Seguro que desea guardar el precio? (s/n): ").lower()
                        if verificar == "s":
                            registro_precio = False
                            break
                        elif verificar == "n":
                            break
                        else:
                            print("Opcion erronea intente de nuevo")
                    else:
                        print("No puede ingresar un precio negativo")
                        break
            # Si el valor de precio no es valido se le pide al usuario que intente de nuevo
            else:
                print("El valor que introdujo no es valido, intente de nuevo")

        # Se guarda la cantidad del nuevo producto disponible
        registro_cantidad = True
        while registro_cantidad:
            cantidad_producto = input("Ingrese la cantidad del nuevo producto: ")
            # Se verifica que el valor de cantidad que ingreso el usuario sea valido
            if cantidad_producto.isnumeric():
                cantidad_producto = int(cantidad_producto)
                while True:
                    if cantidad_producto >  0:
                        verificar = input("Seguro que desea guardar la cantidad? (s/n): ").lower()
                        if verificar == "s":
                            registro_cantidad = False
                            break
                        elif verificar == "n":
                            break
                        else:
                            print("Opcion erronea intente de nuevo")

                    else:
                        print("Cantidad ingresada erronea, intente de nuevo")
                        break
            # Si el valor no es valido se le pide al usuario que intente de nuevo
            else:
                print("El valor que introdujo no es valido, intente de nuevo")
        
        producto = {
            "nombre": nombre_producto,
            "precio": precio_producto,
            "cantidad": cantidad_producto
        }

        # Se agrega el nuevo producto al inventario
        inventario[nombre_producto] = producto
        print("Producto registrado con exito.\n")

    # Accion 2: Realizar compra de un cliente
    elif accion == '2':
        # Se muestran los productos disponibles en el momento
        print("Los productos disponibles son:")
        for producto in inventario:
            print(producto)

        realizar_compra = True
        while realizar_compra:
            nombre_comprar = input("Indique el nombre del producto a comprar: ").lower()

            # Se verifica que el producto este en el inventario
            if nombre_comprar in inventario:
                print("Producto selecionado tiene un precio de: ", inventario[nombre_comprar]["precio"] , "$")
                print("Producto selecionado tiene una cantidad de unidades disponibles: " , inventario[nombre_comprar]["cantidad"])
                
                # Aqui se verifica la cantidad de productos y luego mandar a lista_compra
                verificar_cantidad = True
                while verificar_cantidad:
                    while True:
                        cantidad_comprar = input("Indique la cantidad de unidades que desea: ")
                        # Se verifica que el valor que ingreso el usuario sea valido
                        if cantidad_comprar.isnumeric():
                            cantidad_comprar = int(cantidad_comprar)
                            break
                        else:
                            print("El valor que introdujo no es valido, intente de nuevo")

                    # Si la cantidad que se desea comprar esta disponible, y no es negativa, se agrega el producto a la lista_compra
                    if cantidad_comprar <= inventario[nombre_comprar]["cantidad"] and cantidad_comprar > 0 :
                        producto_comprar = {
                            "nombre" : nombre_comprar,
                            "cantidad": cantidad_comprar,
                            "precio" : inventario[nombre_comprar]["precio"]
                        }

                        # Se resta  del inventario la cantidad de producto que se compro
                        inventario[nombre_comprar]["cantidad"] -= cantidad_comprar

                        # Se agrega el producto a la lista de compras
                        lista_compra.append(producto_comprar)   
                        verificar_cantidad = False

                        # Aqui se le pregunta al usuario si desea agregar otro producto a la lista
                        while True:
                            agregar_producto = input("Desea agregar otro producto a la compra? (s/n): ").lower()
                            if agregar_producto == "s":
                                print("Los productos disponibles son")
                                for producto in inventario:
                                    print(producto)
                                break 
                            
                            # Si el usuario escoge no seguir agregando productos se procesa la compra
                            elif agregar_producto == "n":
                                print("Procesando su compra")
                                total = 0
                                for producto in lista_compra:
                                    total += producto["cantidad"] * producto["precio"]
                                print("Total a pagar por su compra" , total, "$ ")
                                print("Compra realizada\n")
                                realizar_compra = False
                                lista_compra = []
                                break

                            # Si el usuario coloca una entrada invalida se le pide que lo haga de nuevo
                            else:
                                print("Ingreso un valor invalido")

                    # Si el usuario coloca una cantidad no disponible de producto se le pide que introduzca otra cantidad
                    elif cantidad_comprar > inventario[nombre_comprar]["cantidad"]:
                        print("La cantidad de unidades que pide excede lo disponible en el inventario.")
                        menos_cantidad = input("Desea llevar menos cantidad? (s/n): ")
                        if menos_cantidad == "s":
                            print("El producto selecionado tiene una cantidad de unidades disponibles: ", inventario[nombre_comprar]["cantidad"])

                        # Si el usuario no desea el producto se le da la opcion de comprar otro
                        elif menos_cantidad == "n":
                            while True:
                                opcion = input("Desea agregar otro producto a la compra? (s/n): ")
                                if opcion == 's':
                                    verificar_cantidad = False
                                    break
                                elif opcion == 'n':
                                    if lista_compra == []:
                                        print("Compra finalizada.\n")
                                    else:
                                        print("\nProcesando su compra")
                                        total = 0
                                        for producto in lista_compra:
                                            total += producto["cantidad"] * producto["precio"]
                                        print("Total a pagar por su compra:" , total, "$ ")
                                        print("Compra realizada.\n")

                                    verificar_cantidad = False
                                    realizar_compra = False
                                    lista_compra = []
                                    break
                                else:
                                    print("Ingreso un opcion invalida, intente de nuevo.")

                    # Si el usuario coloca un cantidad negativa se le pide que lo repita
                    else:
                        print("Ingreso un valor invalido, intente de nuevo")
            
            # Si el producto no esta en el inventario se le da la opcion al usuario de comprar otro
            else:
                print("Ingreso un producto no existente en la tienda")
                while True:
                    agregar_producto = input("Desea agregar otro producto a la compra? (s/n): ").lower()
                    if agregar_producto == "s":
                        print("Los productos disponibles son:")
                        for producto in inventario:
                            print(producto)
                        break
                    # Si el usuario no desea comprar mas se procesa y termina la compra
                    elif agregar_producto == "n":
                        if lista_compra == []:
                                print("Compra finalizada.\n")
                        else:
                            for producto in lista_compra:
                                total = 0
                                total += producto["cantidad"] * producto["precio"]
                            print("Total a pagar por su compra" , total, "$ ")
                            print("Compra realizada.\n")
                            realizar_compra = False
                            lista_compra = []
                        break
                    else:
                        print("Ingreso una opcion invalida, intente de nuevo.")

    # Accion 3: Salir del programa
    elif accion == '3':
        print("Cerrando aplicacion")
        break

    # Si el usuario coloca una opcion invalida se le pide que lo intente de nuevo
    else:
        print("El numero de la accion no existe, intente de nuevo\n")
