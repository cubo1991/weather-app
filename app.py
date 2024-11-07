from obtenerClima import obtener_clima
from cambiarTemperatura import cambiarTemperatura
from pronosticoExtendido import pronostico_extendido  # Asegúrate de tener esta función implementada
from historialConsultas import mostrarHistorial
from historialConsultas import eliminar_consulta
from historialConsultas import borrarHistorial

#importaciones para la visualizacion de la consola
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from rich.prompt import Prompt
from rich.box import SIMPLE
import time
from limpiarConsola import limpiar_consola
from pronosticoExtendido import salida_con_barra

#creamos una instancia de console para imprimir en la consola con rich
console = Console()


# Función para mostrar la barra de carga al salir del programa
def salida_con_barra():
    console.print("[bold red]Saliendo del programa...[/bold red]")
    with Progress(
        TextColumn("[bold blue]{task.description}[/bold blue]"),
        BarColumn(bar_width=None),
        transient=True,
    ) as progress:
        tarea = progress.add_task("Cerrando", total=100)
        for _ in range(100):
            progress.update(tarea, advance=1)
            time.sleep(0.02)  # Ajusta este valor para controlar la velocidad de la barra de carga



def mostrar_menu():
    console.print("🌞☁️ [bold green] Bienvenido a la Aplicación del Clima [/bold green]🌞☁️", justify="left")
    table = Table(title= "", box= SIMPLE, style= "blue")
    table.add_column("Opción", style="bold blue" )
    table.add_column("Descripción", style="bold cyan",width=30 )
    table.add_row("1", "Obtener clima")
    table.add_row("2", "Pronóstico extendido")
    table.add_row("3", "Ver historial")
    table.add_row("4", "Eliminar historial")
    table.add_row("5","Borrar historial")
    table.add_row("6","Salir")
    console.print(table)


funciona = True  # Variable global para controlar el bucle

def main():
    borrarHistorial("s")
  
console = Console()

def opcion_1():
    ciudad = Prompt.ask("[dark_sea_green]Ingrese el nombre de la ciudad [/dark_sea_green]")
    unidad = Prompt.ask("[dark_sea_green]Ingrese la unidad de temperatura deseada: ('C' / 'F') [/dark_sea_green]")
    cambiarTemperatura(unidad)
    obtener_clima(ciudad, unidad)
    Prompt.ask("presione enter para continuar")
    limpiar_consola()

def opcion_2():
    ciudad = Prompt.ask("[deep_sky_blue3]Ingrese el nombre de la ciudad [/deep_sky_blue3]")
    unidad = Prompt.ask("[deep_sky_blue3]Ingrese la unidad de temperatura deseada ('C' / 'F') [/deep_sky_blue3]")
    pronostico_extendido(ciudad, unidad)
    # Prompt.ask("presione enter para continuar")
    # limpiar_consola()

def opcion_3():
    console.print("[dark_orange3]--------Historial--------[/dark_orange3]")
    mostrarHistorial()
    console.print("[dark_orange3]-------------------------[/dark_orange3]")
    Prompt.ask("presione enter para continuar")
    limpiar_consola()

def opcion_4():
    indice = console.input("[yellow]Ingrese el número de la consulta a eliminar:[/yellow] ")
    indice = int(indice)  # Convierte la entrada a un número
    eliminar_consulta(indice)
    Prompt.ask("presione enter para continuar")
    limpiar_consola()

def opcion_5():
    eliminar = console.input("[yellow]Seguro/a que desea eliminar todo el historial? (S/N):[/yellow] ")
    borrarHistorial(eliminar)
    Prompt.ask("presione enter para continuar")
    limpiar_consola()

def opcion_6():
    global funciona  # Indica que `funciona` es una variable global
    salida_con_barra()
    funciona = False  # Cambia `funciona` a False para salir del bucle
    

def opcion_invalida():
    # console.print("[red] ⚠️ Opción no válida. Por favor, intente de nuevo.⚠️ [/red]")
    resultado = f"[red]⚠️ Opción no válida. Por favor, intente de nuevo.[/red]⚠️"
    console.print(f"[bold_red]Error: [/bold_red]{resultado}")
    Prompt.ask("presione enter para continuar")
    limpiar_consola()
    

# Diccionario de opciones
opciones = {
    '1': opcion_1,
    '2': opcion_2,
    '3': opcion_3,
    '4': opcion_4,
    '5': opcion_5,
    '6': opcion_6,
}

# Bucle principal
while funciona:
    mostrar_menu()
    opcion = Prompt.ask("[bold blue]Ingrese una opción[/bold blue]")
    opciones.get(opcion, opcion_invalida)()  # Ejecuta la función correspondiente o `opcion_invalida`


if __name__ == '__main__':

 main()

