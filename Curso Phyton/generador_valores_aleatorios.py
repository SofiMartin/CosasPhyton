# Valores aleatorios con la función randint

#import random
from random import randint

# Generar un número aleatorio entre 1 y 10.
numero = randint(1,10)
print(f'Número aleatorio generado: {numero}')

#Simular un dado de seis caras
dado = randint(1,6)
print(f'Resultado de lanzar el dado: {dado}')
