import random
import string

# https://symbl.cc/en/  
# es la página de todos los emojis y otros símbolos que ya están agregados UTF-8
"""
recreational_vehicle = 0x1F699
recreational_vehicle = chr(recreational_vehicle)
print(recreational_vehicle)
print("\N{ROCKET}")
print("\N{Grinning Face}")
value = 0x1F600
print(f"{chr(value)}")
"""
happy = "\N{Grinning Face}"
neutral = "\N{Neutral Face}"
sad = "\N{Disappointed Face}"

numbers = string.digits
opcion = random.choice(numbers)
for _ in range(5):
    opcion = random.choice(numbers)
    if 0 <= int(opcion) <= 4:
        print(sad)
    elif 5 <= int(opcion) <= 7:
        print(neutral)
    else:
        print(happy)



"""
e = 2.71828
print(f"{e:.3f}")
print(f"{e:f}")
print(f"{e:8f}")
print(f"{e:e}")
print(f"{e:19f}")
print(f"{e:07.2f}")
"""