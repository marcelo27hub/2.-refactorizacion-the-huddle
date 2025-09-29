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

            
        

