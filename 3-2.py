class Tabla1:
    def __int__(self, numerotabla: int):
        self.numerotabla = numerotabla
        self.hasta = final

    def imprimirtabla(self):
        for i in range(self.inicio, self.hasta+1):
            print(f"{self.numerotabla} x {i} = {self.numerotabla*i}")


objetotabla = Tabla1(int(input("Numero de tabla: ")), int(input("Hasta: ")))
objetotabla.imprimirtabla()
