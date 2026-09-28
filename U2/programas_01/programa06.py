# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta

dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:

    dias_mes = 31

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:

    dias_mes = 30

elif mes == 2:

    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        dias_mes = 29
    else:
        dias_mes = 28
else:
    print("Fecha incorrecta")

if dia <= 0 or dia > dias_mes:
    print("Fecha incorrecta")
else:
    print("Fecha correcta")
