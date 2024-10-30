
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

