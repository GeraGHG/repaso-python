"""
while 0 <= (mark := float(input("Introduzca una nueva nota: "))) <= 10:
    print(mark)
print("Nota fuera de rango")

num_range = int(input("Ingrese un número: "))
num = 5
while num <= num_range:
    print(num, end=" ")
    num += 5


text = "Supercalifragilisticoespialidoso"
count = 0
for letter in text:
    if letter in "aeiou":
        count += 1

reducida = sum(1 for letter in text if letter in "aeiou")

print(count, reducida)


num = 11

for i in range(2, num):
    if num % i == 0: 
        print("No es primo")
        break
else:
    print("It's prime")

a = 0
print(a)
b = 1
print(b)

for _ in range(98):
    r = a + b
    a = b
    b = r
    print(r)


fibb = [0, 1]
for i in range(0, 101):
    fibb.append(fibb[i] + fibb[i + 1])
print(fibb)
"""
x = "X"
d = "D"
u = "U"
for i in range(5):
    for j in range(5):
        if i == j:
            sim = "X"
        if i < j:
            sim = "U"
        if i > j:
            sim = "D"
        print(sim, end=" ")
    print()




