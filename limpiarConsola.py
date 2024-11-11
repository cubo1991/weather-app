from rich.console import Console
import os
import time

# Crea una instancia de Console de rich
console = Console()

def limpiar_consola():
    # Usa el comando del sistema para limpiar la consola completa
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux y macOS
        os.system('clear')
    
    # Limpia el buffer de rich
    console.clear()


