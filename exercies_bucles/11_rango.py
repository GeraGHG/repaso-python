x = 0
resultado_menor = 100
for i in range(-9, 9):
    fx = i**2 - 6*i + 3
    if fx < resultado_menor:
        x = i
        resultado_menor = fx

print(x, resultado_menor)