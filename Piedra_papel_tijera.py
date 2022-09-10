# Juego de piedra, papel, tijera

import random

#despliegue de menu
print("------------------------------------------")
print("\nEscoja su opcion de juego: ")
print("\n1. para piedra ")
print("\n2. para papel ")
print("\n3. para tijera \n")
print("-----------------------------------------\n")

#input
n=int(input("Ingrese su opcion: "))
a=random.randint(1,3)

#processing
if 1<=n<=3:
    if n==1 and a==1:
        print("\nUsted: piedra,  Computadora: piedra")
        print ("\n!Empate!\n")
    elif n==1 and a==2:
        print("\nUsted: piedra,  Computadora: papel")
        print("\nDerrota\n")
    elif n==1 and a==3:
        print("\nUsted: piedra,  Computadora: tijera")
        print("\nVictoria\n")
    elif n==2 and a==1:
        print("\nUsted: papel,  Computadora: piedra")
        print("\nVictoria\n")
    elif n==2 and a==2:
        print("\nUsted: papel,  Computadora: papel")
        print("\n!Empate!\n")
    elif n==2 and a==3:
        print("\nUsted: papel,  Computadora: tijera")
        print("\nDerrota\n")
    elif n==3 and a==1:
        print("\nUsted: tijera,  Computadora: piedra")
        print("\nDerrota\n")
    elif n==3 and a==2:
        print("\nUsted: tijera,  Computadora: papel")
        print("\nVictoria\n")
    elif n==1 and a==2:
        print("\nUsted: tijera,  Computadora: tijera")
        print("\n!Empate!\n")
else:
    print("\nla opcion escogida es incorrecta\n")