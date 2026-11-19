import random

vidasJugador = 3
puntosJugador = 0
nivelJugador = 1

while vidasJugador > 0:
    print(f"Vidas: {vidasJugador}")
    print(f"Nivel: {nivelJugador}")
    ataque = input("Elije un ataque (fuerza, precision, riesgo): ")

    match (ataque):
        case "fuerza":
            cartaJugador = random.randrange(5, 10)
            cartaOrdenador = random.randrange(3, 10)
        case "precision":
            cartaJugador = random.randrange(3, 8)
            cartaOrdenador = random.randrange(2, 9)
        case "riesgo":
            cartaJugador = random.randrange(1, 10)
            cartaOrdenador = random.randrange(1, 8)
        case _:
            print("Esta opción no existe.")
            break

    if (cartaJugador > cartaOrdenador):
        print(f"Ha ganado el jugador con una carta de {cartaJugador} a la carta del ordenador de {cartaOrdenador}")
        puntosJugador = puntosJugador + 1
    elif (cartaJugador < cartaOrdenador):
        print(f"Ha ganado el ordenador con una carta de {cartaOrdenador} a la carta del jugador de {cartaJugador}")
        vidasJugador = vidasJugador - 1
    else:
        print("¡Empate!")

    if (puntosJugador % 3 == 0):
        print("¡Subes de nivel!")
        nivelJugador = nivelJugador + 1
        
        if (vidasJugador < 3):
            print("¡Has recuperado una vida!")
            vidasJugador = vidasJugador + 1


print("Estadisticas finales: ")
print(f" - Puntuacion: {puntosJugador}")
print(f" - Nivel: {nivelJugador}")