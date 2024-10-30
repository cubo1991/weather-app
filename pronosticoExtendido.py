import requests
import os
from dotenv import load_dotenv
import time
import datetime 
from cambiarTemperatura import cambiarTemperatura 

load_dotenv()
api_key = os.getenv('API_KEY')

def pronostico_extendido(ciudad, unidad):
    weather_data= []
    simbolo, unidad = cambiarTemperatura(unidad)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units={unidad}'

    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
        
            datos = respuesta.json()  # Obtener los datos JSON
            coordenadas = datos["coord"]
            
        elif respuesta.status_code == 404:
            print(f"Error: La ciudad '{ciudad}' no fue encontrada.")  # Ciudad no válida
        else:
            print(f"Error: No se pudo obtener el clima para '{ciudad}'. Código {respuesta.status_code}.")
    
    except requests.exceptions.RequestException as e:
        print("Error: Ocurrió un problema al intentar conectarse a la API.")
        print(f"Detalles técnicos: {e}")

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
        else:
            print(f"Error: No se pudo obtener el clima para '{ciudad}'. Código {respuesta.status_code}.")
    
    except requests.exceptions.RequestException as e:
        print("Error: Ocurrió un problema al intentar conectarse a la API.")
        print(f"Detalles técnicos: {e}")


    # Obtén el nombre de la ciudad
    ciudad = ciudad  # Cambia esto si tienes el nombre en el JSON

    # Imprimir el nombre de la ciudad
    print(f"Pronóstico extendido para: {ciudad}\n")

    dias = []

    contador = 0

    for day in weather_data['list']:

        if contador<7:

            fecha = (datetime.datetime.today() + datetime.timedelta(days=contador)).strftime("%d-%m-%Y")
            temperatura = day['main']['temp']
            temp_min = day['main']['temp_min']
            temp_max = day['main']['temp_max']
            descripcion = day['weather'][0]['description']
            humedad = day['main']['humidity']
            velocidad_viento = day['wind']['speed']

            print(f"Fecha: {fecha}")
            print(f"  Temperatura: {temperatura}°{simbolo}")
            print(f"  Temperatura mínima: {temp_min}°{simbolo}")
            print(f"  Temperatura máxima: {temp_max}°{simbolo}")
            print(f"  Descripción del clima: {descripcion}")
            print(f"  Humedad: {humedad}%")
            print(f"  Velocidad del viento: {velocidad_viento} m/s")
            print("-" * 40)
            contador += 1
        else:
            break
import json
import time
from cambiarTemperatura import cambiarTemperatura

def pronostico_extendido(ciudad, unidad):
    simbolo, unidad = cambiarTemperatura(unidad)
    
    # Cargar el archivo JSON de pronóstico simulado
    with open('simulated_weather_forecast.json', 'r') as json_file:
        weather_data = json.load(json_file)
    
    print(f"Pronóstico extendido para: {ciudad}\n")
    
    # Índice para navegar entre los días del pronóstico
    indice_dia = 0
    num_dias = len(weather_data['daily'])

    while True:
        # Asegurarse de que el índice esté dentro del rango válido
        if indice_dia < 0:
            indice_dia = 0
        elif indice_dia >= num_dias:
            indice_dia = num_dias - 1

        # Extraer el pronóstico del día actual
        day = weather_data['daily'][indice_dia]
        fecha = time.strftime('%Y-%m-%d', time.localtime(day['dt']))
        
        # Muestra la información del pronóstico
        print(f"Fecha: {fecha}")
        print(f"  Temperatura día: {day['temp']['day']}°{simbolo}")
        print(f"  Temperatura mínima: {day['temp']['min']}°{simbolo}")
        print(f"  Temperatura máxima: {day['temp']['max']}°{simbolo}")
        print(f"  Descripción del clima: {day['weather'][0]['description']}")
        print(f"  Humedad: {day['humidity']}%")
        print(f"  Velocidad del viento: {day['wind_speed']} m/s")
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
