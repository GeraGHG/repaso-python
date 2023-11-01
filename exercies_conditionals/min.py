def tres_nums(num1, num2, num3):
    return min(num1, num2, num3)

num1 = int(input("Ingrese el primero: "))
num2 = int(input("Ingrese el segundo: "))
num3 = int(input("Ingrese el tercero: "))
resultado = tres_nums(num1, num2, num3)
print("El número menor es:", resultado)

