"""
RECUERDA AÑADIR DATOS EN TIPO STR() no se pueden agregar caracteres enteros INT(), FLOAT(), COMPLEX()
"""

# f = open("""C:/Users/Germanico/Documents/python_repaso/modules_practices/canary-iata.dat""", "a")
# f.write("23 40" + "\n")
# f.close()

# CORRECIÓN
# Ruta del archivo
path = "C:/Users/Germanico/Documents/python_repaso/modules_practices/canary-iata.dat"

# Lista para almacenar las líneas que no deseas eliminar
lineas_mantener = []

# Abre el archivo en modo lectura
with open(path, "r") as f:
    for line in f.readlines():
        # Verifica si la línea no coincide con "23 40"
        if line.strip() != "23 40":
            # Si no coincide, agrega la línea a la lista de líneas a mantener
            lineas_mantener.append(line)

# Abre el archivo en modo escritura para guardar solo las líneas que deseas mantener
with open(path, "w") as f:
    # Escribe las líneas que deseas mantener
    f.writelines(lineas_mantener)

