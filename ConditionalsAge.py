age = 17

if age < 18:
    print('Menor de edad')
else: 
    print('Mayor de edad')

# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

# V1

numbers = [2,3,4,5,6,7,8]

for number in numbers:
   if (number % 2) == 0:
       continue
   print('IMPAR NUMBER: ',number)

# V2

array = []

for number in numbers:
   if (number % 2) == 0:
       continue
   array.append(number)
   
print('MY NEW IMPAR ARRAY IS: ',array)