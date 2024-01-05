import pandas as pd
import matplotlib.pyplot as plt
import json

# Cargar el archivo JSON con los datos
with open('Json/ConsumoPromedio.json', 'r') as file:
    data = json.load(file)

dia = input("Que dia deseas ver?: ")
tinaco = int(input("Que tinaco deseas ver?"))

# Filtrar los datos para el Water Tank 1 solamente
tank_1_data = [entry for entry in data if entry['waterTank'] == tinaco and entry['weekday'] == dia]

# Crear listas para almacenar las horas y niveles del Water Tank 1
hours = []
level_tank_1 = []

# Ordenar los datos filtrados por hora y almacenar en las listas correspondientes
for entry in tank_1_data:
    hours.append(entry['hour'])
    level_tank_1.append(entry['level'])

# Graficar los niveles del Water Tank 1
plt.figure(figsize=(10, 6))
plt.plot(hours, level_tank_1, marker='o', linestyle='-', color='blue')
plt.title(f'Nivel promedio del Water Tank {tinaco} el día {dia}')
plt.xlabel('Hora del día')
plt.ylabel('Nivel del tanque')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Mostrar la gráfica del Water Tank 1
plt.show()