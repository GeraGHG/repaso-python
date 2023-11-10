url = """C:/Users/Germanico/Documents/python_repaso/modules_practices/temps.dat"""
f = open(url, "r")
#print(f.readline().strip()) # hay que eliminar el salto de linea
print(f.readlines()) # ['23 29\n', '23 31\n', '26 34\n', '23 33\n', '22 29\n', '22 28\n', '22 28']
f.close()