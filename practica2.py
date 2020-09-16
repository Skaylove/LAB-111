#Practica 2
X = int(input("ingrese un tiempo en segundos    "))
A =  int(input("Ingrese los horas para realizar la tarea   "))
dias = A * (60*60)
B = int(input("Ingrese las minutos para realizar la tarea    "))
horas = B * (60)
C = int(input("Ingrese los segundos para realizar la tarea  "))
Z = dias+horas+C
if (X<=Z):
    print('Si se puede realizar la tare')
else:
    print('No se puede realizar la tarea')
