def uni_total(text: str):
    total = 0           # return sum(ord(char) for char in text)
    for char in text:  
        total += ord(char)
    return total

print(uni_total("aaa"))