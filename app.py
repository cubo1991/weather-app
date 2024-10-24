from llamadaApi import llamadaApi  # Importar la función desde llamadaApi.py

def obtener_clima(ciudad):
    while True:
        datos = llamadaApi(ciudad)  # Llamar a la función para obtener los datos
        
        if datos is not None:  # Si hay datos, se extrae el clima
            clima = datos['main']
            print(f"Ciudad: {ciudad}")
            print(f"Temperatura: {clima['temp']}°C")
            print(f"Maxima: {clima['temp_max']}°C")
            print(f"Minima: {clima['temp_min']}°C")
            print(f"Humedad: {clima['humidity']}%")
        else:
            print(f"No se pudo obtener el clima para '{ciudad}' debido a un error.")
        continuar = input(f'¿Desea continuar con otra ciudad? NO para salir.\n')
       
        if continuar.upper() == "NO":
            break 
        else: 
            ciudad = input("Ingrese el nombre de la ciudad: ")
          
         

            
if __name__ == '__main__':
    ciudad = input("Ingrese el nombre de la ciudad: ")
    obtener_clima(ciudad)
