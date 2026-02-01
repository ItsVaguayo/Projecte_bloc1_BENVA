def ft_extract(users):
    extract1 = users.split("\n")
    extract2 = []
    for i in range(len(extract1)):
        extract2.append(extract1[i].split(";"))
    return extract2


def ft_find(list_data, to_find):
    for i in range(len(list_data)):
        for x in range(len(list_data[i])):
            if list_data[i][x] == to_find:
                return list_data[i]
    return 0


def cargar_fichero(nombre):
    try:
        f = open(nombre, "r")
        contenido = f.read().strip()
        f.close()
        if contenido == "":
            return []
        return ft_extract(contenido)
    except:
        return []


def guardar_relaciones(relaciones):
    f = open("relaciones.txt", "w")
    for i in range(len(relaciones)):
        linea = relaciones[i][0] + ";" + relaciones[i][1] + ";" + relaciones[i][2] + "\n"
        f.write(linea)
    f.close()


def existe_relacion(relaciones, nif, codigo):
    for i in range(len(relaciones)):
        if relaciones[i][0] == nif and relaciones[i][1] == codigo:
            return i
    return -1


def mostrar_clientes(clientes):
    for i in range(len(clientes)):
        print(clientes[i][0], "-", clientes[i][1])


def mostrar_productos(productos):
    for i in range(len(productos)):
        print(productos[i][0], "-", productos[i][1])


def asignar_producto(clientes, productos, relaciones):
    nif = input("NIF cliente: ")
    codigo = input("Codigo producto: ")

    if ft_find(clientes, nif) == 0 or ft_find(productos, codigo) == 0:
        print("Cliente o producto no existe")
        return

    if existe_relacion(relaciones, nif, codigo) != -1:
        print("Relacion ya existe")
        return

    precio = input("Precio: ")
    relaciones.append([nif, codigo, precio])
    guardar_relaciones(relaciones)
    print("Producto asignado correctamente")


def borrar_producto_cliente(clientes, productos, relaciones):
    nif = input("NIF cliente: ")
    codigo = input("Codigo producto: ")

    if ft_find(clientes, nif) == 0 or ft_find(productos, codigo) == 0:
        print("Cliente o producto no existe")
        return

    pos = existe_relacion(relaciones, nif, codigo)
    if pos == -1:
        print("Relacion no existe")
        return

    relaciones.pop(pos)
    guardar_relaciones(relaciones)
    print("Relacion eliminada correctamente")


def modificar_precio(clientes, productos, relaciones):
    nif = input("NIF cliente: ")
    codigo = input("Codigo producto: ")

    pos = existe_relacion(relaciones, nif, codigo)
    if pos == -1:
        print("Relacion no existe")
        return

    nuevo_precio = input("Nuevo precio: ")
    relaciones[pos][2] = nuevo_precio
    guardar_relaciones(relaciones)
    print("Precio modificado correctamente")


def mostrar_productos_cliente(clientes, productos, relaciones):
    nif = input("NIF cliente: ")

    if ft_find(clientes, nif) == 0:
        print("Cliente no existe")
        return

    encontrado = False
    for i in range(len(relaciones)):
        if relaciones[i][0] == nif:
            codigo = relaciones[i][1]
            producto = ft_find(productos, codigo)
            print(codigo, "-", producto[1], "-", relaciones[i][2])
            encontrado = True

    if not encontrado:
        print("Este cliente no tiene productos asignados")


def menu():
    clientes = cargar_fichero("clientes.txt")
    productos = cargar_fichero("productos.txt")
    relaciones = cargar_fichero("relaciones.txt")

    opcion = ""
    while opcion != "7":
        print("\n--- MENU APLICACION 3 ---")
        print("1. Mostrar clientes")
        print("2. Mostrar productos")
        print("3. Asignar producto a cliente")
        print("4. Borrar producto a cliente")
        print("5. Modificar precio de producto")
        print("6. Mostrar productos de un cliente")
        print("7. Salir")


        opcion = input("Opcion: ")

        if opcion == "1":
            mostrar_clientes(clientes)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            asignar_producto(clientes, productos, relaciones)
        elif opcion == "4":
            borrar_producto_cliente(clientes, productos, relaciones)
        elif opcion == "5":
            modificar_precio(clientes, productos, relaciones)
        elif opcion == "6":
            mostrar_productos_cliente(clientes, productos, relaciones)
        elif opcion == "7":
            print("Adios!")
        else:
            print("Opcion incorrecta")


menu()
