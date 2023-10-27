"""
USD -> CNY
"""
def usd_to_cny(dollars):
    CNY = 6.75 
    cny_amount = CNY * dollars
    cny_str = "{:.2f}".format(cny_amount)
    return f"{dollars} -> {cny_str} Chinese Yuan"

usd_amount = int(input("Enter dollars: "))
print(usd_to_cny(usd_amount))



