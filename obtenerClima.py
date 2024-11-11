from cambiarTemperatura import cambiarTemperatura 
from llamadaApi import llamadaApi  # Importar la función desde llamadaApi.py
from historialConsultas import agregarAlHistorial
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
# from rich.progress import Progress
# from rich.prompt import Prompt
from rich.box import SIMPLE

#creamos una instancia de Console
Console = Console()


def obtener_clima(ciudad, unidad):
    simbolo, unidad = cambiarTemperatura(unidad)
    datos = llamadaApi(ciudad, unidad)  # Llamar a la función para obtener los datos

    if datos is not None:  # Si hay datos, se extrae el clima
        clima = datos['main']
        Console.print("\n")
        # Crear una tabla para mostrar el clima
        tabla_clima = Table(title="", style= "bold blue", box=SIMPLE)
        # Agregar columnas a la tabla
        tabla_clima.add_column("Descripción", style="bold", justify="center", width=15)
        tabla_clima.add_column("Valor", justify="center", width=10)

        # Agregar filas con los datos del clima
        tabla_clima.add_row("Temperatura 🌡️", f"{clima['temp']}°{simbolo}")
        tabla_clima.add_row("Máxima 🌞", f"{clima['temp_max']}°{simbolo}")
        tabla_clima.add_row("Mínima ☁️", f"{clima['temp_min']}°{simbolo}")
        tabla_clima.add_row("Humedad 💧", f"{clima['humidity']}%")

        panel = Panel(
            tabla_clima,
            title=f"☁️🌞 [bold blue]Clima de {ciudad} [/bold blue]🌞☁️",
            subtitle="[bold blue]Consulta meteorológica[/bold blue]",
            width=50,  # Establece un ancho fijo para el panel (opcional)
            expand=False  # Esto asegura que el panel se ajuste al contenido
        )

        # Mostrar la tabla en la consola
        Console.print(panel)

        # También guarda la información en `resultado` en formato de texto
        resultado = (
            f"Ciudad: {ciudad}\n"
            f"Temperatura: {clima['temp']}°{simbolo}\n"
            f"Máxima: {clima['temp_max']}°{simbolo}\n"
            f"Mínima: {clima['temp_min']}°{simbolo}\n"
            f"Humedad: {clima['humidity']}%"
        )

        # Guardar el resultado en el historial
        agregarAlHistorial(resultado)
        agregarAlHistorial("-----------------")
    # else:
    #     Console.print("\n")
    #     resultado = f"No se pudo obtener el clima para '{ciudad}' debido a un error."
    #     Console.print(f"[bold_red]Error: [/bold_red]{resultado}")

        return resultado  # Devolver el resultado formateado para la interfaz
