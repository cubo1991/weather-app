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
            mensaje_error1 = "[red3]La clave API no es válida[/red3]"
            panel_error1 = Panel(mensaje_error1, title="Error", style="red", border_style="bold red")
            Console.print(panel_error1)

        elif respuesta.status_code == 404:
            Console.print("\n")
            mensaje_error2 = f"[red3]⚠️ La ciudad '[green]{ciudad}[/green]' no fue encontrada ⚠️[/red3]"
            panel_error2 = Panel(mensaje_error2, title="ERROR", style="red", border_style="bold red")
            Console.print(panel_error2)

        else:
            Console.print("\n")
            mensaje_error3 = f"[red3]⚠️ No se pudo obtener el clima para'{ciudad}'. Código'{respuesta.status_code}' ⚠️[/red3]"
            panel_error3 = Panel(mensaje_error3, title="ERROR", style="red", border_style="bold red")
            Console.print(panel_error3)
    
    except requests.exceptions.Timeout:
        Console.print("\n")
        mensaje_error4 = f"[red3]⚠️ La solicitud a la API ha excedido el tiempo de espera. ⚠️[/red3] "
        panel_error4 = Panel(mensaje_error4, title="ERROR", style="red", border_style="bold red")
        Console.print(panel_error4)
        
   
    except requests.exceptions.RequestException as e:
        error_message = str(e)
        if "getaddrinfo" in error_message:
            Console.print("\n")
            mensaje_error5 = f"[red3]⚠️ No se pudo resolver el nombre del host de la API. Verifica tu conexión a Internet. ⚠️[/red3] "
            panel_error5 = Panel(mensaje_error5, title="ERROR", style="red", border_style="bold red")
            Console.print(panel_error5)
            

        elif "Connection refused" in error_message:
            Console.print("\n")
            mensaje_error6 = f"[red3]⚠️ La conexión a la API fue rechazada. Verifica que la API esté disponible. ⚠️[/red3]"
            panel_error6 = Panel(mensaje_error6, title="ERROR", style="red", border_style="bold red")
            Console,print(panel_error6)

        else:
            Console.print("\n")
            mensaje_error7 = f"[red3]⚠️ Ocurrió un problema al intentar conectarse a la API ⚠️[/red3]"
            panel_error7 =  Panel(mensaje_error7, title="ERROR", style="red", border_style="bold red")
            Console.print(panel_error7)
            
        # print("Error: Ocurrió un problema al intentar conectarse a la API.")
        # print(f"Detalles técnicos: {e}")
    
    return None  # Retornar None si hay algún error
