import string
letters_lower = string.ascii_lowercase
unique_letters = ""
isograma = "downstream"
for letter in isograma:
    if letter in unique_letters:
        print("No es un isograma")
        break
    if letter.isalpha():
        unique_letters += letter

else:
    print(f"Es un isograma {isograma}")
