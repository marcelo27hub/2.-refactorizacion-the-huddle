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
            
                
                
        