from obtenerClima import obtener_clima
from cambiarTemperatura import cambiarTemperatura
from pronosticoExtendido import pronostico_extendido  # Asegúrate de tener esta función implementada
from historialConsultas import mostrarHistorial
from historialConsultas import eliminar_consulta
from historialConsultas import historial

def mostrar_menu():
    print("----- Menú -----")
    print("1. Obtener clima")
    print("2. Pronóstico extendido")
    print("3. Ver historial de consultas")
    print("4. Eliminar una consulta")
    print("5. Salir")
    print("----------------")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            ciudad = input("Ingrese el nombre de la ciudad: ")
            unidad = input("Ingrese la unidad de temperatura deseada: ")
            cambiarTemperatura(unidad)
            obtener_clima(ciudad, unidad)

        elif opcion == '2':
            ciudad = input("Ingrese el nombre de la ciudad: ")
            unidad = input("Ingrese la unidad de temperatura deseada: ")
            pronostico_extendido(ciudad, unidad)

        elif opcion == '3':
            print("-----------Historial------------")
            mostrarHistorial()
            print("--------------------------------")
        
        elif opcion == '4':
            print("----------Eliminar Consulta----------")
            print("Ingrese el orden del elemento que desea eliminar")
            print("Para ver el orden, primero ingrese al historial")
            orden = int(input("Orden: "))
            eliminar_consulta(historial, orden)
            print("Elemento ", orden, " eliminado del historial")
            
        
        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == '__main__':

    main()

