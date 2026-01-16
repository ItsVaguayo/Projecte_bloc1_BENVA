# Nombre del fichero donde se guardan los clientes
FICHERO = "clients.txt"

# Asegurarse de que el fichero exista
with open(FICHERO, "a", encoding="utf-8"):
    pass  # solo crea el archivo vacío si no existe


def carregar_clients():
    """Carga los clientes desde el fichero y los devuelve en un diccionario"""
    clients = {}
    try:
        with open(FICHERO, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    nif, nom = linea.split(";")
                    clients[nif] = nom
    except FileNotFoundError:
        # Si el fichero no existe, empezamos sin clientes
        pass
    return clients


def guardar_clients(clients):
    """Guarda todos los clientes en el fichero"""
    with open(FICHERO, "w", encoding="utf-8") as f:
        for nif, nomb in clients.items():
            f.write(f"{nif};{nomb}\n")


def mostrar_clients(clients):
    """Muestra todos los clientes por pantalla"""
    if not clients:
        print("No hay clientes registrados.")
    else:
        print("\nClientes existentes:")
        for nif, nomb in clients.items():
            print(f"NIF: {nif} - Nombre: {nomb}")


def alta_client(clients):
    """Da de alta un nuevo cliente"""
    nif = input("Introduce el NIF del cliente: ").strip()
    if nif in clients:
        print("Error: ya existe un cliente con ese NIF.")
        return

    nombre = input("Introduce el nombre del cliente: ").strip()
    clients[nif] = nombre
    guardar_clients(clients)
    print("Cliente dado de alta correctamente.")


def borrar_client(clients):
    """Borra un cliente existente"""
    nif = input("Introduce el NIF del cliente a borrar: ").strip()
    if nif not in clients:
        print("Error: el cliente no existe.")
        return

    del clients[nif]
    guardar_clients(clients)
    print("Cliente borrado correctamente.")


def menu():
    """Muestra el menú principal"""
    print("\n--- MENÚ ---")
    print("0 - Salir del programa")
    print("1 - Mostrar clientes existentes")
    print("2 - Alta nuevo cliente")
    print("3 - Borrar cliente existente")


def main():
    clients = carregar_clients()

    while True:
        menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            print("Saliendo del programa...")
            break
        elif opcion == "1":
            mostrar_clients(clients)
        elif opcion == "2":
            alta_client(clients)
        elif opcion == "3":
            borrar_client(clients)
        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Programa principal
main()
