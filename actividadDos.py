#!/usr/bin/env python3
saldo = 0;
print("¿Que deseas hacer?")
print("1 - Ingreso");
print("2 - Reintegro");
elegirOpcion = int(input("Elige una opcion (cualquier otra para terminar): "));

while elegirOpcion < 0:
if elegirOpcion == 1:
    print("Tu saldo actual es " + str(saldo));
    anadirSaldo = int(input("Introduce la cantidad: "));
    print("Has ingresado " + str(anadirSaldo) + "€, ahora tu saldo es de " + str(saldo + anadirSaldo) + "€");

elif elegirOpcion == 2:
    print("Tu saldo actual es " + str(saldo));
    retirarSaldo = int(input("Introduce la cantidad: "));
    print("Has retirado " + str(retirarSaldo) + "€ de tu cuenta. Ahora tienes " + str(saldo - retirarSaldo) + "€");
else:
    print("Opción no válida, saliendo...");