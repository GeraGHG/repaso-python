string = "OSI"
final = ""
for char in string:
    index = string.find(char)
    if char == "S":
        final += "5" 
    elif char == "O":
        final += "0"
    elif char == "I":
        final += "1"
    else:
        final += char
print(final)
