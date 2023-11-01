dict_countries = {"Italia": "🇮🇹", "México": "🇲🇽", "España": "🇪🇸", "Estados Unidos": "🇺🇸"}


country = input("Ingrese el nombre del país: ")
if country in dict_countries:
    print(dict_countries[country])