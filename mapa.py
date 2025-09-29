#refactorizacion\mapa.py
#importamos ramdon para generar obstaculos aleatorios en el mapa 
import random

#creamos una clase mapa

class mapa:
    #tendra filas columnas como atributos de instancias
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[" . " for _ in range(columnas)] for _ in range(filas)] 
        self.inicio = None
        self.destino = None
#CREAMOS NUESTROS METODOS DE INSTANCIA
    #imprimimos nuestro tablero 
    def imprimir(self):
        for fila in self.tablero:
            print(" ".join(fila))
        #salto de linea para que se vea mejor     
        print()
        
    #aseguramos que no sea un obstaculo     
    def no_obstaculo(self, fila, columna):
        if 0 <= fila <self.filas and 0 <= columna < self.columnas:
            return self.tablero[fila][columna] in [" . ", " p ", " F "]
        return False
    
    #agregamos obstaculos
    def agregar_obstaculos(self, fila, columna, tipo):
        if 0 <= fila <self.filas and 0 <= columna < self.columnas:
            self.tablero[fila][columna] = tipo
        else: 
            print("coordenadas fuera del rango!")
            
    #modificamos nuestra celda
    def modificar_celda(self, fila, columna, tipo):
        if tipo in [" . ", " A ", " X "]:
            self.tablero[fila][columna] = tipo 
            return True
        return False
    #generamos el camino solo con el camino marcado y el camino visible
    def generar_tablero_limpio(self, camino):
        limpio = [[" . " for _ in range(self.columnas)] for _ in range(self.filas)]
        if camino:
            for f, c in camino:
                if self.tablero[f][c] == " A ":
                    limpio[f][c] = " A "
                else:
                    limpio[f][c] = " * "
            #marcar inicio y destino 
            limpio[camino[0][0]][camino[0][1]]= " P "
            limpio[camino[-1][0]][camino[-1][1]] = " F "
        return limpio        