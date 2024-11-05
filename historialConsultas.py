historial = []

def agregarAlHistorial(resultado):
    with open('historial.txt', 'a') as file:
        file.write(resultado + '\n')

def mostrarHistorial():
    try:
        with open('historial.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("No hay consultas en el historial.")
    
def eliminar_consulta(indice):
    try:
        with open('historial.txt', 'r') as file:
            lines = file.readlines()
        if 1 <= indice <= len(lines) // 5:
            del lines[(indice - 1) * 5: indice * 5]
            with open('historial.txt', 'w') as file:
                file.writelines(lines)
        else:
            print("Índice fuera de rango.")
    except FileNotFoundError:
        print("No hay consultas en el historial.")
        
        
def borrarHistorial():
    with open('historial.txt', 'w') as file:
        pass