import os
from time import sleep
from random import randint

array = ["piedra","papel","tijera"]
contUser = 0
contPc = 0
condicion=True
while condicion:
    os.system("cls")
    print("JUEGO DE PIEDRA, PAPEL O TIJERA")
    pc = array[randint(0,len(array)-1)]
    pci=array.index(pc)
    print("Tu tienes: {} puntos y la maquina tiene {} puntos ".format(contUser,contPc))
    rsp = input('Ingresa piedra,papel o tijera:\n >> ').lower()
    rspi=array.index(rsp)
    if rsp not in array:
        print("Ingresa una de las opciones validas para jugar")
        sleep(1)
        os.system('cls')
    elif pci >rspi:
        if pci ==2 and rspi==0:
            print("Ganaste, {} gana a {}".format(rsp, pc))
            contUser += 1
        else:
            print("Perdiste, {} gana a {}".format(pc,rsp))
            contPc += 1
    elif pci == rspi:
        print("Es un empate de dos {}s".format(pc))
    elif pci<rspi:
        if pci == 0 and rspi == 2:
            print("Perdiste, {} gana a {}".format(pc, rsp))
            contPc += 1
        else:
            print("Ganaste, {} gana a {}".format(rsp, pc))
            contUser += 1
    sleep(2)
    if contPc>contUser:
        contLider="La Maquina"
    else:
        contLider="El Jugador"
    if(contPc>3 or contUser>3):
        print("El juego a terminado, el ganador es {}".format(contLider))
        condicion=False





