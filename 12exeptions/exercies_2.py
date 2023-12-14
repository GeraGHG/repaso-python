def getint() -> int:
    while True:
        try:
            num = int(input("Give me an integer number: "))
        except ValueError:
            print("Try it again!")
        else:
            print(f"Correcto tu número es {num}")
            break

getint()

def recursiva_getint() -> int:
    try:
        num = int(input("Give me a integer numbre: "))
    except ValueError:
        print("Try it again!")
        recursiva_getint()
    else:
        return num