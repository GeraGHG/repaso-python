cadena = "1010"
range = len(cadena) - 1
suma = 0
for char in cadena:
    suma += int(char) * 2**range
    range -= 1
print(float(suma))