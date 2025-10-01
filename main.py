# main.py
from mapa import Mapa
from calculadora_rutas import CalculadoraDeRutas
from input_usuario import UsuarioEntrada

def main():
    print("BIENVENIDOS AL BUSCADOR DE RUTAS")
    print(".: Camino libre\nA: Agua\nX: Obstáculo")

    filas = int(input("Ingrese cantidad de filas: "))
    columnas = int(input("Ingrese cantidad de columnas: "))
    mapa = Mapa(filas, columnas)
    mapa.agregar_obstaculos_usuario()
    
    print("\nTablero con obstáculos:")
    mapa.imprimir_mapa()

    inicio = UsuarioEntrada.pedir_coordenadas("Inicio", mapa)
    destino = UsuarioEntrada.pedir_coordenadas("Destino", mapa)

    calculadora = CalculadoraDeRutas(mapa)
    camino = calculadora.calcular_ruta(inicio, destino)

    if camino:
        calculadora.marcar_camino(camino, inicio, destino)
        mapa_limpio = mapa.generar_tablero_limpio(camino)
    else:
        mapa_limpio = None
        print("No se encontró camino.")

    while True:
        print("\nOpciones:")
        print("1: Mostrar tablero completo con obstáculos y camino")
        print("2: Mostrar solo el camino más corto limpio")
        print("3: Agregar o cambiar obstáculos y recalcular camino")
        print("4: Crear un nuevo tablero")
        print("5: Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if camino:
                calculadora.marcar_camino(camino, inicio, destino)
            mapa.imprimir_mapa()

        elif opcion == "2":
            if camino:
                mapa_limpio = mapa.generar_tablero_limpio(camino)
                for fila in mapa_limpio:
                    print(" ".join(fila))
            else:
                print("No hay camino calculado aún.")

        elif opcion == "3":
            fila = int(input(f"Fila (1-{mapa.filas}): ")) - 1
            columna = int(input(f"Columna (1-{mapa.columnas}): ")) - 1
            print("Tipos de celda disponibles:\n . -> Camino libre\n A -> Agua\n X -> Obstáculo")
            tipo = input("Ingrese el tipo de celda: ").strip().upper()
            tipo = f" {tipo} "
            if mapa.modificar_celda(fila, columna, tipo):
                camino = calculadora.calcular_ruta(inicio, destino)
                if camino:
                    calculadora.marcar_camino(camino, inicio, destino)
                    print("Camino recalculado con los nuevos obstáculos.")
                else:
                    mapa_limpio = None
                    print("No se encontró camino.")
            else:
                print("Tipo de celda inválido.")

        elif opcion == "4":
            filas = int(input("Ingrese cantidad de filas: "))
            columnas = int(input("Ingrese cantidad de columnas: "))
            mapa = Mapa(filas, columnas)
            mapa.agregar_obstaculos_usuario()
            mapa.imprimir_mapa()
            inicio = UsuarioEntrada.pedir_coordenadas("Inicio", mapa)
            destino = UsuarioEntrada.pedir_coordenadas("Destino", mapa)
            calculadora = CalculadoraDeRutas(mapa)
            camino = calculadora.calcular_ruta(inicio, destino)
            if camino:
                calculadora.marcar_camino(camino, inicio, destino)
                mapa_limpio = mapa.generar_tablero_limpio(camino)
            else:
                mapa_limpio = None
                print("No se encontró camino.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
