num1 = 12
num2 = 44

if num1 < num2:
    menor = num1
else:
    menor = num2

mcd = 1
for i in range(1, menor+1):
    if num1 % i == 0 and num2 % i == 0:
        mcd = i

print(mcd)
