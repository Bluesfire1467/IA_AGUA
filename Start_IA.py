from Procesamiento import ConsumoPromedio, ConsumoFijo, Cisterna as Cis, Arbol_Decision
import socketio
import json
import os

# Variables globales
dataconfig = {}
Consumopromedio = []
Consumofijo = []
history = []
Cisterna = []
check = False

# Lee los datos desde el archivo JSON para history
current_directory = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join('Procesamiento', 'Json', 'registros.json')
with open(config_path, 'r') as file:
    data = json.load(file)
file.close()
for muestra in data:
    history.append(muestra)
# ===================================================================
sio = socketio.Client()

@sio.event
def connect():
    print('\033[92mConexión establecida\033[0m')

@sio.event
def disconnect():
    print('\033[91mDesconectado del servidor\033[0m')
    print('\033[92mGuardando datos de entrenamiento\033[0m')

@sio.on('append-new-data')
def muestras(data):
    global history, dataconfig, check, Consumopromedio, Consumofijo, Cisterna
    # Conteo muestras semanas de entrenamiento
    if (len(history) >= dataconfig["ia"]["trainingWeeks"] * len(dataconfig["buildings"]) + len(dataconfig["tankers"])) * 7 * 24:
        # Generando consumo promedio, consumo fijo, administracion de cisterna
        if (check == False):
            print("\033[92mEntrenamiento Completo\033[0m")
            Consumopromedio = ConsumoPromedio.ConsumoPromedio(history, dataconfig)
            Consumofijo = ConsumoFijo.consumo_fijo(dataconfig)
            Cisterna = Cis.Cisterna(dataconfig)
            check = True
        print(data)
        print(f"Consumo fijo por edificio: {Consumofijo}")
        print(f"Litros por edificio: {Cisterna}")

        #Ejecusion de toma de desiciones
        Arbol_Decision.Arbol_Desicion(data, Consumopromedio, Consumofijo, Cisterna, dataconfig)


    else:
        for muestra in data:
            history.append(muestra)
        print(len(history))
        print(f'Edificios:{len(dataconfig["buildings"])} Cisternas:{len(dataconfig["tankers"])}')

@sio.on('get-config')
def config(data):
    global dataconfig
    dataconfig = data
    print("\033[1;36mConfiguración recibida\033[0m")

@sio.on('reset')
def reset():
    global dataconfig, history, check
    dataconfig = {}
    history = []
    check = False

sio.connect('http://localhost:3459')
sio.wait()

# escucha on, emite
#sio.on(escucha)
#sio.emit('desicion','{'id', 'nivel'}')