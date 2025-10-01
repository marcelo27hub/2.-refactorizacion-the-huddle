# mapa.py
from obstaculos import agregar_obstaculos_usuario as agregar_obs  # importamos la función de obstaculos.py

class Mapa:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[" . " for _ in range(columnas)] for _ in range(filas)]
        self.inicio = None
        self.destino = None

    # Método para imprimir el tablero
    def imprimir_mapa(self):
        for fila in self.tablero:
            print(" ".join(fila))
        print()

    # Verifica si la celda no es obstáculo
    def no_obstaculo(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            return self.tablero[fila][columna] in [" . ", " P ", " F "]
        return False

    # Agrega un obstáculo o tipo de celda
    def agregar_obstaculo(self, fila, columna, tipo):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.tablero[fila][columna] = tipo
        else:
            print("Coordenadas fuera del rango!")

    # Modifica el tipo de celda
    def modificar_celda(self, fila, columna, tipo):
        if tipo in [" . ", " A ", " X "]:
            self.tablero[fila][columna] = tipo
            return True
        return False

    # Genera un tablero limpio mostrando solo el camino y el agua
    def generar_tablero_limpio(self, camino):
        limpio = [[" . " for _ in range(self.columnas)] for _ in range(self.filas)]
        if camino:
            for f, c in camino:
                if self.tablero[f][c] == " . ":
                    limpio[f][c] = " * "
            # marcar inicio y destino
            limpio[camino[0][0]][camino[0][1]] = " P "
            limpio[camino[-1][0]][camino[-1][1]] = " F "
        # conservar agua
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] == " A ":
                    limpio[i][j] = " A "
        return limpio


    # Método para agregar obstáculos desde la función externa
    def agregar_obstaculos_usuario(self):
        agregar_obs(self)
