path = "C:/Users/Germanico/Documents/python_repaso/modules_practices/canary-iata.dat"
canary_iata = ('TFN\n', 'TFS\n', 'LPA\n', 'GMZ\n', 'VDE\n', 'SPC\n', 'ACE\n', 'FUE\n')
f = open(path, "w")


# f.write("\n".join(canaru_iata)) Cuando no exista separación 
f.writelines(canary_iata)


f.close()