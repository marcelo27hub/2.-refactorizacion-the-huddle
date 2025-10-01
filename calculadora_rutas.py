# calculadora_rutas.py
from algoritmos import AlgoritmoBusqueda  # la clase abstracta#importamos una cola de prioridad
import heapq

class CalculadoraDeRutas(AlgoritmoBusqueda):
    """Calculadora de rutas que hereda de AlgoritmoBusqueda"""
    
    #atributo de instancia
    def __init__(self, mapa):
        super().__init__(mapa)
    
    #defino mi metodo heuristica     
    def heuristica(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
    #defino los posibles movimientos que puede hacer en el tablero el algoritmo 
    def movimientos_posibles(self, nodo):
        fila, columna = nodo
        movimientos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        vecinos = []
        for df, dc in movimientos:
            nf, nc = fila + df, columna + dc
            if 0 <= nf < self.mapa.filas and 0 <= nc < self.mapa.columnas:
                celda = self.mapa.tablero[nf][nc]
                if celda in [" . ", " F "]:
                    vecinos.append(((nf, nc), 1))
                elif celda == " A ":
                    vecinos.append(((nf, nc), 1.5))
        return vecinos
    # defino mi metodo calcular ruta para saber la ruta que tomara al final 
    def calcular_ruta(self, inicio, destino):
        abiertos = []
        heapq.heappush(abiertos, (0, inicio, [inicio], 0))
        visitados = {}
        while abiertos:
            f, nodo, camino, g = heapq.heappop(abiertos)
            if nodo == destino:
                return camino
            if nodo in visitados and visitados[nodo] <= g:
                continue
            visitados[nodo] = g
            for vecino, costo in self.movimientos_posibles(nodo):
                g_nuevo = g + costo
                f_nuevo = g_nuevo + self.heuristica(vecino, destino)
                heapq.heappush(abiertos, (f_nuevo, vecino, camino + [vecino], g_nuevo))
        return None
    
    # defino mi metodo marcar mi camino
    def marcar_camino(self, camino, inicio, destino):
        for fila, col in camino:
            if (fila, col) == inicio:
                self.mapa.tablero[fila][col] = " P "
            elif (fila, col) == destino:
                self.mapa.tablero[fila][col] = " F "
            elif self.mapa.tablero[fila][col] == " . ":
                self.mapa.tablero[fila][col] = " * "                
                    
    
    