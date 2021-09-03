class Notas:
    def __init__(self, nota):
        self.calificacion = nota

    def mostraraprobacion(self):
        if self.calificacion > 3.2:
             return f"Aprendiz aprobo"
        elif self.calificacion < 3.2:
            return f"El aprendiz no aprobo"
        else:
             return f"Ingrese una nota valida"

 objetonota = Notas (float(input("Ingrese la nota: ")))
print(objetonota.mostraraprobacion())
