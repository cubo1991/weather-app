import json
import time
from cambiarTemperatura import cambiarTemperatura 

def pronostico_extendido(ciudad, unidad ):
    simbolo, unidad = cambiarTemperatura(unidad)
    # Abre el archivo JSON que está al mismo nivel que esta función
    with open('simulated_weather_forecast.json', 'r') as json_file:
        weather_data = json.load(json_file)
    
    # Obtén el nombre de la ciudad
    ciudad = ciudad  # Cambia esto si tienes el nombre en el JSON

    # Imprimir el nombre de la ciudad
    print(f"Pronóstico extendido para: {ciudad}\n")
    
    # Itera a través de los datos del pronóstico
    for day in weather_data['daily']:
        # Convierte el tiempo de Unix a un formato legible (año-mes-día)
        fecha = time.strftime('%Y-%m-%d', time.localtime(day['dt']))
        
        # Muestra la información del pronóstico
        print(f"Fecha: {fecha}")
        print(f"  Temperatura día: {day['temp']['day']}°{simbolo}")
        print(f"  Temperatura mínima: {day['temp']['min']}°{simbolo}")
        print(f"  Temperatura máxima: {day['temp']['max']}°{simbolo}")
        print(f"  Descripción del clima: {day['weather'][0]['description']}")
        print(f"  Humedad: {day['humidity']}%")
        print(f"  Velocidad del viento: {day['wind_speed']} m/s")
        print("-" * 40)  # Separador para cada día

