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

"""
def clientes_diccionario():
    clients = {}
    try:
          for clientsdoc in range (clientsdoc):
                linea = clientsdoc.strip()
                if linea:
                    nif, nom = linea.split(";")
                    clients[nif] = nom
    except FileNotFoundError:
        print("No existe el fichero")
"""
def ft_alta_clients():
        dni = int(input("Introduce el nif sin letra: "))
        dni = str(dni)
        nom = input("Introduce el nombre: ")
        clientsdoc = open("clients.txt","a")
        clientsdoc.write(dni+";" + nom+"\n")
        clientsdoc.close()

def ft_listar_clients():
    lista = ft_extract()
    try:
        for x in lista:
            #de la lista, pilla el primer caracter y le da valor a la variable
            dni = x[0]
            nombre = x[1]
            print("DNI:",dni,"NOMBRE:",nombre)
        return
    except FileNotFoundError:
        print("Existe un error en el fichero")


"""def ft_borrar_clientes(clientsdoc):
    clients = open("clients.txt", "a")
    clients4545 = {}
    for clientsdoc in range (clients):
        print(clients4545)
"""

def ft_menu():
    while True:
        try:
            texto=("""
0- Sortir del programa
1- Mostrar clients existents
2- Alta nou client
3- Esborrar client existent
____________________________""")
            print(texto)
            menu=int(input("--> "))
            if menu == 0:
                return (menu)
            elif menu == 1:
                ft_listar_clients()
            elif menu == 2:
                ft_alta_clients()
            elif menu == 3:
                #ft_borrar_clientes()
                print("hola")
            else:
                print("Numero invalido")
        except:
            print("Caracter invalido")


ala=ft_menu()
print(ala)