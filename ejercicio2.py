disponibles = 20
historial = 0
opcion = 0

print ("Bienvenido al sistema de gestion de equipos del laboratorio central de investigacion!")

while opcion != 5:

    print("\n==== MENU PRINCIPAL ====")
    print("1. Equipos disponibles")
    print("2. Asignar equipo")
    print("3. Liberar equipo")
    print("4. Historial de usos")
    print("5. Salir")

    try:
        opcion = int(input("\nSeleccione una opcion: "))

        if opcion == 1:
            print("Equipos disponbles:", disponibles)

        elif opcion == 2:
            if disponibles > 0:
                cantidad = int(input("Ingrese la cantidad de equipos disponibles."))

                if cantidad <= 0:
                    print("Error: La cantidad debe ser mayor a 0.")
                elif cantidad > disponibles:
                    print("Error: No hay suficientes equipos.")
                else:
                    disponibles = disponibles - cantidad
                    historial = historial + cantidad
                    print("Equipos asignados correctamente.")
                    print("Equipos disponibles", disponibles)
            else:
                print("No hay equipos disponibles.")
        elif opcion == 3:
            cantidad = int(input("Ingrese la cantidad de equipos a liberar: "))

            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor  a 0.")
            elif disponibles + cantidad > 20:
                print("Error: No se puede superar el maximo de 20 equpos.")
            else:
                disponibles = disponibles + cantidad
                historial = historial - cantidad
                print("Equipos liberados correctamente.")
                print("Equipos disponibles", disponibles)
        elif opcion == 4:
            print("Total de equipos asignados actualmente", historial)

        elif opcion == 5:
            print("Gracias por utilizar nuestro software, hasta la proxima.")

        else:
            print("Opcion invalida, intente nuevamente.")
    except ValueError:
        print("Error: Debe ingresar un numero entero")             