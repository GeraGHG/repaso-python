num = 45
multiplo = 3
lista_multiplos = [0]
while True:
    lista_multiplos.append(multiplo)
    suma = sum(lista_multiplos)
    multiplo += 3
    if suma >= num:
        print(lista_multiplos)
        break