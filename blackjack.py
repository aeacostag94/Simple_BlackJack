import random
from array import array
import numpy as np


# Funcion para repartir la baraja solo para el repartidor.

def _repartidor():

    carta_repartidor = random.randint(1, 10)
    carta_repartidor2 = random.randint(1, 10)
    print("Primera carta: " + str(carta_repartidor))
    print("Primera carta: " + str(carta_repartidor2))
    acumulado_rep = carta_repartidor + carta_repartidor2
    print("Repartidor tiene:  *****" + str(acumulado_rep))

    while acumulado_rep <= 21 or acumulado_rep <= 20 or acumulado_rep <= 19 or acumulado_rep <= 18:
        otracarta = random.randint(1, 10)
        print("Otra carta valor de:  " + str(otracarta))
        acumulado_rep = acumulado_rep + otracarta
        print("Repartidor acumula= ******" + str(acumulado_rep))
        if acumulado_rep in range(18, 22):
            print("Repartidor se detiene en  :" + str(acumulado_rep))
            break
    else:
        print("Repartidor pierde por tener:  " + str(acumulado_rep))


############## FIN DE LA FUNCION ############################


# VARIABLES:

acumulado = 0
x = 0

# Inicio del juego:

print("Bienvenido a la partida de BlackJack, ¿Cuanto jugadores son: ?")
jugadores = int(input("Ingrese el numero de jugadores de 1 a 4: "))


# restriccion de valores mayores a 4 jugadores.
while(True):
    if jugadores not in range(1, 5):
        print("Enter a valid number between 1 and 4")
        jugadores = int(input())
    else:
        print("+++++ Numero de jugadores +++++ : " + str(jugadores))
        break


# for x in repeat(1, jugadores):  # Runs the loop jugadores times
    # print("Jugador numero: " + str(jugadores))


# Logica para el ciclo de toma de decision de cada jugador
while x < jugadores:
    x = x + 1
    print("+++++ Jugador numero +++++:  " + str(x))

    r1 = random.randint(1, 10)
    r2 = random.randint(1, 10)
    acumulado = r1 + r2
    print("Tu carta numero uno:  " + str(r1))
    print("Tu carta numero dos:  " + str(r2))
    print("Total: " + str(r1 + r2))

    print("Quiere otra carta: ")
    print("Marque (1) para si y (2) para no")
    decision = int(input())


# Validacion del ingreso
# How do you limit user inputs to a list to a specified range of integers in Python?
# doing this:

    while(True):
        if decision not in range(1, 3):
            print("Enter a valid number between 1 and 2")
            decision = int(input())
        else:
            # print("sirve") se uso para probar el ciclo.
            break

# Logica del programa:

    if decision == 1:
        peticion = random.randint(1, 10)
        print("Su carta: " + str(peticion))
        acumulado = r1 + r2 + peticion
        print(" **** Total ****:" + str(acumulado))
        while acumulado < 21:
            print("Quiere otra carta: ")
            print("1 para si y 2 para no")
            decision2 = int(input())
            if decision2 == 1:
                peticion2 = random.randint(1, 10)
                print("Su otra carta es: " + str(peticion2))
                acumulado = acumulado + peticion2
                print("**** Total ****:" + str(acumulado))
                if acumulado > 21:
                    print("PERDISTE SO SORRY!! :(")
            else:
                print("Se queda, total es:" + str(acumulado))
                break
    else:
        print("Se queda total es: " + str(acumulado))

    temp_array = array('i', [acumulado])
    temporal = temp_array.tolist()
    print(temporal)
    print(np.array([temporal]))

# Se llama la funcion del repartidor.
_repartidor()
