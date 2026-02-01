# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Aplicacio_4.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vaguayo- <vaguayo-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/12 16:36:29 by vaguayo-          #+#    #+#              #
#    Updated: 2026/02/01 21:04:12 by vaguayo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import libft
from datetime import datetime

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
        # e.filename guarda la infirma # e.filename guarda la informacio del fitxer que ha fallat, super util!!
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
        if list[i][0] == to_find:
            return (i)
    return (None)

def addProduct(productes, cistell):
    id_input = input("Introdueix el codi del producte: ")
    info_productes = libft.ft_extract(productes)
    producte = libft.ft_find(info_productes, id_input)
    
    if not producte:
        print("Error: No s'ha trobat el producte\n")
        return cistell
    nom_prod = producte[2]
    preu_prod = producte[1]

    quantitat = int(input(f"Quantes unitats de '{nom_prod}' vols?: "))
    
    index = ft_find_index(cistell, id_input)
    if index is not None:
        nova_qty = int(cistell[index][1]) + quantitat
        cistell[index][1] = str(nova_qty)
    else:
        cistell.append([id_input, str(quantitat), nom_prod, preu_prod])
    
    showCistella(cistell)
    return cistell
    
def showCistella(cistella):
    if not cistella:
        print("\nLa teva cistella està buida...")
        return 
    
    print("\n" + "*"*75)
    print(f"{'CODI':<8} | {'NOM':<18} | {'QTY':<6} | {'PREU':<10} | {'TOTAL'}")
    print("*"*75)
    
    total_comanda = 0
    for item in cistella:
        preu_unitari = int(item[3])
        subtotal = int(item[1]) * preu_unitari
        total_comanda += subtotal
        
        preu_txt = f"{preu_unitari} €"
        subtotal_txt = f"{subtotal} €"
        
        print(f"{item[0]:<8} | {item[2]:<18} | {item[1]:<6} | {preu_txt:<10} | {subtotal_txt}")
        
    print("*"*75)
    print(f"TOTAL COMANDA: {total_comanda} €")
def deleteProducte(cistella):
    id = input("Introdueix el codi del producte que vols eliminar de la teva cistella: \n")
    producte = ft_find_index(cistella,id)
    
    if producte is None:
        print("Error: No se ha trobat el producte\n")
        return (cistella)
    del cistella[producte]
    showCistella(cistella)
    return cistella
    
def validarComanda(user_nif, cistella):
    if not cistella:
        print("No pots validar una comanda buida.")
        return False
    
    data_avui = datetime.today().strftime('%Y%m%d')
    nom_fitxer = f"{user_nif}{data_avui}.txt"
    
    try:
        with open(nom_fitxer, 'w') as f:
            for item in cistella:
                f.write(f"{item[0]};{item[1]};{item[3]}\n")
        print(f"Comanda validada correctament! Guardada a: {nom_fitxer}")
        return True
    except Exception as e:
        print(f"Error al desar la comanda: {e}")
        return False

def aplicacio_4():
    usuaris, productes = tryRead()
    choice = 1
    cistella = []
    
    if usuaris is None:
        return (-1)
    
    user = login(usuaris)
    if not user:
        return
    print(f"Benvingut a l’aplicació de vendes {user[1]}")
    while (choice != 0):
        choice = menu()
        match choice:
            case 0:
                print(f"Sortint del programa. Que tinguis un bon dia {user[1]}")
            case 1:
                cistella = addProduct(productes,cistella)
            case 2:
                deleteProducte(cistella)
            case 3:
                showCistella(cistella)
            case 4:
                if validarComanda(user[0], cistella):
                    cistella = []
aplicacio_4()