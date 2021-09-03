class Area:
    def __init__(self, b, a):
        self.base = b
        self.altura = a

    def hallararea(self):
        return self.base * self.altura

objetoarea = Area(int(input("Ingrese la base: ")),
                 int(input("Ingrese la altura: ")))

print(f"El area es { objetoarea.hallararea()}")

