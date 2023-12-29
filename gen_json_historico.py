import json
from datetime import datetime, timedelta
import random

# Función para generar registros cada hora desde el lunes a las 0:00 hasta el viernes a las 23:00
def generate_data():
    start_date = datetime(2023, 10, 23, 0, 0)  # Lunes
    end_date = datetime(2023, 11, 27, 23, 0)  # Viernes

    data = []
    current_date = start_date

    while current_date <= end_date:
        for water_tank in range(1, 4):
            record = {
                "date": current_date.isoformat() + 'Z',
                "level": generate_random_level(water_tank),
                "waterTank": water_tank
            }
            data.append(record)

        current_date += timedelta(hours=1)

    return data

# Función para generar niveles aleatorios dependiendo del tanque de agua
def generate_random_level(water_tank):
    if water_tank == 1 or water_tank == 2:
        return random.randint(1, 1100)
    else:
        return random.randint(1, 5000)

data = generate_data()

with open('registros.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Se han generado muestras cada hora desde el lunes hasta el viernes para los tres tanques de agua en el archivo 'registros.json'")
