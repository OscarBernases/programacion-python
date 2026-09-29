"""
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no.
"""

print("VERSION 1: ")
num = int(input("Introduce un número: "))

contador = 0
suma = num

while num != 0:
    num = int(input("Introduce un número: "))
    contador = contador + 1
    suma = suma + num
else:
    print(f"La suma de todos los números es: {suma}")
    print(f"La media de todos los números es: {suma / contador}")


print("VERSION 2: ")
num = int(input("Introduce un número: "))

contador = 0
suma = num

while True:
    num = int(input("Introduce un número: "))
    contador = contador + 1
    suma = suma + num
    if num == 0:
        break

print(f"La suma de todos los números es: {suma}")
print(f"La media de todos los números es: {suma / contador}")
