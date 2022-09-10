# Juego de piedra, papel, tijera

import random

#despliegue de menu
print("------------------------------------------")
print("\nEscoja su opcion de juego: ")
print("\n1. para piedra ")
print("\n2. para papel ")
print("\n3. para tijera \n")
print("-----------------------------------------")

#input
n=int(input("Ingrese su opcion: "))
a=random.randint(1,3)

#processing
if 1<=n<=3:
    if n==1 and a==1:
        print ("!Empate!")
    elif n==1 and a==2:
        print("Derrota")
    elif n==1 and a==3:
        print("Victoria")
    elif n==2 and a==1:
        print("Victoria")
    elif n==2 and a==2:
        print("!Empate!")
    elif n==2 and a==3:
        print("Derrota")
    elif n==3 and a==1:
        print("Derrota")
    elif n==3 and a==2:
        print("VIctoria")
    elif n==1 and a==2:
        print("!Empate!")
else:
    print("la opcion escogida es incorrecta")
