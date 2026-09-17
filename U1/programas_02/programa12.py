"""
Sabiendo que 1 milla equivale a 1,61 Km, escribe un programa que pida un
número de millas y un número de Km, y muestre respectivamente el número de
kilómetros y millas equivalentes. Los resultados deben estar redondeados a
2 decimales.
"""

millas = float(input("Introduce un número de millas: "))
km = float(input("Introduce un número de kilómetros: "))
 
km_desde_millas = round(millas * 1.61, 2)
millas_desde_km = round(km / 1.61, 2)
 
print(f"{millas} millas equivalen a {km_desde_millas}km")
print(f"{km} km equivalen a {millas_desde_km} millas")