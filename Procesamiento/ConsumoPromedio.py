import pandas as pd
import json
import os

def ConsumoPromedio(history, dataconfig):
    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame(history)

    # Convertir la columna 'date' al formato datetime
    df['date'] = pd.to_datetime(df['date'])

    # Agregar columnas para el día de la semana y la hora
    df['weekday'] = df['date'].dt.strftime('%A')
    df['hour'] = df['date'].dt.strftime('%H')

    # Definir el orden de los días de la semana
    ordered_days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]

    # Convertir la columna 'weekday' a tipo 'category' con el orden establecido
    df['weekday'] = pd.Categorical(df['weekday'], categories=ordered_days, ordered=True)

    # Obtener el número de semanas que el usuario quiere considerar
    n_semanas = dataconfig["ia"]["trainingWeeks"]

    # Filtrar las últimas n semanas del DataFrame
    last_n_weeks = df['date'].max() - pd.DateOffset(weeks=n_semanas)
    df_filtered = df[df['date'] >= last_n_weeks]

    # Agrupar por día de la semana, hora y tanque, y calcular el promedio
    grouped = df_filtered.groupby(['weekday', 'hour', 'waterTank'])['level'].mean().reset_index()

    # Ordenar el DataFrame por día de la semana y reiniciar el índice
    grouped = grouped.sort_values(by=['weekday', 'hour', 'waterTank']).reset_index(drop=True)

    # Guardar el DataFrame resultante en un archivo JSON como una lista de diccionarios
    grouped_records = grouped.to_dict(orient='records')

    # Obtener la ruta del directorio actual donde se encuentra consumopromedio.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_directory, 'Json', 'ConsumoPromedio.json')

    print("\033[92m**Consumo promedio generado**\033[0m")

    with open(config_path, 'w') as file:
        file.write(json.dumps(grouped_records, indent=4))
    file.close()
    return json.dumps(grouped_records, indent=4)
