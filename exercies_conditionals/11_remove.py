def remove(text: str):
    if text.endswith("!"):
        return text[:-1]
    else:
        return text

print(remove("Hi!"))
print(remove("Hi!!!"))
print(remove("!Hi"))
        
