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

#creamos una instancia de console para imprimir en la consola con rich
Console = Console()

# Función para mostrar la barra de carga al salir del programa
def salida_con_barra():
    Console.print("[bold red]Saliendo del programa...[/bold red]")
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
    Console.print("🌞☁️ [bold green] Bienvenido a la Aplicación del Clima [/bold green]🌞☁️", justify="left")
    table = Table(title= "", box= SIMPLE, style= "blue")
    table.add_column("Opción", style="bold blue" )
    table.add_column("Descripción", style="bold cyan",width=30 )
    table.add_row("1", "Obtener clima")
    table.add_row("2", "Pronóstico extendido")
    table.add_row("3", "Ver historial")
    table.add_row("4", "Eliminar historial")
    table.add_row("5","Borrar historial")
    table.add_row("6","Salir")
    Console.print(table)



def main():
    borrarHistorial("s")
    while True:
        mostrar_menu()
        opcion = Prompt.ask("[yellow4]Selecciona una opción (1-6)[/yellow4]")
        # opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            # ciudad = input("Ingrese el nombre de la ciudad: ")
            ciudad = Prompt.ask("[dark_sea_green]Ingrese el nombre de la ciudad [/dark_sea_green]")
            # unidad = input("Ingrese la unidad de temperatura deseada: ")
            unidad = Prompt.ask("[dark_sea_green]Ingrese la unidad de temperatura deseada: ('C' / 'F') [/dark_sea_green]")
            cambiarTemperatura(unidad)
            obtener_clima(ciudad, unidad)

        elif opcion == '2':
            # ciudad = input("Ingrese el nombre de la ciudad: ")
            ciudad = Prompt.ask("[deep_sky_blue3] Ingrese el nombre de la ciudad [/deep_sky_blue3]")

            # unidad = input("Ingrese la unidad de temperatura deseada: ")
            unidad = Prompt.ask("[deep_sky_blue3] Ingrese la unidad de temperatura deseada ('C' / 'F') [/deep_sky_blue3]")
            pronostico_extendido(ciudad, unidad)

        elif opcion == '3':
            Console.print("[dark_orange3]--------Historial--------[/dark_orange3]")
            mostrarHistorial()
            Console.print("[dark_orange3]-------------------------[/dark_orange3]")

        elif opcion == '4':
            # indice = int(input("Ingrese el número de la consulta a eliminar: "))
            
            indice = Console.input("[yellow]Ingrese el número de la consulta a eliminar:[/yellow] ")
            indice = int(indice)  # Convierte la entrada a un número
            eliminar_consulta(indice)
            
        elif opcion == '5':
            # eliminar = input("Seguro/a que desea eliminar todo el historial? (S/N): ")
            eliminar = Console.input("[yellow]Seguro/a que desea eliminar todo el historial? (S/N):[yellow] ")
            
            borrarHistorial(eliminar)
        
        elif opcion == '6':
                    # print("Saliendo del programa...")
                    salida_con_barra()
                    break
                
        else:
            Console.print("[red] ⚠️ Opción no válida. Por favor, intente de nuevo.⚠️ [/red]")

if __name__ == '__main__':

    main()

