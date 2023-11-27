class Droid:
    def __init__(self, name: str, serial_number: int):
        self.name = name
        self.serial_number = serial_number

    def __eq__(self, droid: Droid) -> bool:
        return self.name == droid.name
    
droid1 = Droid("C-3PO", 23)
droid2 = Droid("C-3PO", 25)
print(droid1 == droid2) 