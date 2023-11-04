# print(not([]))
data = ["Tenerife", {"cielo": "limpio", "temp": 24}, 3718, (28.2933947, -16.5226597)]
print(data)
"""
Aunque está permitido, NUNCA llames list a una variable porque destruirías la función que nos permite crear listas. Y tampoco uses nombres derivados como _list o list_ ya que no son nombres representativos que identifiquen el propósito de la variable.

Para crear una lista vacía, se suele recomendar el uso de [] frente a list(), no sólo por ser más pitónico sino por tener (en promedio) un mejor rendimiento en tiempos de ejecución.


"""
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

print(shopping[10:])

print(shopping[-100:2])
# ['Agua', 'Huevos']

print(shopping[2:100])
# ['Aceite', 'Sal', 'Limón']
# Ninguna de las operaciones anteriores modifican la lista original, simplemente devuelven una lista nueva."""
cities = ["London", "New York", "Paris", "Hong Kong", "Madrid"]
cities.insert(1, "Ciudad de México")
print(cities)
"""
Repetir elementos
Al igual que con las cadenas de texto, el operador * nos permite repetir los elementos de una lista:
"""
shopping = ['Agua', 'Huevos', 'Aceite']

print(shopping * 3)

print(shopping.index("Agua"))


