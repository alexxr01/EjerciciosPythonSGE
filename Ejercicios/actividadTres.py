#!/usr/bin/env python3
sala = [['X' for j in range(4)] for i in range(5)]

reservar_mas = True

while reservar_mas:
    # Mostrar la matriz con el estado actual de las butacas
    for i in range(5):
        for j in range(4):
            print(sala[i][j], end=' ')
        print()

    # Preguntar por la fila y columna de la butaca a reservar
    fila = int(input("Introduce la fila: "))
    columna = int(input("Introduce la columna: "))

    # Comprobar si la fila y columna introducidas son válidas
    if fila < 1 or fila > 5 or columna < 1 or columna > 4:
        print("Fila o columna no válidas.")
    # Comprobar si la butaca está ocupada
    elif sala[fila-1][columna-1] == 'O':
        print("La butaca ya está ocupada.")
    # Reservar la butaca
    else:
        sala[fila-1][columna-1] = 'O'
        print("Butaca reservada.")

        # Preguntar si desea hacer otra reserva
        respuesta = input("¿Quieres hacer otra reserva? (S/N) ")
        if respuesta.upper() == 'N':
            reservar_mas = False