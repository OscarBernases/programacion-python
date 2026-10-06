"""
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana.
"""

import random

banca = random.randrange(17, 22)
puntuacion_jugador = 0
seguir = True

while seguir:
    carta = random.randrange(1, 6)
    puntuacion_jugador = puntuacion_jugador + carta
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