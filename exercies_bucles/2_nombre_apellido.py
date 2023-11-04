while True:
    if (name := input("¿Su nombre? ")) == name.title():
        break
    else:
        print("Error. Debe escribirlo correctamente")