from math import pi
class areaperimetro:
    def __init__(self, mn):
        self.menu = mn
    def areacirculo(self):
        radio = float(input("Ingrese el radio del circulo del que desea conocer el area: "))
        area = pi * (radio ** 2)
        print(f"El area del circulo en m es de {area}")
    def perimetrocuadrado(self):
        ladox = float(input("Ingrese uno de los lados del cuadrado del que desea conocer el perimetro: "))
        perimetro = ladox * 4
        print(f"El perimetro del cuadrado en m es {perimetro}")
objetoareaperimetro = areaperimetro(int(input("Si desea hallar el area de un circulo, presione 1: \n"
                                              "Si desea hallar el perimetro de un cuadrado, presione 2: \n = ")))
if objetoareaperimetro.menu == 1:
    print(objetoareaperimetro.areacirculo())
elif objetoareaperimetro.menu == 2:
    print(objetoareaperimetro.perimetrocuadrado())