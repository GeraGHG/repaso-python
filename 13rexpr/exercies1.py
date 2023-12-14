import re
from pathlib import Path
# Here let's do the exercie

with open("13rexpr/text.txt", "r") as file:
	text = file.read()

expretion = r"\w+@[a-zA-Z]+\.com"


# all matches
result = re.findall(expretion, text)
print(result)


# Exercies 2
sentence = """
Carlos Arturo	
449 123 45 67
carlos_@hotmail.com
www.carlos.com

Manuel Alejandro
448-234-56-78
alejandro@outlook.com
https://www.manuel.alejandro.com.mx
http://alejandro.com.mx

Cesar Alan
449 345 67 89
cesar@hotmail.com
cesar.net
"""
numbers = r"\d{3}[\s-]\d{3}[\s-]\d{2}[\s-]\d{2}"
result = re.findall(numbers, sentence)

print([number.replace("-", " ") for number in result])



