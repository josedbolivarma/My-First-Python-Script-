import math

print("¿Cómo se llama?")
nombre = input()

print('¿Cuál es tu altura en metros?')
altura = float(input())

print('¿Cuál es tu peso en kilogramos?')
peso = float(input())

# Operación: (IMC = peso [kg]/ estatura [m2])
imc = round(peso / math.sqrt(altura), 2)

print('Hola ' + nombre)
print(' este es tu IMC: ', imc)
