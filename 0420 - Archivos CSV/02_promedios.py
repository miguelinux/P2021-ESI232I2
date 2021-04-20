# CSV -> Comma Separated Values
import csv

def promedio_por_alumno(lector):
    promedio = 0.0
    for fila in lector:
        for i in range(1,5):
            promedio = promedio + float(fila[i])
        print("El promedio de", fila[0], "es", promedio)

# Pregutamos por el nombre del archivo
nombre_archivo = input("Escribe el nombre del archivo: ")
archivo = open(nombre_archivo,"r")
lector = csv.reader(archivo)

promedio_por_alumno(lector)
