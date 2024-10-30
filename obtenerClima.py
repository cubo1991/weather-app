from cambiarTemperatura import cambiarTemperatura 
from llamadaApi import llamadaApi  # Importar la función desde llamadaApi.py

def obtener_clima(ciudad, unidad):
    simbolo, unidad = cambiarTemperatura(unidad)


    while True:
      
        datos = llamadaApi(ciudad, unidad)  # Llamar a la función para obtener los datos
        
        if datos is not None:  # Si hay datos, se extrae el clima
            
            clima = datos['main']
            print(f"Ciudad: {ciudad}")
            print(f"Temperatura: {clima['temp']}°{simbolo}")
            print(f"Maxima: {clima['temp_max']}°{simbolo}")
            print(f"Minima: {clima['temp_min']}°{simbolo}")
            print(f"Humedad: {clima['humidity']}%")
        else:
            print(f"No se pudo obtener el clima para '{ciudad}' debido a un error.")
        continuar = input(f'¿Desea continuar con otra ciudad? NO para salir.\n')
       
        if continuar.upper() == "NO":
            break 
        else: 
            
            ciudad = input("Ingrese el nombre de la ciudad: ")
            unidad = input("Ingrese la unidad de Temperatura deseada: ")
            simbolo, unidad = cambiarTemperatura(unidad)

         