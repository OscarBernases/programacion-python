"""
Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca.
"""

import random

banca = random.randrange(17, 22)
num_jugadores = int(input("Introduce el número de jugadores: "))

for jugador in range(1, num_jugadores + 1):
    print(f"\nTurno del jugador {jugador}:")
    puntuacion_jugador = 0
    seguir = True

    while seguir:
        carta = random.randrange(1, 6)
        puntuacion_jugador += carta
        print(f"Has sacado una carta de valor {carta}. Tu puntuación actual es {puntuacion_jugador}.")

        if puntuacion_jugador > 21:
            print("¡Te has pasado de 21! Has perdido.")
            seguir = False
        else:
            respuesta = input("¿Quieres sacar otra carta? (s/n): ")
            if respuesta != "s":
                seguir = False

    print(f"La banca tiene una puntuación de {banca}.")

    if puntuacion_jugador > 21:
        print("Has perdido porque te has pasado de 21.")
    elif puntuacion_jugador <= banca:
        print("Has perdido porque tu puntuación es menor o igual a la de la banca.")
    else:
        print("¡Felicidades! Has ganado porque tu puntuación es mayor que la de la banca.")