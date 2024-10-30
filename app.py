from llamadaApi import llamadaApi  # Importar la función desde llamadaApi.py

from pronosticoExtendido import pronostico_extendido

from cambiarTemperatura import cambiarTemperatura 
def obtener_clima(ciudad, unidad):
    simbolo, unidad = cambiarTemperatura(unidad)


    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

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
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == '__main__':
    ciudad = input("Ingrese el nombre de la ciudad: ")
    unidad = input("Ingrese unidad de temperatura: ")
    #obtener_clima(ciudad)
    pronostico_extendido(ciudad, unidad)
    

