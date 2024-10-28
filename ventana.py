import tkinter
from app import obtener_clima

ventana = tkinter.Tk()
ventana.geometry("500x500")

# Crear un Frame para centrar el contenido
frame = tkinter.Frame(ventana)
frame.pack(expand=True)  # Permitir que el Frame se expanda en el centro

# Función para obtener el clima
def obtenerClima(boton):
    # Obtener los valores de las cajas de texto
    ciudad = cajaCiudad.get()
    unidad = cajaTemperatura.get()
    
    # Llamar a la función obtener_clima con las variables
    resultado = obtener_clima(ciudad, unidad)
    
    # Mostrar el resultado en el label
    resultadoLabel.config(text=resultado)

    # Preguntar si desea continuar con otra consulta
    continuarLabel.config(text="¿Desea realizar otra consulta? (S/N)")
    cajaContinuar.grid(row=8, column=0, padx=10)  # Mostrar la caja de texto para continuar
    botonContinuar.grid()  # Mostrar el botón de continuar
    boton.grid_remove()  # Ocultar el botón "Clima actual"

# Procesar la respuesta del usuario
def procesarContinuar():
    respuesta = cajaContinuar.get().strip().upper()

    # Procesar la respuesta del usuario
    if respuesta == "S":
        # Limpiar las entradas y el label de resultados
        cajaCiudad.delete(0, tkinter.END)
        cajaTemperatura.delete(0, tkinter.END)
        resultadoLabel.config(text="")
        continuarLabel.config(text="")
        cajaContinuar.delete(0, tkinter.END)  # Limpiar caja de continuar
        cajaContinuar.grid_remove()  # Ocultar la caja de continuar
        botonContinuar.grid_remove()  # Ocultar el botón de continuar
        botonClimaActual.grid()  # Volver a mostrar el botón "Clima actual"

        # Reiniciar la aplicación (opcional)
        iniciarAplicacion()

    elif respuesta == "N":
        ventana.destroy()  # Cerrar la aplicación

    else:
        continuarLabel.config(text="Respuesta inválida. Por favor, ingrese 'S' o 'N'.")

def iniciarAplicacion():
    # Reiniciar todos los elementos de la interfaz
    resultadoLabel.config(text="")
    continuarLabel.config(text="")
    cajaContinuar.grid_remove()  # Ocultar la caja de continuar
    botonContinuar.grid_remove()  # Ocultar el botón de continuar

# Etiqueta para la entrada de ciudad
tituloIngreseCiudad = tkinter.Label(frame, text="Ingrese el nombre de la ciudad")
tituloIngreseCiudad.grid(row=0, column=0, padx=10, pady=(10, 0))  # Espacio superior

# Caja de entrada para ciudad
cajaCiudad = tkinter.Entry(frame)
cajaCiudad.grid(row=1, column=0, padx=10, pady=(0, 10))  # Espacio inferior

# Etiqueta para la entrada de unidad
tituloIngreseUnidad = tkinter.Label(frame, text="Ingrese la unidad de temperatura (C/F):")
tituloIngreseUnidad.grid(row=2, column=0, padx=10, pady=(10, 0))  # Espacio superior

# Caja de entrada para unidad
cajaTemperatura = tkinter.Entry(frame)
cajaTemperatura.grid(row=3, column=0, padx=10, pady=(0, 20))  # Espacio inferior

# Label para mostrar los resultados
resultadoLabel = tkinter.Label(frame, text="")
resultadoLabel.grid(row=4, column=0, padx=10, pady=(10, 0))  # Espacio superior

# Label para preguntar si quiere continuar
continuarLabel = tkinter.Label(frame, text="")
continuarLabel.grid(row=5, column=0, padx=10, pady=(10, 0))  # Espacio superior

# Caja de texto para continuar (declarar fuera de las funciones)
cajaContinuar = tkinter.Entry(frame)

# Botón para obtener el clima
botonClimaActual = tkinter.Button(frame, text="Clima actual", command=lambda: obtenerClima(botonClimaActual))
botonClimaActual.grid(row=6, column=0, padx=10, pady=(10, 20))  # Espacio inferior

# Botón para procesar continuar (inicialmente oculto)
botonContinuar = tkinter.Button(frame, text="Continuar", command=procesarContinuar)
botonContinuar.grid(row=7, column=0, padx=10, pady=(10, 0))  # Posición inicial
botonContinuar.grid_remove()  # Ocultar el botón al inicio

ventana.title("App del Clima")
ventana.mainloop()
