# main.py
from mapa import Mapa
from input_usuario import UsuarioEntrada
from calculadora_rutas import CalculadoraDeRutas
import copy

def main():
    print("BIENVENIDOS AL BUSCADOR DE RUTAS")
    print(".: Camino libre")
    print("A: Agua")
    print("X: Obstáculo")

    while True:
        try:
            filas = int(input("Ingrese cantidad de filas: "))
            columnas = int(input("Ingrese cantidad de columnas: "))
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Crear mapa
    mapa = Mapa(filas, columnas)
    mapa.agregar_obstaculos_usuario()

    print("\nTablero con obstáculos:")
    mapa.imprimir_mapa()

    # Entrada de inicio y destino
    inicio = UsuarioEntrada.pedir_coordenadas("Inicio", mapa)
    destino = UsuarioEntrada.pedir_coordenadas("Destino", mapa)

    # Guardamos una copia limpia con obstáculos y agua, sin camino
    mapa_base = copy.deepcopy(mapa.tablero)

    # Creamos calculadora
    calculadora = CalculadoraDeRutas(mapa)
    camino = calculadora.calcular_ruta(inicio, destino)

    if camino:
        # Resetear tablero base y marcar el camino
        mapa.tablero = copy.deepcopy(mapa_base)
        calculadora.marcar_camino(camino, inicio, destino)
        mapa_limpio = mapa.generar_tablero_limpio(camino)
    else:
        print("No se encontró camino entre inicio y destino.")
        mapa_limpio = None

    while True:
        print("\nOpciones:")
        print("1: Mostrar tablero completo con obstáculos y camino")
        print("2: Mostrar solo el camino más corto limpio")
        print("3: Agregar o cambiar obstáculos y recalcular camino")
        print("4: Crear un nuevo tablero")
        print("5: Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mapa.imprimir_mapa()

        elif opcion == "2":
            if mapa_limpio:
                for fila in mapa_limpio:
                    print(" ".join(fila))
            else:
                print("No hay camino calculado aún.")

        elif opcion == "3":
            fila = int(input(f"Fila (1-{filas}): ")) - 1
            columna = int(input(f"Columna (1-{columnas}): ")) - 1
            print("Tipos de celda disponibles:")
            print(" . -> Camino libre")
            print(" A -> Agua")
            print(" X -> Obstáculo")
            tipo = f" {input('Ingrese el tipo de celda: ').strip().upper()} "

            if mapa.modificar_celda(fila, columna, tipo):
                # Resetear tablero base y recalcular
                mapa.tablero = copy.deepcopy(mapa_base)
                camino = calculadora.calcular_ruta(inicio, destino)
                if camino:
                    calculadora.marcar_camino(camino, inicio, destino)
                    mapa_limpio = mapa.generar_tablero_limpio(camino)
                    print("Camino recalculado con los nuevos obstáculos:")
                    mapa.imprimir_mapa()
                else:
                    mapa_limpio = None
                    print("No se encontró camino. Intenta desbloquear otra celda.")
                # Actualizar la base con los cambios de obstáculos
                mapa_base[fila][columna] = tipo
            else:
                print("Tipo de celda inválido.")

        elif opcion == "4":
            return main()  # Reinicia el programa

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
