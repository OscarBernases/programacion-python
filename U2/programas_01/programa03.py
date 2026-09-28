"""
Escribe un programa que pida dos numero y muestre su división. Se deben tener en
cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.
"""

try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    print(f"{num1} dividido entre {num2} es {num1 / num2}")

except ZeroDivisionError:
    print("No se puede dividir entre 0")
