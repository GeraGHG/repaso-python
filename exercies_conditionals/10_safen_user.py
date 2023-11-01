def safen_input(text: str) -> str:
    new_text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    
    return new_text

code = input("Enter your text: ")
resultado = safen_input(code)
print(resultado)