from funciones import (
    simular_datos,
    calcular_promedio,
    contar_clasificaciones,
    contar_servicios,
    mejor_servicio,
    mostrar_resumen
)

def main():
    # 1. Generar datos
    registros = simular_datos(200)

    # 2. Validación básica (similar a tu ejemplo)
    if registros:

        # 3. Procesamiento
        promedio = calcular_promedio(registros)
        clasificaciones = contar_clasificaciones(registros)
        servicios = contar_servicios(registros)
        mejor = mejor_servicio(registros)

        # 4. Salida
        mostrar_resumen(
            len(registros),
            promedio,
            clasificaciones,
            servicios,
            mejor,
            registros
        )

if __name__ == "__main__":
    main()
