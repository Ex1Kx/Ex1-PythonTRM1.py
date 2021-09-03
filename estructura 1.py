class Semaforo:
    def __int__(self, colorsemaforo):
        self.estadosemaforo = colorsemaforo

        def mostrarestado(self):
            if self.estadosemaforo == "verde":
                return f"Puede seguir"
            elif self.estadosemaforo == "rojo":
                return f"Debe parar"
            else:
                return f"Estado en amarillo o fallando"


objetosemaforo = Semaforo("verde")

print(objetosemaforo.mostrarestado())
