def solicitar_datos():
    nombre = input("Ingrese el nombre del estudiante: ")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de calificaciones (máximo 4): "))

            if 1 <= cantidad <= 4:
                break
            else:
                print("Error: debe ingresar entre 1 y 4 calificaciones.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    calificaciones = []

    for i in range(cantidad):
        while True:
            try:
                nota = float(input(f"Ingrese la calificación {i + 1}: "))

                if 0 <= nota <= 100:
                    calificaciones.append(nota)
                    break
                else:
                    print("Error: la calificación debe estar entre 0 y 100.")

            except ValueError:
                print("Error: debe ingresar una calificación válida.")

    return nombre, calificaciones