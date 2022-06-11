import math

# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

# EJERCICIO 1

def calcularAreaTriangulo(altura, base): 
    area = (base * altura) / altura
    return area

print('CALCULAR EL ÁREA DE UN TRIÁNGULO: ')
print(calcularAreaTriangulo(20, 10))

# EJERCICIO 2

def calcularAreaCirculo(radio = 0): 
    area = math.sqrt(radio) * math.pi
    return area

print('CALCULAR EL ÁREA DE UN CIRCULO: ')
print(calcularAreaCirculo(12))

# EJERCICIO 3

# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def calcularNumeroPrimo(num):
    for n in range(2, num):
        if num % n == 0:
            print('No es primo', n, 'es divisor de', num)
            return False
    print('Es primo:', num)
    return True
        
calcularNumeroPrimo(1)