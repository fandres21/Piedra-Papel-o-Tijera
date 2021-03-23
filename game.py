import os
from time import sleep
from random import randint
from dearpygui import core, simple

from dearpygui.core import *
from dearpygui.simple import *
from PIL import Image
array = ["piedra", "papel", "tijera"]
contUser = 0
contPc = 0
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
    return condicion


def presentacion():
    clear()
    #print("JUEGO DE PIEDRA, PAPEL O TIJERA")
    pc = array[randint(0, len(array)-1)]
    pci = array.index(pc)
    return [pc, pci]


# if __name__ == "__main__":
#     while condicion:
#         presentacion()
#         pc,pci = presentacion()
#         print("Tu tienes: {} puntos y la maquina tiene {} puntos ".format(contUser,contPc))
#         rsp = input('Ingresa piedra,papel o tijera:\n >> ').lower()
#         if rsp not in array:
#             print("Ingresa una de las opciones validas para jugar")
#             sleep(1)
#             clear()
#         else:
#             rspi = array.index(rsp)
#             if pci >rspi:
#                 if pci ==2 and rspi==0:
#                     print("Ganaste, {} gana a {}".format(rsp, pc))
#                     contUser += 1
#                 else:
#                     print("Perdiste, {} gana a {}".format(pc,rsp))
#                     contPc += 1
#             elif pci == rspi:
#                 print("Es un empate de dos {}s".format(pc))
#             elif pci<rspi:
#                 if pci == 0 and rspi == 2:
#                     print("Perdiste, {} gana a {}".format(pc, rsp))
#                     contPc += 1
#                 else:
#                     print("Ganaste, {} gana a {}".format(rsp, pc))
#                     contUser += 1
#         sleep(2)
#         condicion = whoWin(contPc,contUser)

###########################################
#####INTERFAZ VISUAL #####################
##########################################
def obtenerSelectBox(Sender):
    # print para comprobar resultado en Str
    #print(array[core.get_value(Sender)])
    return str(array[core.get_value(Sender)])


with simple.window("JUEGO DE PIEDRA, PAPEL O TIJERA"):
    core.set_main_window_size(500, 500)
    pc, pci = presentacion()
    core.add_text(
        "Tu tienes: {} puntos y la maquina tiene {} puntos ".format(contUser, contPc))

    opcionElegida = core.add_listbox(
        name="",
        items=array,
        num_items=3,
        default_value = 0,
        callback=obtenerSelectBox,
        label = "aasdsads"
        
        )
        
    print(opcionElegida)

    entrada = core.add_input_text(
        "string", default_value="Ingresa piedra,papel o tijera:\n >> ".lower())
    # get_value(entrada)

core.start_dearpygui(primary_window="JUEGO DE PIEDRA, PAPEL O TIJERA")
