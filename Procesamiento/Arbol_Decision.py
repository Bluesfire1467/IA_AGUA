import json
import time
import os

def Arbol_Desicion(data, Consumopromedio, Consumofijo, Cisterna, dataconfig):
    CisternaLvl = {"level": 438.66}
    for cisterna in dataconfig["tankers"]:
        capacidadcisterna = cisterna["capacity"]

    # Verificando que haya agua en cisterna
    if CisternaLvl["level"] < capacidadcisterna * 0.004:
        pass
    else:
        print("La cisterna esta disponible")