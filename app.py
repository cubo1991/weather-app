import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def obtener_clima(ciudad):
    print("Estas buscando datos de la ciudad:", ciudad)

if __name__ == '__main__':
    ciudad = input("Ingrese el nombre de la ciudad: ")
    obtener_clima(ciudad)
    