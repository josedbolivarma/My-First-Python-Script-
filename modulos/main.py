# import operaciones as O

# def main():
#     res = O.suma(2, 2)
#     resResta = O.resta(5, 3)
#     op = O.Operador.multiplicacion(4, 4)
#     print('Hola en main()', res, resResta)
#     print(op)

# if __name__ == '__main__':
#     main()

# Importar modulos de un paquete

# import operaciones.suma

# def main():
#     mult = operaciones.suma.Multiplicador()
#     print(mult.multiplica(5, 5))
#     # suma = operaciones.suma.suma(2 ,2)
#     # print(suma)

# if __name__ == '__main__':
#     main()

# import operaciones.restador.resta
# import operaciones.sumador.suma

import operaciones.restador.resta as r
import operaciones.sumador.suma as s

# from operaciones import restador, sumador

# from operaciones import *

# resta = restador.resta(5, 3)
# suma = sumador.suma(4, 4)


def main():
    # resta = operaciones.restador.resta.resta(5, 3)
    # suma = operaciones.sumador.suma.suma(40, 40)
        resta = r.resta(5, 3)
        suma = s.suma(40, 40)
        print(resta, suma)

if __name__ == '__main__':
    main()