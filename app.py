from obtenerClima import obtener_clima
from cambiarTemperatura import cambiarTemperatura
from pronosticoExtendido import pronostico_extendido  # Asegúrate de tener esta función implementada
from historialConsultas import mostrarHistorial
from historialConsultas import eliminar_consulta
from historialConsultas import borrarHistorial


#importaciones para la visualizacion de la consola
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from rich.prompt import Prompt
from rich.box import SIMPLE
import time
import os
from limpiarConsola import limpiar_consola
from pronosticoExtendido import salida_con_barra
from rich.style import Style
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


# Función para mostrar menu de opciones
def mostrar_menu():

    # os.system("cls" if os.name == "nt" else "clear")

    # Crear un panel del menú
    menu_content = Table(title="", box=SIMPLE, style="blue")
    menu_content.add_column("Opción", style="bold blue", justify="center")
    menu_content.add_column("Descripción", style="bold cyan", width=30, justify="center" )
    menu_content.add_row("1", "Obtener clima", style="#003366" )
    menu_content.add_row("2", "Pronóstico extendido", style="#5f8787")
    menu_content.add_row("3", "Ver historial", style="#af8700")
    menu_content.add_row("4", "Eliminar historial", style="#98FF98")
    menu_content.add_row("5", "Borrar historial", style="#FFA07A")
    menu_content.add_row("6", "Salir", style="#FFDB58" )

    # Crear y mostrar el panel con el menú y el fondo simulado
    panel = Panel(
        menu_content,
        title="☁️🌞 [bold green] Bienvenido a la Aplicación del Clima [/bold green] 🌞☁️",
        
    )

    console.print(panel , justify="center")
    


funciona = True  # Variable global para controlar el bucle

# Función main
def main():
    borrarHistorial("s")

#instanciamos console, con esto aplicamos rich
console = Console()

# Funciones  para cada opcion
def opcion_1():
    

        ciudad = Prompt.ask("[#003366]Ingrese el nombre de la ciudad [/#003366]")
        unidad = Prompt.ask("[#003366]Ingrese la unidad de temperatura deseada: ([bold green]'C'[/bold green] / [bold magenta]'F'[/bold magenta]) [/#003366]")
        cambiarTemperatura(unidad)
        
        # Agregar el spinner para indicar la carga de datos
        with console.status("[bold blue]Obteniendo el clima...[/bold blue]", spinner="weather", ):
            time.sleep(3)
            # Llamada a la función para obtener el clima
            
            obtener_clima(ciudad, unidad)
        Prompt.ask("[bold green]presione (--enter--) para continuar[/bold green]")
        limpiar_consola()

def opcion_2():
    ciudad = Prompt.ask("[#5f8787]Ingrese el nombre de la ciudad [/#5f8787]")
    unidad = Prompt.ask("[#5f8787]Ingrese la unidad de temperatura deseada ([bold green]'C'[/bold green] /[bold magenta]'F'[/bold magenta]) [/#5f8787]")
    pronostico_extendido(ciudad, unidad)
    # Prompt.ask("presione enter para continuar")
    # limpiar_consola()

def opcion_3():
    console.print("[#af8700]--------Historial--------[/#af8700]")
    mostrarHistorial()
    console.print("[#af8700]-------------------------[/#af8700]")
    Prompt.ask("[bold green]presione enter para continuar[/bold green]")
    limpiar_consola()

def opcion_4():
    indice = console.input("[#98FF98]Ingrese el número de la consulta a eliminar:[/#98FF98] ")
    indice = int(indice)  # Convierte la entrada a un número
    eliminar_consulta(indice)
    Prompt.ask("[bold green]presione enter para continuar[/bold green]")
    limpiar_consola()

def opcion_5():
    eliminar = console.input("[#FFA07A]Seguro/a que desea eliminar todo el historial? (S/N):[/#FFA07A] ")
    borrarHistorial(eliminar)
    Prompt.ask("[bold green]presione enter para continuar[/bold green]")
    limpiar_consola()

def opcion_6():
    global funciona  # Indica que `funciona` es una variable global
    salida_con_barra()
    funciona = False  # Cambia `funciona` a False para salir del bucle
    

def opcion_invalida():
    # console.print("[red] ⚠️ Opción no válida. Por favor, intente de nuevo.⚠️ [/red]")
    mensajeError1 = f"[red]⚠️ Opción no válida. Por favor, intente de nuevo.[/red]⚠️"
    PanelError1 = Panel(mensajeError1, title="ERROR", style="red", border_style="bold red")
    console.print(PanelError1)
    Prompt.ask("[bold green]presione enter para continuar[/bold green]")
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
    opcion = Prompt.ask("[bold green]Seleccione una opción para continuar[/bold green]")
    opciones.get(opcion, opcion_invalida)()  # Ejecuta la función correspondiente o `opcion_invalida`


if __name__ == '__main__':

 main()

