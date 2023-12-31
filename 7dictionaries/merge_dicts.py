# **********************
# MEZCLANDO DICCIONARIOS
# **********************


def run(d1: dict, d2: dict) -> dict:
    merged = d1.copy()
    
    for key, value in d2.items():
        if type(key).__name__ != type(value).__name__:
            if key in merged:
                if merged[key] < value:
                    merged[key] = value
            else:
                merged[key] = value
        else:
            if key in merged:
                merged[key] = key
            else:
                merged[key] = value
    return merged



if __name__ == '__main__':
    run({'a': 1, 'b': 2}, {'a': 3, 'c': 4})