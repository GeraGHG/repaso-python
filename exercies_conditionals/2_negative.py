class Number:
    def MakeNegative(self, num):
        if num == 0:
            return num
        if num < 0:
            return num
        else:
            return num * -1

Kata = Number()
print(Kata.MakeNegative(-9))


    
