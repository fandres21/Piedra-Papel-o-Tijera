import os
from time import sleep
from random import randint
from dearpygui import core, simple

from dearpygui.core import *
from dearpygui.simple import *
from PIL import Image
array = ["piedra", "papel", "tijera"]
condicion = True
clear= lambda :os.system('cls')
#Imagenes para opciones
Impiedra=Image.open("src/img/piedra.png")
Impapel=Image.open("src/img/papel.png")
Imtijera=Image.open("src/img/tijera.png")
def whoWin(contPc, contUser):
    condicion = True
    if contPc > contUser:
        contLider = "La Maquina"
    else:
        contLider = "El Jugador"
    if(contPc > 3 or contUser > 3):
        print("El juego a terminado, el ganador es {}".format(contLider))
        condicion = False
        configure_item(".",enabled=False)
    return condicion


def presentacion():
    clear()
    pc = array[randint(0, len(array)-1)]
    pci = array.index(pc)
    return [pc, pci]

###########################################
#####INTERFAZ VISUAL #####################
##########################################
contUser=0
contPc=0
def MainLoop(Sender):
    global contUser
    global contPc
    presentacion()
    pc, pci = presentacion()
    print("Tu tienes: {} puntos y la maquina tiene {} puntos ".format(contUser, contPc))
    valueRetorn=str(array[core.get_value(Sender)])
    valueRetorni = array.index(valueRetorn)
    if pci>valueRetorni:
        if pci == 2 and valueRetorni == 0:
            print("Ganaste, {} gana a {}".format(valueRetorn, pc))
            contUser+=1
        else:
            print("Perdiste, {} gana a {}".format(pc, valueRetorn))
            contPc += 1
    elif pci == valueRetorni:
        print("Es un empate de dos {}s".format(pc))
    elif pci<valueRetorni:
        if pci == 0 and valueRetorni == 2:
            print("Perdiste, {} gana a {}".format(pc, valueRetorn))
            contPc += 1
        else:
            print("Ganaste, {} gana a {}".format(valueRetorn, pc))
            contUser += 1
    set_value("Tu tienes: 0 puntos y la maquina tiene 0 puntos","Tu tienes: {} puntos y la maquina tiene {} puntos".format(contUser, contPc))
    condicion = whoWin(contPc,contUser)

with simple.window("PPT"):

    core.set_main_window_size(500, 500)
    pc, pci = presentacion()
    core.add_text(name="Tu tienes: 0 puntos y la maquina tiene 0 puntos",
        tip="Contenedor Puntos")
    opcionElegida = core.add_listbox(
        name=".",
        items=array,
        num_items=3,
        default_value = 0,
        callback=MainLoop,
        )
core.start_dearpygui(primary_window="PPT")
