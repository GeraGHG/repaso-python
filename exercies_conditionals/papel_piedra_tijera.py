def juego(jugador1, jugador2):
    if jugador1 == jugador2:
        return f"Empate"
    
    if jugador1 == "piedra" and jugador2 == "papel":
        return f"Gana persona2: El papel envuelve a la piedra"
    elif jugador1 == "papel" and jugador2 == "piedra":
        return f"Gana persona1: El papel envuelve a la piedra"
    
    if jugador1 == "piedra" and jugador2 == "tijera":
        return f"Gana persona1: La piedra rompe la tijera"
    elif jugador1 == "tijera" and jugador2 == "piedra":
        return  f"Gana persona2: La piedra rompe la tijera"
    
    if jugador1 == "papel" and jugador2 == "tijera":
        return f"Gana persona2: Tijera corta papel"
    elif jugador1 == "tijera" and jugador2 == "papel":
        return f"Gana persona1: Tijera corta papel"
    
    

def menu():
    while True:
        print("\nEscriba su opción (piedra, papel o tijera)")
        print("Si desea salir tecleé \"q\" para ambos jugadores\n")
        opcion1 = input("Persona 1: ¿Cúal es su jugada? ").lower()
        opcion2 = input("Persona 2: ¿Cúal es su jugada? ").lower()
        print()
        if opcion1 == "q" and opcion2 == "q":
            print("\nGracias por jugar ;)")
            break
        resultado = juego(opcion1, opcion2)
        print(resultado)


menu()
