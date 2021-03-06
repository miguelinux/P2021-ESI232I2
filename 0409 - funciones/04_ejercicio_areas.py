import math

# funcion menu sin parametros
def menu():
    print("1) Calcular el área de un rectángulo")
    print("2) Calcular el área de un triángulo")
    print("3) Calcular el área de un cuadrado")
    print("4) Calcular el área de un círculo")
    print("5) Salir")


def area_rectangulo(base, altura):
    resultado = base * altura
    return resultado


def area_triangulo(base, altura):
    resultado = base * altura / 2
    return resultado

def area_circulo(radio):
    #resultado = 3.1416 * radio * radio
    resultado = math.pi * radio * radio
    return resultado


def calcular_area_rectangulo(figura):
    largo = float(input("¿Cuanto mide de largo?: "))
    ancho = float(input("¿Cuanto mide de ancho?: "))
    area = area_rectangulo(largo, ancho)
    print("El area del",figura," es ", area)


def calcular_area_triangulo():
    base = float(input("¿Cuanto mide de base?: "))
    altura = float(input("¿Cuanto mide de altura?: "))
    area = area_triangulo(base, altura)
    print("El area del triangulo es ", area)


def calcular_area_circulo():
    radio = float(input("¿Cuanto mide el radio?: "))
    area = area_circulo(radio)
    print("El area del triangulo es ", area)


opcion = 0
# Mientras la opcion sea deferente de 5
while opcion != 5:
    menu()
    opcion = int(input("Opción: "))
    if opcion == 1:
        calcular_area_rectangulo("rectangulo")
    elif opcion == 2:
        calcular_area_triangulo()
    elif opcion == 3:
        calcular_area_rectangulo("cuadrado")
    elif opcion == 4:
        calcular_area_circulo()

