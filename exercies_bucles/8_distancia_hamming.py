cadena1 = "0001010011101"
cadena2 = "0000110010001"
if len(cadena1) != len(cadena2):
        raise ValueError("Las cadenas deben tener la misma longitud")
distancia = 0
for i in range(len(cadena1)):
    if cadena1[i] != cadena2[i]:
        distancia += 1

print(distancia)