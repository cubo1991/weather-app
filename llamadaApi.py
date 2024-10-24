import requests
import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()
api_key = os.getenv('API_KEY')

def llamadaApi(ciudad, unidad):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units={unidad}'
    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            return respuesta.json()  # Retornar los datos completos si la solicitud es exitosa
        elif respuesta.status_code == 404:
            print(f"Error: La ciudad '{ciudad}' no fue encontrada.")  # Ciudad no válida
        else:
            print(f"Error: No se pudo obtener el clima para '{ciudad}'. Código {respuesta.status_code}.")
    
    except requests.exceptions.RequestException as e:
        print("Error: Ocurrió un problema al intentar conectarse a la API.")
        print(f"Detalles técnicos: {e}")
    
    return None  # Retornar None si hay algún error
