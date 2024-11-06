from cambiarTemperatura import cambiarTemperatura 
from llamadaApi import llamadaApi  # Importar la función desde llamadaApi.py
from historialConsultas import agregarAlHistorial

def obtener_clima(ciudad, unidad):
    simbolo, unidad = cambiarTemperatura(unidad)
    datos = llamadaApi(ciudad, unidad)  # Llamar a la función para obtener los datos

    if datos is not None:  # Si hay datos, se extrae el clima
        clima = datos['main']
        resultado = (
            f"Ciudad: {ciudad}\n"
            f"Temperatura: {clima['temp']}°{simbolo}\n"
            f"Máxima: {clima['temp_max']}°{simbolo}\n"
            f"Mínima: {clima['temp_min']}°{simbolo}\n"
            f"Humedad: {clima['humidity']}%"
        ) 
        print(f"Ciudad: {ciudad}")
        print(f"Temperatura: {clima['temp']}°{simbolo}")
        print(f"Máxima: {clima['temp_max']}°{simbolo}")
        print(f"Mínima: {clima['temp_min']}°{simbolo}")
        print(f"Humedad: {clima['humidity']}%")
        agregarAlHistorial(resultado)
        agregarAlHistorial("-----------------")
    else:
        resultado = f"No se pudo obtener el clima para '{ciudad}' debido a un error."
        print(resultado)

    return resultado  # Devolver el resultado formateado para la interfaz
