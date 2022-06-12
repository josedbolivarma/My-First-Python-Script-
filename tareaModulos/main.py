# EJERCICIO 1 
# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.

import operaciones.operaciones

suma = operaciones.operaciones.sumacion(4, 4)
resta =  operaciones.operaciones.restacion(4, 4)
multiplicacion =  operaciones.operaciones.multiplicacion(4, 4)
division =  operaciones.operaciones.division(8, 4)

print(suma)
print(resta)
print(multiplicacion)
print(division)