import string

# string de prueba 
cadena = "hello-world"

# utilizo la biblioteca "string" para obener todos los ^[a-Z,A-Z]
ALPHABET = string.ascii_letters


for char in cadena:
    if char not in ALPHABET: # Sí un caracter no se encuentra en ALPHABET se ejecuta la condición 
        print("Se han encontrado caracteres no alfabéticos")
        break # Rompe el bucle
else:
    print("Todos son alfabéticos")  # se ejecuta si la condicion de arriba no se cumple
