import requests
import os
from dotenv import load_dotenv
import datetime 
from cambiarTemperatura import cambiarTemperatura 
####
from rich.console import Console
from rich.table import Table
from rich.box import SIMPLE
from rich.progress import Progress,BarColumn, TextColumn
from rich.prompt import Prompt
import time

console = Console()
# Función para mostrar la barra de carga al salir del programa
def salida_con_barra():
    console.print("[magenta]Saliendo del pronostico extendido...[/magenta]")
    with Progress(
        TextColumn("[bold blue]{task.description}[/bold blue]"),
        BarColumn(bar_width=None),
        transient=True,
    ) as progress:
        tarea = progress.add_task("Cerrando", total=100)
        for _ in range(100):
            progress.update(tarea, advance=1)
            time.sleep(0.02)  # Ajusta este valor para controlar la velocidad de la barra de carga

load_dotenv()
api_key = os.getenv('API_KEY')


def pronostico_extendido(ciudad, unidad):
    simbolo, unidad = cambiarTemperatura(unidad)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units={unidad}'

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            coordenadas = datos["coord"]
        elif respuesta.status_code == 404:
            console.print(f"[bold_red]Error:[/bold_red] La ciudad '{ciudad}' no fue encontrada.")
            return []
        else:
            console.print(f"[bold_red]Error:[/bold_red] No se pudo obtener el clima para '{ciudad}'. Código {respuesta.status_code}.")
            return []
    except requests.exceptions.RequestException as e:
        console.print("[bold_red]Error:[/vold_red] Ocurrió un problema al intentar conectarse a la API.")
        console.print(f"[bold_red]Detalles técnicos:[/bold_red] {e}")
        return []

    latitud = coordenadas['lat']
    longitud = coordenadas['lon']
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={latitud}&lon={longitud}&appid={api_key}&units={unidad}"

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            weather_data = respuesta.json()
        else:
            console.print(f"[bold_red]Error:[/bold_red] No se pudo obtener el clima extendido para '{ciudad}'. Código {respuesta.status_code}.")
            return []
    except requests.exceptions.RequestException as e:
        console.print("[bold_red]Error:[/bold_red] Ocurrió un problema al intentar conectarse a la API.")
        console.print(f"[bold_red]Detalles técnicos:[/bold_red] {e}")
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

    # Mostrar los días uno a uno en formato de tabla
    indice_dia = 0
    while True:
        if indice_dia < 0:
            indice_dia = 0
        elif indice_dia >= len(dias):
            indice_dia = len(dias) - 1

        dia_actual = dias[indice_dia]

        # Crear la tabla para mostrar el pronóstico de un solo día
        tabla = Table(show_header=True, title=f"pronostico de {ciudad}",title_style="bold", header_style="bold cyan", box=SIMPLE)
        tabla.add_column("Fecha", style="bold")
        tabla.add_column("Temperatura", justify="center", style="bold green")
        tabla.add_column("Mínima", justify="center", style="bold yellow")
        tabla.add_column("Máxima", justify="center", style="bold red")
        tabla.add_column("Detalle", justify="center", style="bold magenta")
        tabla.add_column("Humedad", justify="center", style="bold blue")
        tabla.add_column("Viento (m/s)", justify="center", style="bold white")

        # Añadir la fila con la información del día actual
        tabla.add_row(
            dia_actual['fecha'],
            f"{dia_actual['temperatura']}°{simbolo}",
            f"{dia_actual['temp_min']}°{simbolo}",
            f"{dia_actual['temp_max']}°{simbolo}",
            dia_actual['descripcion'],
            f"{dia_actual['humedad']}%",
            f"{dia_actual['velocidad_viento']} m/s"
        )

        # Mostrar la tabla en consola
        console.print(tabla)

        # Menú de navegación
        console.print("\n[purple4] Opciones de navegación:[/purple4]")
        if indice_dia > 0:
            console.print("[bold_blue]1. [/bold_blue] [blue_violet] Día anterior[/blue_violet]")
        if indice_dia < len(dias) - 1:
            console.print("[bold_blue]2. [/bold_blue] [blue_violet] Día siguiente[/blue_violet]")
        console.print("[bold_blue]3. [/bold_blue] [blue_violet] Salir del pronóstico extendido[/blue_violet]")

        opcion = Prompt.ask("[magenta]Seleccione una opción (1-3):[/magenta] ")

        if opcion == '1' and indice_dia > 0:
            indice_dia -= 1  # Moverse al día anterior
        elif opcion == '2' and indice_dia < len(dias) - 1:
            indice_dia += 1  # Moverse al día siguiente
        elif opcion == '3':

            salida_con_barra()
            # print("Saliendo del pronóstico extendido...")
            break
        else:
            console.print("[red]⚠️ Opción no válida. Por favor, intente de nuevo.⚠️ [/red]")
