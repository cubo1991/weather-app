import requests
import os
from dotenv import load_dotenv
import datetime 
from cambiarTemperatura import cambiarTemperatura 

load_dotenv()
api_key = os.getenv('API_KEY')

def pronostico_extendido(ciudad, unidad):
    weather_data = []
    simbolo, unidad = cambiarTemperatura(unidad)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units={unidad}'

    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()  # Obtener los datos JSON
            coordenadas = datos["coord"]
        elif respuesta.status_code == 404:
            print(f"Error: La ciudad '{ciudad}' no fue encontrada.")  # Ciudad no válida
            return
        else:
            print(f"Error: No se pudo obtener el clima para '{ciudad}'. Código {respuesta.status_code}.")
            return
    
    except requests.exceptions.RequestException as e:
        print("Error: Ocurrió un problema al intentar conectarse a la API.")
        print(f"Detalles técnicos: {e}")
        return

    latitud = coordenadas['lat']
    longitud = coordenadas['lon']

    # Segunda solicitud para el pronóstico extendido
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={latitud}&lon={longitud}&appid={api_key}&units={unidad}"
    
    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            weather_data = respuesta.json()  # Obtener los datos JSON
        elif respuesta.status_code == 404:
            print(f"Error: La ciudad '{ciudad}' no fue encontrada.")  # Ciudad no válida
            return
        else:
            print(f"Error: No se pudo obtener el clima para '{ciudad}'. Código {respuesta.status_code}.")
            return
    
    except requests.exceptions.RequestException as e:
        print("Error: Ocurrió un problema al intentar conectarse a la API.")
        print(f"Detalles técnicos: {e}")
        return

    # Imprimir el nombre de la ciudad
    print(f"Pronóstico extendido para: {ciudad}\n")

    dias = []
    contador = 0

    # Recopila los datos de los próximos 7 días
    for day in weather_data['list']:
        if contador < 7:
            dias.append({
                'fecha': (datetime.datetime.today() + datetime.timedelta(days=contador)).strftime("%d-%m-%Y"),
                'temperatura': day['main']['temp'],
                'temp_min': day['main']['temp_min'],
                'temp_max': day['main']['temp_max'],
                'descripcion': day['weather'][0]['description'],
                'humedad': day['main']['humidity'],
                'velocidad_viento': day['wind']['speed']
            })
            contador += 1

    # Índice para navegar entre los días
    indice_dia = 0

    while True:
        # Asegurar que el índice esté en el rango válido
        if indice_dia < 0:
            indice_dia = 0
        elif indice_dia >= len(dias):
            indice_dia = len(dias) - 1

        dia_actual = dias[indice_dia]
        print(f"Fecha: {dia_actual['fecha']}")
        print(f"  Temperatura: {dia_actual['temperatura']}°{simbolo}")
        print(f"  Temperatura mínima: {dia_actual['temp_min']}°{simbolo}")
        print(f"  Temperatura máxima: {dia_actual['temp_max']}°{simbolo}")
        print(f"  Descripción del clima: {dia_actual['descripcion']}")
        print(f"  Humedad: {dia_actual['humedad']}%")
        print(f"  Velocidad del viento: {dia_actual['velocidad_viento']} m/s")
        print("-" * 40)

        # Menú de navegación
        print("\nOpciones de navegación:")
        print("1. Día anterior")
        print("2. Día siguiente")
        print("3. Salir del pronóstico extendido")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            indice_dia -= 1  # Moverse al día anterior
        elif opcion == '2':
            indice_dia += 1  # Moverse al día siguiente
        elif opcion == '3':
            print("Saliendo del pronóstico extendido...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
