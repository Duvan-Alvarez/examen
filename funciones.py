import random


def simular_datos(cantidad=200):
    clientes = ["Laura Gómez", "Carlos Pérez", "Ana Torres", "Luis Martínez", "Sofía Ramírez"]
    mascotas = ["Max", "Luna", "Rocky", "Milo", "Nina", "Toby"]
    servicios = ["Baño", "Vacunación", "Consulta general", "Desparasitación", "Corte de uñas"]
    registros = []

    for i in range(1, cantidad + 1):
        registro = {
            "id": i,
            "cliente": random.choice(clientes),
            "mascota": random.choice(mascotas),
            "servicio": random.choice(servicios),
            "costo": random.randint(20000, 100000),
            "calificacion": round(random.uniform(1, 5), 1)
        }
        registros.append(registro)

    return registros


def calcular_promedio(registros):
    suma = 0
    for r in registros:
        suma += r["calificacion"]
    return suma / len(registros)



def clasificar(calificacion):
    if calificacion >= 4.5:
        return "Excelente"
    elif calificacion >= 3.5:
        return "Buena"
    elif calificacion >= 2.5:
        return "Regular"
    else:
        return "Crítica"



def contar_clasificaciones(registros):
    conteo = {"Excelente": 0, "Buena": 0, "Regular": 0, "Crítica": 0}

    for r in registros:
        categoria = clasificar(r["calificacion"])
        conteo[categoria] += 1

    return conteo



def contar_servicios(registros):
    conteo = {}

    for r in registros:
        servicio = r["servicio"]
        if servicio in conteo:
            conteo[servicio] += 1
        else:
            conteo[servicio] = 1

    return conteo



def mejor_servicio(registros):
    suma_servicios = {}
    conteo_servicios = {}

    for r in registros:
        servicio = r["servicio"]
        calificacion = r["calificacion"]

        if servicio not in suma_servicios:
            suma_servicios[servicio] = 0
            conteo_servicios[servicio] = 0

        suma_servicios[servicio] += calificacion
        conteo_servicios[servicio] += 1

    promedios = {}
    for servicio in suma_servicios:
        promedios[servicio] = suma_servicios[servicio] / conteo_servicios[servicio]

    mejor = max(promedios, key=promedios.get)
    return mejor, promedios[mejor]



def mostrar_resumen(total, promedio, clasificaciones, servicios, mejor_servicio, registros):
    print("\n--- RESUMEN GENERAL ---")

    print(f"Total de registros: {total}")
    print(f"Promedio general de satisfacción: {promedio:.2f}")

    print("\nAtenciones por clasificación:")
    for categoria, cantidad in clasificaciones.items():
        print(f"  {categoria}: {cantidad}")

    print("\nAtenciones por servicio:")
    for servicio, cantidad in servicios.items():
        print(f"  {servicio}: {cantidad}")

    print(f"\nServicio mejor calificado: {mejor_servicio[0]} ({mejor_servicio[1]:.2f})")

    print("\nEjemplos de registros:")
    for r in registros[:3]:
        print(f"  ID {r['id']}: {r['cliente']} - {r['mascota']} - {r['servicio']} - ${r['costo']} - {r['calificacion']}")

