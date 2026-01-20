documento = "clients.txt"
clientsdoc=   open(documento,"a")

#By Victor A.
#Esta funcion desarrollada por Victor A. crea una LISTA con los nombres y DNI de cada individuo por separado
def ft_extract():
    clientsdoc = open("clients.txt", "r")
    clientsdoc = clientsdoc.read()
    extract1 = clientsdoc.split("\n")
    extract2 = []
    for i in range(len(extract1)):
        extract2.append(extract1[i].split(";"))
    return (extract2)
def ft_alta_clients(clientes_lista):
        lista=clientes_lista
        dni = input("Introduce el nif sin letra: ")
        nom = input("Introduce el nombre: ")
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


def ft_borrar_clientes(clientsdoc):
    open("clients.txt","r")

    clientes_acuales=clientsdoc

    nif_borrar= input("Cual es el DNI del usuario a eliminar= ")
    for x in clientes_acuales:
        if len(x) == 2:
            if x[0] == nif_borrar:
                print("El DNI del usuario a eliminado es: ",x[0])
                del ("clients.txt"[x])



def ft_menu():
    while True:
       # try:
            texto=("""
0- Sortir del programa
1- Mostrar clients existents
2- Alta nou client
3- Esborrar client existent
____________________________""")
            print(texto)
            menu=int(input("--> "))
            clientes_lista=ft_extract()
            if menu == 0:
                return (menu)
            elif menu == 1:
                ft_listar_clients(clientes_lista)
            elif menu == 2:
                ft_alta_clients(clientes_lista)
            elif menu == 3:
                ft_borrar_clientes(clientes_lista)
            else:
                print("Numero invalido")
        #except:
         #   print("Caracter invalido")


hola=ft_menu()
print(hola)