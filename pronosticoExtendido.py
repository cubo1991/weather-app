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
