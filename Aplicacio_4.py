# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Aplicacio_4.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vaguayo- <vaguayo-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/12 16:36:29 by vaguayo-          #+#    #+#              #
#    Updated: 2026/01/12 17:47:47 by vaguayo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

def login(usuaris):
    count = 0
    nif = int(input("Si us plau introdueix el teu NIF: "))
    info_usuaris = usuaris.split("\n") 
    info_usuaris = info_usuaris.split(';')
    while not nif in info_usuaris:
            if count > 3:
                return(print("Error, maxim 3 intents"))
            print(f"Error, tens {3 - count } intents")
            nif = int(input("Si us plau introdueix el teu NIF: "))
            count += 1
    print("yes")
  
        
def aplicacio_4(usuaris, productes):
    if not os.path.exists("/ruta/fitxer"):
        return (print("Error"))
    if not usuaris and productes:
        return (print("Error"))
    
usuaris = "5675;victor\n5444;pepe"
login(usuaris)