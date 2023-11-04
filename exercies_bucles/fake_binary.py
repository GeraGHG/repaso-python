string_num = "670135"
new_string = ""
for char in string_num:
    if int(char) < 5:
        new_string += "0"
    if int(char) >= 5:
        new_string += "1"
print(new_string)
