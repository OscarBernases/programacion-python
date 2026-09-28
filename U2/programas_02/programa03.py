"""
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
continue.
"""

n = 0

print("CON BUCLE WHILE: ")
while n <= 10:
    if n % 2 == 0:
        print(n)
    n = n + 1

n = 0

print("CON BUCLE WHILE + CONTINUE: ")
while n <= 10:
    if n % 2 != 0:
        n = n + 1
        continue
    print(n)
    n = n + 1

print("CON BUCLE FOR: ")
for i in range(11):
    if i % 2 == 0:
        print(i)

print("CON BUCLE FOR + CONTINUE: ")
for i in range(11):
    if i % 2 != 0:
        continue
    print(i)
