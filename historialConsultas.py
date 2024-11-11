from rich.console import Console
historial = []
console = Console()

def agregarAlHistorial(resultado):
    with open('historial.txt', 'a') as file:
        file.write(resultado + '\n')

def mostrarHistorial():
    try:
        with open('historial.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        console.print("[dark_orange3]No hay consultas en el historial.[/dark_orange3]")
    
def eliminar_consulta(indice):
    try:
        with open('historial.txt', 'r') as file:
            lines = file.readlines()
        if 1 <= indice <= len(lines) // 5:
            del lines[(indice - 1) * 5: indice * 5]
            with open('historial.txt', 'w') as file:
                file.writelines(lines)
        else:
            console.print("[bold_red]Índice fuera de rango.[/bold_red]")
    except FileNotFoundError:
        console.print("[dark_orange3]No hay consultas en el historial.[/dark_orange3]")
        
        
def borrarHistorial(eliminar):
    if eliminar == "s":
        with open('historial.txt', 'w') as file:
            pass