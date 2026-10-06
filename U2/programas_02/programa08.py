"""
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.
Puedes generar el número usando la función random.randrange(1, 21) para
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
del programa).
Mejora el programa de forma que el usuario tenga solo 3 intentos.
"""

import random

numero_aleatorio = random.randrange(1, 21)
intentos = 0
acertado = False

print("Adivina el número entre 1 y 20")

while intentos < 3 and not acertado:
    numero_usuario = int(input("Introduce un número: "))
    intentos = intentos + 1

    if numero_usuario < numero_aleatorio:
        print("El número a adivinar es mayor que el introducido.")
    elif numero_usuario > numero_aleatorio:
        print("El número a adivinar es menor que el introducido.")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_aleatorio} en {intentos} intentos.")
        acertado = True

if acertado == True:
    print(f"¡Has ganado! Has usado {intentos} intentos.")
else:
    print(f"Lo siento, has agotado tus intentos. El número era {numero_aleatorio}.")