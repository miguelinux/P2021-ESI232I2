# Escribir la palabra "hola" en número de veces
# que el usuario nos indique

cuantos = int(input("¿Cuantos holas quieres?: "))

for contador in range(1, cuantos+1):
    print(contador,": Hola")