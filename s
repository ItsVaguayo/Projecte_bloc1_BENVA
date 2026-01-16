"""
def alta_clients():
    try:
        os.makedirs("clients.txt")
        os.open("clients.txt")
    except:
        os.open("clients.txt")

def menu():
    while True:
        try:
            menu=int(input("0- Sortir del programa 1- Mostrar clients existents 2- Alta nou client 3- Esborrar client existent -->   "))
            if menu == 0:
                return (menu)
            elif menu == 1:
                return (menu)
            elif menu == 2:
                return (menu)
            elif menu == 3:
                return (menu)
            else:
                print("Numero invalido")
        except:
            print("Caracter invalido")


ala=alta_clients()
print(ala)
"""
