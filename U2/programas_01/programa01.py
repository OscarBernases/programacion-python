"""
Escribe un programa que pida primero un número par y luego un número impar (positivos
o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
impar respectivamente), se mostrará un aviso.
"""

num1 = int(input("Introduce un número par: "))
num2 = int(input("Introduce un número impar: "))

if num1 % 2 != 0 or num2 % 2 == 0:
    print("Error.")
else:
    print("Correcto.")
