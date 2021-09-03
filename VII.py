def teclas():
    print("Como se llama?")
    nombre = input()
    print(f"Me alegro de conocerte {nombre}")

teclas()

def convertir():
    cantidad = float(input("Digame una cantidad en pesos: "))
    print(f"{cantidad}pesos equivalen a {round(cantidad * 2900.25)} dolares")
