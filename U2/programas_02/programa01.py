"""
Escribe un programa que muestre una lista de números del 1 al 10. Resuelve el ejercicio
de dos formas distintas, utilizando los bucles for y while. Cuando utilices el bucle for
puedes hacer uso de la función range.
"""

n = 0

print("CON BUCLE WHILE: ")
while n <= 10:
    print(n)
    n = n + 1

print("CON BUCLE FOR: ")
for i in range(10 + 1):
    print(i)
