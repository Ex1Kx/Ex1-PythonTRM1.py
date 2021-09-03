class Sumatoria:
    def __init__(self, num1, num2):
        self.numeroUno = num1
        self.numeroDos = num2
        
    def sumar(self):
        return self.numeroUno + self.numeroDos
    
objetosuma = Sumatoria(int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo numero: ")))
print(f"La suma de estos numeros es { objetosuma.sumar()}")

        
        
        