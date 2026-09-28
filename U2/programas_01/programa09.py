"""
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:

    1. Piedra
    2. Papel
    3. Tijera

Seleccione una opción (1, 2 o 3):

Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.
Ten en cuenta que:
    La piedra gana a la tijera pero pierde contra el papel.
    El papel gana a la piedra pero pierde contra la tijera.
    La tijera gana al papel pero pierde contra la piedra.
"""

import random

opcion_programa = random.randrange(1, 4)

opcion_jugador = int(
    input("1. Piedra\n2. Papel\n3. Tijera\n\nSeleccione una opción (1, 2 o 3): ")
)

if (
    (opcion_jugador == 1 and opcion_programa == 3)
    or (opcion_jugador == 2 and opcion_programa == 1)
    or (opcion_jugador == 3 and opcion_programa == 2)
):
    print("¡Has ganado!")
elif (
    (opcion_programa == 1 and opcion_jugador == 3)
    or (opcion_programa == 2 and opcion_jugador == 1)
    or (opcion_programa == 3 and opcion_jugador == 2)
):
    print("¡Has perdido!")
else:
    print("¡Empate!")
