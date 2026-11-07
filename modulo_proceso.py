def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio


def determinar_estado(promedio):
    if promedio >= 70:
        return "Aprobado"
    else:
        return "Reprobado"