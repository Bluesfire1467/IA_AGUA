import socket
import json

# Entrada de soneo
muestra = [{'date': '2023-11-02T06:36:52.106Z', 'level': 3, 'waterTank': 1},{'date': '2023-11-02T06:36:52.106Z', 'level': 3, 'waterTank': 2},{'date': '2023-11-02T06:36:52.106Z', 'level': 3, 'waterTank': 'Cisterna'}]
muestraJson = json.dumps(muestra)

# Envio de personas por edificio

# Conexion con socket y envio de datos
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.connect( ("localhost", 3456) )

mi_socket.sendall(muestraJson.encode())
mi_socket.close()