"""
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor.
"""

def calcular_area_circulo(radio):
    return 3.1416 * radio ** 2

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_rectangulo(base, altura):
    return base * altura

def mostrar_menu():
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Introduce una opción (1-4): ")
        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def opcion1():
    radio = float(input("Introduce el radio del círculo: "))
    if radio > 0:
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area}")
    else:
        print("El radio debe ser mayor que 0. Inténtalo de nuevo.")

def opcion2():
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    if base > 0 and altura > 0:
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area}")
    else:
        print("La base y la altura deben ser mayores que 0. Inténtalo de nuevo.")

def opcion3():
    base = float(input("Introduce la base del rectángulo: "))
    altura = float(input("Introduce la altura del rectángulo: "))
    if base > 0 and altura > 0:
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area}")
    else:
        print("La base y la altura deben ser mayores que 0. Inténtalo de nuevo.")

main()