"""
Escribe un programa en Python que importe el modulo math completo y que le pregunte al
usuario que operación matemática quiere hacer:
1. Seno de un ángulo
2. Coseno de ángulo
3. Raíz cuadrada de un número
4. Potencia de dos números.
Le pida los datos necesarios y muestre los resultados por pantalla.
"""

import math

def mostrar_menu():
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un número")
    print("4. Potencia de dos números")
    print("5. Salir")

def main():
    mostrar_menu()
    opcion = input("Introduce una opción (1-5): ")
    match opcion:
        case "1":
            calcular_seno()
        case "2":
            calcular_coseno()
        case "3":
            calcular_raiz_cuadrada()
        case "4":
            calcular_potencia()
        case "5":
            print("Saliendo del programa...")
        case _:
            print("Opción no válida. Inténtalo de nuevo.")

def calcular_seno():
    angulo = float(input("Introduce el ángulo en grados: "))
    radianes = math.radians(angulo)
    resultado = math.sin(radianes)
    print(f"El seno de {angulo} grados es: {resultado}")

def calcular_coseno():
    angulo = float(input("Introduce el ángulo en grados: "))
    radianes = math.radians(angulo)
    resultado = math.cos(radianes)
    print(f"El coseno de {angulo} grados es: {resultado}")

def calcular_raiz_cuadrada():
    numero = float(input("Introduce un número: "))
    resultado = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es: {resultado}")

def calcular_potencia():
    base = float(input("Introduce la base: "))
    exponente = float(input("Introduce el exponente: "))
    resultado = math.pow(base, exponente)
    print(f"{base} elevado a {exponente} es: {resultado}")