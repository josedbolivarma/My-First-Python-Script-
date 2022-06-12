# EJERCICIO 1
# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

# Color

# Ruedas

# Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

# Velocidad

# Cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = ''
    ruedas = ''
    puertas = ''
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = ''
    cilindrada = ''
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

c = Coche('Rojo', 4, 4, 240, 'No')

print(c.color, c.ruedas, c.puertas, c.velocidad, c.cilindrada)