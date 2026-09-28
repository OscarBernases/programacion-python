"""
Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que
saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya
sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
Puedes pedir el valor de cada tirada de dados por teclado o usar la la función
random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello
debes poner import random al inicio del programa)
"""

import random

jugador1_dado1 = random.randrange(1, 7)
jugador1_dado2 = random.randrange(1, 7)

jugador2_dado1 = random.randrange(1, 7)
jugador2_dado2 = random.randrange(1, 7)

jugador1_total = jugador1_dado1 + jugador1_dado2
jugador2_total = jugador2_dado1 + jugador2_dado2

if jugador1_dado1 > jugador1_dado2:
    jugador1_tirada_mayor = jugador1_dado1
else:
    jugador1_tirada_mayor = jugador1_dado2

if jugador2_dado1 > jugador2_dado2:
    jugador2_tirada_mayor = jugador2_dado1
else:
    jugador2_tirada_mayor = jugador2_dado2

if jugador1_total > jugador2_total:
    print("El jugador 1 ha ganado.")
elif jugador1_total < jugador2_total:
    print("El jugador 2 ha ganado.")
else:
    if jugador1_tirada_mayor > jugador2_tirada_mayor:
        print("El jugador 1 ha ganado.")
    else:
        print("El jugador 2 ha ganado.")
