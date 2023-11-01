"""
Escriba un programa en Python que pida (por separado) dos valores numéricos y un operando (suma, resta, multiplicación, división) y calcule el resultado de la operación, usando para ello la sentencia match-case.
"""
def operation(num1, num2, operator):
    match operator:
        case "+":
            print(f"{num1}{operator}{num2}={num1+num2}")
        case "-":
            print(f"{num1}{operator}{num2}={num1-num2}")
        case "*":
            print(f"{num1}{operator}{num2}={num1*num2}")
        case "/":
            print(f"{num1}{operator}{num2}={num1/num2}")
        case _:
            print("Unknown operator")

operation(5, 3, "*")

# Cordenadas
point = (6, 3)
match point:
    case (x, y):
        print(f"({x}, {y}) is in plane")
    case (x, y, z):
        print(f"({x}, {y}, {z}) is in space")

# Determinar valores enteros
point = ('2', '5')

match point:
    case (int(), int()):
        print(f'{point} is in plane')
    case (int(), int(), int()):
        print(f'{point} is in space')
    case _:
        print('Unknown!')


point = (8, 3, 5)

match point:
    case (int(x), int(y)):
        dist_to_origin = (x ** 2 + y ** 2) ** (1 / 2)
    case (int(x), int(y), int(z)):
        dist_to_origin = (x ** 2 + y ** 2 + z ** 2) ** (1 / 2)
    case _:
        print('Unknown!')

# Aquí no detecta el ocho porque no es entero
point = ('8', 3, 5)  # Nótese el 8 como "string"

match point:
    case (int(x), int(y)):
        dist_to_origin = (x ** 2 + y ** 2) ** (1 / 2)
    case (int(x), int(y), int(z)): # no trasforma es una comprobación en el case
        dist_to_origin = (x ** 2 + y ** 2 + z ** 2) ** (1 / 2)
    case _:
        print('Unknown!')

# Unknown!