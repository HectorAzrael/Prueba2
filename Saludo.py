# saludo.py

def saludar(nombre):
    mensaje = f"Hola, {nombre}!"
    return mensaje

if __name__ == "__main__":
    nombre = input("Agrega tu nombre y apellido: ")
    print(saludar(nombre))
