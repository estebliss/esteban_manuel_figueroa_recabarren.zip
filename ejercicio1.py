cantidad = 0

while cantidad <= 0:
    try:
        cantidad = int(input("Ingrese la cantidad de cientificos que desea registrar: "))
        if cantidad <= 0:
            print("Dato de investigacion invalido. Ingrese un entero positivo para continuar el registro.")
    except ValueError:
         print("Dato de investigacion invalido. Ingrese un entero positivo para continuar el registro.")

principales = 0
asistentes = 0

for i in range(cantidad):
    print("\nRegistro del cientifico", i + 1)

    id_cientifico = ""

    while len(id_cientifico) < 6 or any(c.isspace() for c in id_cientifico):
        id_cientifico = input("Ingrese el ID del cientifico: ")

        if len(id_cientifico) <6:
            print("Error: El ID debe tener al menos 6 caracteres.")
        elif any(c.isspace() for c in id_cientifico):
            print("Error: El ID no debe contener espacios.")

    publicaciones = 0

    while publicaciones <= 0:
        try:
            publicaciones = int(input("Ingrese el numero de publicaciones: "))

            if publicaciones <=0:
                print("Error de registro, ingresa un numero entero positivo para el numero de publicaciones.")
        except ValueError:
            print("Error de registro.  Ingresa un numero entero positivo para el numero de publiciones.")

    if publicaciones > 10:
        print("Clasificacion: Investigador Principal.")
    else:
        print("Clasificacion: Investigador Asistente")
        asistentes += 1

print("\n==== RESUMEN FINAL ====")
print("Total de cientificos registrados:", cantidad)        
print("Investigadores Principales:", principales)        
print("Investigadores Asistentes:", asistentes)        

print(f"El instituto cuenta con {principales} investigadores Principales y {asistentes} Investigadores Asiste10ntes. Ciencia en marcha!")        