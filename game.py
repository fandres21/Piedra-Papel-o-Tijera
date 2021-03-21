import os
from time import sleep
from random import randint

array = ["piedra","papel","tijera"]

contUser = 0
contPc = 0
while True:
    os.system("cls")
    print("JUEGO DE PIEDRA, PAPEL O TIJERA")
    pc = array[randint(0,len(array)-1)]
    print("Tu tienes: {} puntos y la maquina tiene {} puntos ".format(contUser,contPc))
    rsp = input('Ingresa piedra,papel o tijera:\n >> ').lower()
    if rsp not in  array:
        print("Ingresa una de las opciones validas para jugar")
        sleep(1)
        print("Ingresa una de las opciones validas")
        os.system('cls')        
    else:
        if rsp == pc :
            print("Es un empate")
        elif rsp == 'piedra' and pc == 'papel':
            contPc += 1
            print("Perdiste, papel gana a piedra")
        elif rsp == 'papel' and pc == 'tijera':
            contPc += 1
            print("Perdiste, tijera corta papel")
        elif rsp == "tijera" and pc == "piedra":
            contPc += 1
            print("Perdiste, Piedra rompe tijera")
        elif rsp == "papel" and pc == "piedra":
            contUser += 1
            print("Ganaste, papel envuelve piedra")
        elif rsp == "tijera" and pc == "papel":
            contUser += 1
            print("Ganaste, Tijera corta Papel")
        elif rsp == "piedra" and pc == "tijera":
            contUser += 1
            print("Ganaste, Piedra Rompe Tijera")
        sleep(2) 



