import random

def agregar_obstaculo(mapa, fila, columna, tipo):
    mapa.agregar_obstaculo(fila, columna, tipo)

def agregar_obstaculos_usuario(mapa):
    tipos = {" A ": "Agua", " X ": "Obstáculo"}
    for tipo, nombre in tipos.items():
        try:
            cantidad = int(input(f"Ingrese cantidad de {nombre}: "))
        except ValueError:
            print("Número inválido, se usará 0")
            cantidad = 0
        puestos = 0
        while puestos < cantidad:
            fila = random.randint(0, mapa.filas - 1)
            columna = random.randint(0, mapa.columnas - 1)
            if mapa.tablero[fila][columna] == " . ":
                mapa.agregar_obstaculo(fila, columna, tipo)
                puestos += 1
