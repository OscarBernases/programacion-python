"""
Escribe un programa que use varias veces la función print() para:
 - Mostrar las operaciones de los operadores aritméticos de Python entre
   dos números.
 - Mostrar las operaciones de los operadores lógicos de Python con
   valores booleanos.
 - Mostrar las operaciones de los operadores de comparación de Python con
   valores booleanos y/o números.
"""

a = 10
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

p = True
q = False

print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)

print("Igual:", a == b)
print("Distinto:", a != b)
print("Mayor:", a > b)
print("Menor:", a < b)
print("Mayor o igual:", a >= b)
print("Menor o igual:", a <= b)
