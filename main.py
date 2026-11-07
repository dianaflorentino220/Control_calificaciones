from modulo_entrada import solicitar_datos

from modulo_proceso import calcular_promedio, determinar_estado


def main():

    print("================================")
    print("   SISTEMA DE CALIFICACIONES")
    print("================================")

    nombre, calificaciones = solicitar_datos()

    promedio = calcular_promedio(calificaciones)

    estado = determinar_estado(promedio)

    print("\n========== RESULTADOS ==========")

    print("Nombre del estudiante:", nombre)

    print("Cantidad de calificaciones:", len(calificaciones))

    print("Calificaciones:", calificaciones)

    print("Promedio final:", round(promedio, 2))

    print("Estado académico:", estado)

    print("================================")


if __name__ == "__main__":
    main()