class Dolares:
    def _init_(self, ps,):
        self.Pesos = ps
        self.Dolar = 3.54700
        self.euros = 23

    def multiplicar(self):
        return self.Pesos * self.Dolar

dolaresx = Dolares(int(input("Ingrese La Cantidad De Dolares Que Desea Convertir: ")))
print(f"La Cantidad De Dolares Es De ${dolaresx.multiplicar()} Pesos Colombianos")