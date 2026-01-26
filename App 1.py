def ft_extract():
    # By Victor A.
    # Esta funcion desarrollada por Victor A. crea una LISTA con los nombres y DNI de cada individuo por separado
    clientsdoc = open("clients.txt", "r")
    clientsdoc = clientsdoc.read()
    extract1 = clientsdoc.split("\n")
    extract2 = []
    for i in range(len(extract1)):
        extract2.append(extract1[i].split(";"))
    return extract2
def ft_alta_clients(clientes_lista):
        dni = input("Introduce el NIF/DNI: ")
        nom = input("Introduce el Nombre: ")
        autorizar_creacion=True

        for cliente in clientes_lista:
                if dni == cliente[0]:
                    print("El DNI", dni,"Ya esta registrado")
                    autorizar_creacion=False
        if autorizar_creacion==True:
                clientsdoc = open("clients.txt","a")
                clientsdoc.write(dni+";" + nom+"\n")
                clientsdoc.close()
                print("El usuario",nom,"a sido agregado")
        else:
            print("Cancelando operacion")
def ft_listar_clients(clientes_lista):
    lista = clientes_lista
    try:
        for x in lista:
            #de la lista, pilla el primer caracter y le da valor a la variable
            if len(x) == 2:
                dni = x[0]
                nombre = x[1]
                print("DNI:",dni,"NOMBRE:",nombre)
        return
    except FileNotFoundError:
        print("Existe un error en el fichero")
def ft_borrar_clientes(clientes_lista):
    dni_borrar = input("Cual es el DNI del usuario a borrar: ")
    nueva_lista = []
    encontrado = False
    for x in clientes_lista:
        if len(x) ==2:
            if x[0] == dni_borrar:
                print("El cliente con DNI", dni_borrar,"ha sido eliminado")
                print("El usuario",x[1],"ha decido abandonar")
                encontrado = True
            else:
                nueva_lista.append(x)
    if encontrado == False:
        print("El cliente con DNI no existe")
        return

    documento= open("clients.txt", "w")
    for cliente in nueva_lista:
            documento.write(cliente[0] + ";" + cliente[1] + "\n")
    documento.close()
    return
def ft_menu():
    while True:
            texto=("""
0- Sortir del programa
1- Mostrar clients existents
2- Alta nou client
3- Esborrar client existent
____________________________""")
            print(texto)
            try:
                menu=int(input("--> "))
                clientes_lista=ft_extract()
                if menu == 0:
                    menu=("""¡ADIOS!""")
                    return (menu)
                elif menu == 1:
                    ft_listar_clients(clientes_lista)
                elif menu == 2:
                    ft_alta_clients(clientes_lista)
                elif menu == 3:
                    ft_borrar_clientes(clientes_lista)
                else:
                    print("Numero invalido")
            except ValueError:
                print("Introduzca un numero no letras")


hola=ft_menu()
print(hola)