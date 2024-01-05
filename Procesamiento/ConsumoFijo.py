import json
import os

def consumo_fijo(dataconfig):
    edificiosConsumoFijo = []
    for edificio in dataconfig["buildings"]:
        edificiosConsumoFijo.append(edificio["residents"] * 100)

    print("\033[92m**Consumo fijo generado**\033[0m")
    return edificiosConsumoFijo
