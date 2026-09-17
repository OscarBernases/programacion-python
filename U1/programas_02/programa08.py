"""
Una tienda ofrece un descuento del 15% sobre el total de la compra y un
cliente desea saber cuánto deberá pagar finalmente por su compra.
"""
 
total_compra = float(input("Introduce el total de la compra: "))
 
descuento = total_compra * 0.15
total_a_pagar = total_compra - descuento
 
print(f"Descuento: {descuento}€")
print(f"Total: {total_a_pagar}€")