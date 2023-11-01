
def if_check(letter1: str, letter2: str):
    if letter1.isalpha() and letter2.isalpha():
        if (letter1.islower() and letter2.islower()) or (letter1.isupper() and letter2.isupper()):
            return 1
        else:
            return 0
        
    else: 
        return -1
print(if_check("B", "g"))