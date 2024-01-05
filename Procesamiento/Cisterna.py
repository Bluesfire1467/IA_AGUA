import json
import os

def Cisterna(dataconfig):
    # Numero de personas total
    personas = 0
    for edificios in dataconfig["buildings"]:
        personas = personas + edificios["residents"]

    # Litros por persona
    capacidadcisterna = 0
    for cisterna in dataconfig["tankers"]:
        capacidadcisterna = cisterna["capacity"]
    litrosPersona = capacidadcisterna / personas

    # Litros por edificio
    litrosEdificio = []
    for edificios in dataconfig["buildings"]:
        litrosEdificio.append(edificios["residents"] * litrosPersona)

    print("\033[92m**Litros por edificio asignados**\033[0m")

    return litrosEdificio
