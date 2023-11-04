import random
numero_random = random.randint(1, 100)
intentos = 1
while True:
    num_user = int(input("\nIntroduze un número: "))
    if num_user == numero_random:
        print(f"✅ ¡Enhorabuena! Has encontrado el número en {intentos} intentos")
        break
    if numero_random > num_user:
        print("Mayor")
    else:
        print("Menor")
    intentos += 1
