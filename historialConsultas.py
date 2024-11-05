historial = []

def agregarAlHistorial (consulta):
    if consulta is not None:
        historial.append(consulta)
        print("Consulta agregada al historial")
    else:
        print("Error, la consulta no fue recibida por esta funcion")

def mostrarHistorial():

    if not historial:
        print("No se han realizado consultas")
        print("Para hacerlo, ingresa la opcion 1 del menú")
    else:

        for i, consulta in enumerate(historial):
            print("-------------",i+1,"-------------")
            print(consulta)
    
def eliminar_consulta(historial, indice):
    if 0 <= indice < len(historial): 
        elemento = historial.pop(indice+1)
        print(f"Elemento '{elemento}' eliminado en el índice {indice+1}.")
    else:
        print("Índice fuera de rango.")