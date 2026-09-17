"""
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de N segundos. Escribe un
programa que determine la hora de llegada a la ciudad B.
"""
 
horas_salida = int(input("Introduce la hora de salida: "))
minutos_salida = int(input("Introduce los minutos de salida: "))
segundos_salida = int(input("Introduce los segundos de salida: "))
duracion_viaje = int(input("Introduce la duración del viaje en segundos: "))
 
segundos_salida = horas_salida * 3600 + minutos_salida * 60 + segundos_salida
segundos_llegada = (segundos_salida + duracion_viaje) % 86400
 
horas_llegada = segundos_llegada // 3600
minutos_llegada = (segundos_llegada % 3600) // 60
segundos_llegada = segundos_llegada % 60
 
print(f"Hora de llegada a la ciudad B: {horas_llegada}:{minutos_llegada}:{segundos_llegada}")