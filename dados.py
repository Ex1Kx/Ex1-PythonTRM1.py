import random
resultado = random.randint(1,6)
class Dados:
    def __init__(self, numda: range(6)):
        self.numeroDados = numda

    def resultados(self):
        while self.numeroDados < 6:
            return f"Dame un numero entre el 1 y el 6"
            if self.numeroApuesta == resultado:
                return f"Felicidades ha ganado"
            else:
                return f"Mala suerte has perdido"
        if self.numeroApuesta < 0 or self.numeroApuesta > 6:
            print(f"Esta incorrecto intentelo de nuevo")

apuestadados = Dados(int(input("Ingrese el número al que desea apostar: ")))
print(f"El resultado es {resultado}")
print(apuestadados.resultados())
while True:
    x = input("Presione a para apostar nuevamente o b para salir: \n")
    if x == 'a':
        continue
    elif x == 'b':
        break
    else:
        print (f"Presiona a o b")