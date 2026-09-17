"""
Escribe un programa que convierta un valor dado en grados Fahrenheit a
grados Celsius.
"""
 
gradosf = float(input("Introduce la temperatura en grados Fahrenheit: "))
gradosc = (gradosf - 32) * 5 / 9
 
print(f"{gradosf}°F son {gradosc}°C")