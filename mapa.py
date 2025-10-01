from obstaculos import agregar_obstaculos_usuario as agregar_obs

class Mapa:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[" . " for _ in range(columnas)] for _ in range(filas)]
        self.inicio = None
        self.destino = None

    def imprimir_mapa(self):
        for fila in self.tablero:
            print(" ".join(fila))
        print()

    def no_obstaculo(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            return self.tablero[fila][columna] in [" . ", " P ", " F "]
        return False

    def agregar_obstaculo(self, fila, columna, tipo):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.tablero[fila][columna] = tipo
        else:
            print("Coordenadas fuera del rango!")

    def modificar_celda(self, fila, columna, tipo):
        if tipo in [" . ", " A ", " X "]:
            self.tablero[fila][columna] = tipo
            return True
        return False

    def generar_tablero_limpio(self, camino):
        limpio = [[" . " for _ in range(self.columnas)] for _ in range(self.filas)]
        if camino:
            for f, c in camino:
                limpio[f][c] = " * "
            limpio[camino[0][0]][camino[0][1]] = " P "
            limpio[camino[-1][0]][camino[-1][1]] = " F "
        return limpio

    def agregar_obstaculos_usuario(self):
        agregar_obs(self)
