def escribir():
    nombre = input("Escriba su nombre: ")
    ruta = "D:\prueba.txt"
    with open (ruta, mode="a", encoding="utf-8") as fichero:
        fichero.write(nombre + " ")


def leer():
    with open('D:\prueba.txt', 'r') as fichero:
        content = fichero.read()
    print(content)

escribir()
leer()