import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def obtener_clima(ciudad):
   
    try :
        url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            clima = datos['main']
            print(f"Ciudad: {ciudad}")
            print(f"Temperatura: {clima['temp']}°C")
            print(f"Maxima: {clima['temp_max']}°C")
            print(f"Minima: {clima['temp_min']}°C")
            print(f"Humedad: {clima['humidity']}%")
        elif respuesta.status_code == 404:
                # Si la ciudad no existe
                print(f"Error: La ciudad '{ciudad}' no fue encontrada.")
        else:
            # Otros errores relacionados con la API
            print(f"Error: No se pudo obtener el clima para '{ciudad}'. (Código {respuesta.status_code})")
    except requests.exceptions.RequestException as e:
        # Manejo de cualquier otro error de conexión o solicitud
        print("Error: Ocurrió un problema al intentar conectarse a la API. Inténtalo de nuevo más tarde.")
        print(f"Detalles técnicos: {e}")


if __.name__ == '__main__':
    ciudad = input("Ingrese el nombre de la ciudad: ")
    obtener_clima(ciudad)