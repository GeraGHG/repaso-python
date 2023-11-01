def if_donar(edad, peso, latidos_m, plaquetas):
    if (18 <= edad <= 65) and peso > 50 and 50 <= latidos_m <= 110  and plaquetas > 150_000: 
        print("Apto para donar sangre")
    else:
        print("No apto para donar sangre")