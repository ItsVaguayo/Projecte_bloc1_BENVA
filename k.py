documento = "clients.txt"
clientsdoc=   open(documento,"a")

#By Victor A.
def ft_extract(documento):
    extract1 = documento.split("\n")
    extract2 = []
    for i in range(len(extract1)):
        extract2.append(extract1[i].split(";"))
    print(extract2)
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
def alta_clients():
        dni = int(input("Introduce el nif sin letra: "))
        dni = str(dni)
        nom = input("Introduce el nombre: ")
        clientsdoc = open("clients.txt","a")
        clientsdoc.write(dni+";" + nom+"\n")
        clientsdoc.close()
def borrar_clientes(clientsdoc):
    clients = open("clients.txt", "a")
    clients4545 = {}
    for clientsdoc in range (clients):
        print(clients4545)


def menu():
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
                ft_extract
            elif menu == 2:
                alta_clients()
            elif menu == 3:
                borrar_clientes()
            else:
                print("Numero invalido")
        except:
            print("Caracter invalido")


ala=menu()
print(ala)