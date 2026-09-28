"""
Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
negativo) y si el valor no es correcto, mostrará un aviso.
"""

num1 = int(input("Introduce un número par: "))

if num1 % 2 == 0:
    num2 = int(input("Introduce un número impar: "))
    if num2 % 2 == 0:
        print("Error.")
    else:
        print("Correcto.")
else:
    print("Error.")
