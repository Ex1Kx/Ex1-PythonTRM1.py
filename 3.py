class Recarga:
    def __init__(self, ce, vr):
        self.numerodecelular = ce
        self.valorrecarga = vr
        self.valorminuto = 100

    def mostrarminutos(self):
        return self.valorrecarga / self.valorminuto

        def __str__(self):
            return f"Hola, su recarga ha sido exitosa para el numero:  "


objetorecarga = Recarga(input("Ingrese numero de celular: "), int(input("Ingrese valor de la recarga: ")))
print(f"{ objetorecarga.__str__()} los minutos asignados son: "
    f"{objetorecarga.mostrarminutos()}")
