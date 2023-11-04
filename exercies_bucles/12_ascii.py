columna1 = []
columna2 = []
columna3 = []
columna4 = []

inicio = 33
final = 127
for i in range(19):
    for j in range(5):
        if inicio == final:
            print()
        if inicio < 100:
            print(f"0{inicio} {chr(inicio)}", end="  ")
            inicio += 1
        elif inicio >= 100:
            print(f"{inicio} {chr(inicio)}", end="  ")
            inicio += 1
            if inicio == final:
                print(f"{inicio}")
                break
    print()

        