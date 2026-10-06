"""
Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
pedir el número hasta que no se introduzca correctamente. Controla las posibles
excepciones a la hora de introducir el número por teclado.
"""
añadido = False
while True and not añadido:
    try:
        numero = int(input("Introduce un número entre 1 y 10: "))
        if numero >= 1 and numero <= 10:
            print(f"Has introducido correctamente el número {numero}.")
            añadido = True
        else:
            print("El número no está entre 1 y 10. Inténtalo de nuevo.")
    except ValueError:
        print("Error. Introduce un número entero.")