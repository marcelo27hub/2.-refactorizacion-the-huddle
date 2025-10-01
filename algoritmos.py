# algoritmos.py
from abc import ABC, abstractmethod

class AlgoritmoBusqueda(ABC):
    def __init__(self, mapa):
        self.mapa = mapa

    @abstractmethod
    def calcular_ruta(self, inicio, destino):
        pass
