strCountries = input('Escribe una lista de paises separados por comas ",": ').replace(' ', '').split(',')
listCountries = str(set(strCountries))

print(strCountries)
print(listCountries)