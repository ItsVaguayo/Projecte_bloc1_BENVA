# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Aplicacio_4.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vaguayo- <vaguayo-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/12 16:36:29 by vaguayo-          #+#    #+#              #
#    Updated: 2026/01/16 17:27:36 by vaguayo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os


def extract(users):
    extract1 = users.split("\n")
    extract2 = []
    for i in range(len(extract1)):
        extract2.append(extract1[i].split(";"))
    return (extract2)


def ft_find(list, to_find):
    for i in range(len(list)):
        for x in range(len(list[i])):
            if list[i][x] == to_find:
                return (list[i])
    return (0)


def login(users):
    count = 0
    nif = input("Si us plau introdueix el teu NIF: ")
    info_users = extract(users)
    user = ft_find(info_users, nif)
    while not user:
        if count > 2:
            print("Error, maxim 3 intents")
            exit(1)
        print(f"Error, tens {3 - count} intents")
        nif = input("Si us plau introdueix el teu NIF: ")
        user = ft_find(info_users, nif)
        count += 1
    return user


def menu():
    opcio = ""
    opciones_validas = ["0", "1", "2", "3", "4"]

    while opcio not in opciones_validas:
        print("\n***********************************")
        print("* MENÚ PRINCIPAL          *")
        print("***********************************")
        print("0- Sortir del programa")
        print("1- Afegir productes a la comanda")
        print("2- Eliminar productes de la comanda")
        print("3- Mostrar comanda")
        print("4- Validar comanda")
        print("***********************************")

        opcio = input("\nSelecciona una opció (0-4): ")

        if opcio not in opciones_validas:
            print("Error: Opció no vàlida")

    return int(opcio)


def aplicacio_4(users, productes):
    if not users and productes:
        return (print("Error"))
    user = login(users)
    print(f"Benvingut a l’aplicació de vendes {user[1]}")
    choice = menu()


users = "5675;victor\n5444;pepe"
productes = "5675;victor\n5444;pepe"
aplicacio_4(users, productes)
if not os.path.exists("/ruta/fitxer"):
    print("Error")