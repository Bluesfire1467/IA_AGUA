import socket
import json
from Arbol.Arbol_Decision import IA


# Este ejecutable inicia el procesamiento


mi_socket = socket.socket()
mi_socket.bind( ('localhost',8000) )

# Cantidad de peticiones en cola
mi_socket.listen(5)

while True:
    # Acepta peticiones
    conexion, direccion = mi_socket.accept()
    #print(f"Coneccion establecida con: {direccion}")

    entrada = conexion.recv(4096).decode()
    decision = received_dict = json.loads(entrada)

    # Mostrar el diccionario recibido


    # Cerrar la conexión
    conexion.close()


def cisterna_data():
