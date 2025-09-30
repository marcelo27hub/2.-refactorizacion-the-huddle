#creo una clase para que el usuario pueda interactuar con la consola

class UsuarioEntrada:
    
    @staticmethod
    def pedir_coordenadas(mensaje, mapa):
        while True:
            try:
                fila = int(input(F"ingrese fila de {mensaje}(1-{mapa.filas}): ")) 
                columna = int(input(F"ingrese columna de {mensaje}(1-{mapa.columnas}): "))
            except ValueError:
                print("Ingresaste algo que no es un numero entero, intenta de nuevo!")
                continue
            if 0 <= fila < mapa.filas and 0 <= columna < mapa.columnas:
                if mapa.tablero[fila][columna] == " . ":
                    return (fila, columna)
                else:
                    print("Celda ocupada por un obstáculo")
            else:
                print("Coordenadas fuera del tablero, intenta de nuevo!")             
    