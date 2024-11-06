import requests
import os
from dotenv import load_dotenv
import datetime 
from cambiarTemperatura import cambiarTemperatura 
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich.box import SIMPLE

load_dotenv()
api_key = os.getenv('API_KEY')
Console = Console()

def pronostico_extendido(ciudad, unidad):
    simbolo, unidad = cambiarTemperatura(unidad)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units={unidad}'

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            coordenadas = datos["coord"]
        elif respuesta.status_code == 404:
            Console.print(f"[bold_red]Error:[/bold_red] La ciudad '{ciudad}' no fue encontrada.")
            return []
        else:
            Console.print(f"[bold_red]Error:[/bold_red] No se pudo obtener el clima para '{ciudad}'. Código {respuesta.status_code}.")
            return []
    except requests.exceptions.RequestException as e:
        Console.print("[bold_red]Error:[/vold_red] Ocurrió un problema al intentar conectarse a la API.")
        Console.print(f"[bold_red]Detalles técnicos:[/bold_red] {e}")
        return []

    latitud = coordenadas['lat']
    longitud = coordenadas['lon']
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={latitud}&lon={longitud}&appid={api_key}&units={unidad}"

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            weather_data = respuesta.json()
        else:
            Console.print(f"[bold_red]Error:[/bold_red] No se pudo obtener el clima extendido para '{ciudad}'. Código {respuesta.status_code}.")
            return []
    except requests.exceptions.RequestException as e:
        Console.print("[bold_red]Error:[/bold_red] Ocurrió un problema al intentar conectarse a la API.")
        Console.print(f"[bold_red]Detalles técnicos:[/bold_red] {e}")
        return []

    # Crear lista de pronósticos para los próximos 7 días
    dias = []
    for i in range(7):
        dia = weather_data['list'][i]  # Asegúrate de que hay al menos 7 días en la lista.
        dias.append({
            'fecha': (datetime.datetime.today() + datetime.timedelta(days=i)).strftime("%d-%m-%Y"),
            'temperatura': dia['main']['temp'],
            'temp_min': dia['main']['temp_min'],
            'temp_max': dia['main']['temp_max'],
            'descripcion': dia['weather'][0]['description'],
            'humedad': dia['main']['humidity'],
            'velocidad_viento': dia['wind']['speed']
        })

    print(f"Pronóstico extendido para {ciudad}: {dias}")  # Muestra la lista de días en consola.
    
    return dias  # Retorna solo la lista de días.
