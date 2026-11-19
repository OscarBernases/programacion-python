entero = int(input("Ingrese un número entero: "))
decimal = float(input("Ingrese un número decimal: "))
texto = input("Ingrese un texto: ")

print(f"Tipo Entero: {type(entero)}")
print(f"Tipo Decimal: {type(decimal)}")
print(f"Tipo Texto: {type(texto)}")

esEntero = type(entero) == int
print(esEntero)

esDecimal = type(decimal) == float
print(esDecimal)

esTexto = type(texto) == str
print(esTexto)

todasCorrectas = esEntero == True and esDecimal == True and esTexto == True
print(todasCorrectas)

comprobarNumeros = entero + decimal
print(comprobarNumeros)