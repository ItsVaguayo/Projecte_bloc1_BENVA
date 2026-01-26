# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Aplicacio_4.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vaguayo- <vaguayo-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/12 16:36:29 by vaguayo-          #+#    #+#              #
#    Updated: 2026/01/26 17:56:13 by vaguayo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import libft

def tryRead():
    try:
        f_user = open('clients.txt', 'r')
        usuaris = f_user.read()
        f_user.close()

        f_prod = open('productes.txt', 'r')
        productes = f_prod.read()
        f_prod.close()

        return usuaris, productes

    except FileNotFoundError as e:
        # e.filename guarda la infirmacio del fitxer que ha fallat, super util!!
        print(f"Error: Falta el fitxer obligatori -> {e.filename}")
        return None, None
    except Exception as e:
        # Captura qualsevol altre error inesperat
        print(f"S'ha produit un error inesperat: {e}")
        return None, None

     
def login(users):
    count = 0
    nif = input("Si us plau introdueix el teu NIF: ")
    info_users = libft.ft_extract(users)
    user = libft.ft_find(info_users,nif)
    while not user:
            if count > 2:
                print("Error, maxim 3 intents")
                return None
            print(f"Error, tens {3 - count } intents")
            nif = input("Si us plau introdueix el teu NIF: ")
            user = libft.ft_find(info_users,nif)
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

def ft_find_index(list, to_find):
    if not list:
        return (None)
    for i in range(len(list)):
        for x in range(len(list[i])):
            if list[i][x] == to_find:
                return (i)
    return (None)

def addProduct(productes, cistell):
    id = input("Introdueix el codi del producte que vols afegir a la teva cistella: \n")
    info_productes = libft.ft_extract(productes)
    producte = libft.ft_find(info_productes,id)
    
    if not producte:
        print("Error: No se ha trobat el producte\n")
        return (None)
    quantitat = int(input("Intrueix la quantitat que vols del producte: "))
    index = ft_find_index(cistell,producte[0])
    if index:
        quantitat += int(cistell[index][1])
        cistell[index][1] = str(quantitat)
    else:
        cistell.append([id,quantitat,producte[1],producte[2]])
    showCistella(cistell)
    return(cistell)
    
def showCistella(cistella):
    if not cistella:
        print("La teva cistella esta buida...\n")
        return 
    print("\n***********************************")
    print("* CISTELL                   *")
    print("***********************************")
    print("*  Codi  *  Quantitat  *  Preu  *  Total  *")
    print("\n***********************************")
    for i in range(len(cistella)):
        print(f"*  {cistella[i][0]}  *  {cistella[i][1]}  *  {cistella[i][2]}  *  {(int(cistella[i][1]) * int(cistella[i][2]))}  *")
        print("\n***********************************")
def aplicacio_4():
    usuaris, productes = tryRead()
    choice = 1
    cistella = []
    
    if usuaris is None:
        print("Error")
        return (-1)
    
    user = login(usuaris)
    
    print(f"Benvingut a l’aplicació de vendes {user[1]}")
    while (choice != 0):
        choice = menu()
        match choice:
            case 0:
                print(f"Sortint del programa. Que tinguis un bon dia {user}!")
            case 1:
                cistella = addProduct(productes,cistella)

aplicacio_4()