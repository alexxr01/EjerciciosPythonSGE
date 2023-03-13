#!/usr/bin/env python3

saldo = 0
operaciones = []

while True:
    print("1. Ingreso")
    print("2. Reintegro")
    print("3. Salir")
    opcion = input("¿Qué deseas hacer? = ")
    if opcion == "1":
        cantidad = float(input("Cantidad a ingresar: "))
        saldo += cantidad
        operaciones.append(cantidad)
    elif opcion == "2":
        cantidad = float(input("Cantidad a reintegrar: "))
        if saldo >= cantidad:
            saldo -= cantidad
            operaciones.append(-cantidad)
        else:
            print("Saldo insuficiente. No se puede realizar el reintegro.")
    elif opcion == "3":
        print("\nHas salido del programa.")
        print("Finalmente quedas con", saldo, "€ en tu cuenta.")
        break;
    else:
        break  # Terminar el bucle si la opción no es válida
    
    print("\nActualmente cuentas con", saldo, "€ en tu cuenta.\n")

# Crear las listas de ingresos y reintegros
ingresos = [cantidad for cantidad in operaciones if cantidad > 0]
reintegros = [-cantidad for cantidad in operaciones if cantidad < 0]

# Mostrar las listas de ingresos y reintegros
print("Ingresos: ", ingresos)
print("Reintegros: ", reintegros)
