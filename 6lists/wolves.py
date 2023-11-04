# **************
# EL LOBO ACECHA
# **************

def run(farm):       # 3, -1, -1
    for i in range(len(farm) - 1, -1, -1):
        if farm[i] == 'lobo':  # 2
            if i == len(farm) - 1:
                return "No te quiero ver más por aquí, lobo"
            else:                        # 3 - 2 
                return f"Cuidado oveja {len(farm) - 1 - i}, el lobo te va a comer"

if __name__ == '__main__':
    run(['oveja', 'oveja', 'lobo', 'oveja'])