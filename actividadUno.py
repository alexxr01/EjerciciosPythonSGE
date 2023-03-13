#!/usr/bin/env python3

def dibujar_tablero(tablero):
    print("\n")
    print("\t   |   |")
    print("\t {} | {} | {}".format(tablero[0], tablero[1], tablero[2]))
    print("\t___|___|___")
    print("\t   |   |")
    print("\t {} | {} | {}".format(tablero[3], tablero[4], tablero[5]))
    print("\t___|___|___")
    print("\t   |   |")
    print("\t {} | {} | {}".format(tablero[6], tablero[7], tablero[8]))
    print("\t   |   |")
    print("\n")

def comprobar_ganador(tablero, jugador):
    # Comprobar filas
    for i in range(0, 9, 3):
        if tablero[i] == tablero[i+1] == tablero[i+2] == jugador:
            return True

    # Comprobar columnas
    for i in range(3):
        if tablero[i] == tablero[i+3] == tablero[i+6] == jugador:
            return True

    # Comprobar diagonales
    if tablero[0] == tablero[4] == tablero[8] == jugador:
        return True
    elif tablero[2] == tablero[4] == tablero[6] == jugador:
        return True

    return False

def juego():
    tablero = [" " for i in range(9)]
    jugador = "X"
    jugar = True

    while jugar:
        dibujar_tablero(tablero)
        print("Es el turno del jugador", jugador)

        posicion = input("Elige una posición del 1-9: ")

        try:
            posicion = int(posicion)
            if 1 <= posicion <= 9:
                if tablero[posicion-1] == " ":
                    tablero[posicion-1] = jugador

                    if comprobar_ganador(tablero, jugador):
                        dibujar_tablero(tablero)
                        print("El jugador", jugador, "ha ganado!")
                        jugar = False
                    else:
                        if " " not in tablero:
                            dibujar_tablero(tablero)
                            print("Empate!")
                            jugar = False
                        else:
                            jugador = "O" if jugador == "X" else "X"
            else:
                print("Por favor, introduce un número del 1-9")
        except ValueError:
            print("Por favor, introduce un número del 1-9")

if __name__ == "__main__":
    juego()
