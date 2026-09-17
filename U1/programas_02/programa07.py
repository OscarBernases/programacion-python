"""
Escribe un programa que reciba una cantidad de minutos y muestre por
pantalla a cuántas horas y minutos corresponde.
"""
 
minutos_teclado = int(input("Introduce una cantidad de minutos: "))
 
horas = minutos_teclado // 60
minutos = minutos_teclado % 60
 
print(f"{minutos_teclado} minutos son {horas} horas y {minutos} minutos")