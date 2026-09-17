"""
Escribe un programa que, dado un número de dos cifras, diseñe un algoritmo
que permita obtener el número invertido.
"""
 
num = int(input("Introduce un número de dos cifras: "))
 
decenas = num // 10
unidades = num % 10
invertido = unidades * 10 + decenas
 
print(f"El número {num} invertido es {invertido}")