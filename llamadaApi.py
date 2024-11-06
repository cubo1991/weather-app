import requests
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

Console = Console()

# Cargar variables desde .env
load_dotenv()
api_key = os.getenv('API_KEY')

def llamadaApi(ciudad, unidad):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units={unidad}'
    # print(f'{url}')
    try:
        respuesta = requests.get(url, timeout=5) # Establecer un tiempo de espera de 5 segundos
        
        if respuesta.status_code == 200:
            return respuesta.json()  # Retornar los datos completos si la solicitud es exitosa
        elif respuesta.status_code == 401:
            # print("Error: La clave API no es válida.")  # Clave API no válida
            mensaje_error1 = "[red3]Error!:[/red3] La clave API no es válida"
            panel_error1 = Panel(mensaje_error1, title="Error", style="red", border_style="bold red")
            Console.print(panel_error1)

        elif respuesta.status_code == 404:
            # print(f"Error: La ciudad '{ciudad}' no fue encontrada.")  # Ciudad no válida
            mensaje_error2 = f"[red3]Error!:[/red3] La ciudad '[bold green]{ciudad}[/bold green]' no fue encontrada"
            panel_error2 = Panel(mensaje_error2, title="Error", style="red", border_style="bold red")
            Console.print(panel_error2)

        else:
            # print(f"Error: No se pudo obtener el clima para '{ciudad}'. Código {respuesta.status_code}.")
            Console.print(f"[red3]Error!:[/red3] No se pudo obtener el clima para'{ciudad}'. Código'{respuesta.status_code}'")
    
    except requests.exceptions.Timeout:
        # print("Error: La solicitud a la API ha excedido el tiempo de espera.")
        Console.print("[red3]Error!:[/red3] La solicitud a la API ha excedido el tiempo de espera. ")
   
    except requests.exceptions.RequestException as e:
        error_message = str(e)
        if "getaddrinfo" in error_message:
            # print("Error: No se pudo resolver el nombre del host de la API. Verifica tu conexión a Internet.")
            Console.print("[red3]Error!:[/red3] No se pudo resolver el nombre del host de la API. Verifica tu conexión a Internet. ")

        elif "Connection refused" in error_message:
            # print("Error: La conexión a la API fue rechazada. Verifica que la API esté disponible.")
            Console.print("[red3]Error!:[/red3] La conexión a la API fue rechazada. Verifica que la API esté disponible. ")

        else:
            # print("Error: Ocurrió un problema al intentar conectarse a la API.")
            Console.print("[red3]Error!:[/red3] Ocurrió un problema al intentar conectarse a la API")
            
        # print("Error: Ocurrió un problema al intentar conectarse a la API.")
        # print(f"Detalles técnicos: {e}")
    
    return None  # Retornar None si hay algún error
