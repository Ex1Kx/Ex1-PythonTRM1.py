class Tabla1:
    def __int__(self, numerotabla: int):
        self.numerotabla = numerotabla

    def imprimirtabla(self):
        for i in range(10):
            print(f"{self.numerotabla} x {i} = {self.numerotabla*i}")


objetotabla = Tabla1(int(input("Numero de tabla: ")))
objetotabla.imprimirtabla()
