import tkinter
from app import obtener_clima, pronostico_extendido

# Función para mostrar el menú de inicio
def mostrar_menu():
    for widget in frame.winfo_children():
        widget.destroy()

    botonClimaActual = tkinter.Button(frame, text="Clima actual", command=mostrar_campos_clima_actual)
    botonClimaActual.pack(pady=10)
    botonPronosticoExtendido = tkinter.Button(frame, text="Pronóstico extendido", command=mostrar_campos_pronostico)
    botonPronosticoExtendido.pack(pady=10)

# Función para mostrar los campos de entrada para el clima actual
def mostrar_campos_clima_actual():
    for widget in frame.winfo_children():
        widget.destroy()
        
    etiquetaCiudad = tkinter.Label(frame, text="Ingrese la ciudad:")
    etiquetaCiudad.pack()
    cajaCiudad = tkinter.Entry(frame)
    cajaCiudad.pack()

    etiquetaUnidad = tkinter.Label(frame, text="Ingrese la unidad de temperatura (C/F):")
    etiquetaUnidad.pack()
    cajaUnidad = tkinter.Entry(frame)
    cajaUnidad.pack()

    botonObtenerClima = tkinter.Button(frame, text="Obtener Clima", command=lambda: obtenerClima(cajaCiudad.get(), cajaUnidad.get()))
    botonObtenerClima.pack(pady=10)
    botonVolver = tkinter.Button(frame, text="Volver al menú", command=mostrar_menu)
    botonVolver.pack(pady=5)
    botonCerrar = tkinter.Button(frame, text="Cerrar", command=ventana.quit)
    botonCerrar.pack(pady=5)

# Función para mostrar los campos de entrada para el pronóstico extendido
def mostrar_campos_pronostico():
    for widget in frame.winfo_children():
        widget.destroy()
        
    etiquetaCiudad = tkinter.Label(frame, text="Ingrese la ciudad:")
    etiquetaCiudad.pack()
    cajaCiudad = tkinter.Entry(frame)
    cajaCiudad.pack()

    etiquetaUnidad = tkinter.Label(frame, text="Ingrese la unidad de temperatura (C/F):")
    etiquetaUnidad.pack()
    cajaUnidad = tkinter.Entry(frame)
    cajaUnidad.pack()

    botonObtenerPronostico = tkinter.Button(frame, text="Obtener Pronóstico", command=lambda: obtenerPronostico(cajaCiudad.get(), cajaUnidad.get()))
    botonObtenerPronostico.pack(pady=10)
    botonVolver = tkinter.Button(frame, text="Volver al menú", command=mostrar_menu)
    botonVolver.pack(pady=5)
    botonCerrar = tkinter.Button(frame, text="Cerrar", command=ventana.quit)
    botonCerrar.pack(pady=5)

# Función para obtener el clima actual
def obtenerClima(ciudad, unidad):
    resultado = obtener_clima(ciudad, unidad)
    mostrar_resultado(resultado)

# Función para obtener el pronóstico extendido
def obtenerPronostico(ciudad, unidad):
    global dias_pronostico, indice_dia
    dias_pronostico = pronostico_extendido(ciudad, unidad)
    print(f"Datos del pronóstico: {dias_pronostico}")  # Ver los datos recibidos
    indice_dia = 0
    if isinstance(dias_pronostico, list) and len(dias_pronostico) > 0:
        mostrar_dia()
    else:
        mostrar_resultado("Error al obtener el pronóstico. Verifique la ciudad y la unidad.")

# Función para mostrar el día actual del pronóstico
def mostrar_dia():
    for widget in frame.winfo_children():
        widget.destroy()
    
    try:
        dia_actual = dias_pronostico[indice_dia]
        print(f"Día actual: {dia_actual}")  # Ver el día que se va a mostrar
        texto_dia = (
            f"Fecha: {dia_actual['fecha']}\n"
            f"Temperatura: {dia_actual['temperatura']}°\n"
            f"Temperatura mínima: {dia_actual['temp_min']}°\n"
            f"Temperatura máxima: {dia_actual['temp_max']}°\n"
            f"Descripción: {dia_actual['descripcion']}\n"
            f"Humedad: {dia_actual['humedad']}%\n"
            f"Velocidad del viento: {dia_actual['velocidad_viento']} m/s\n"
        )
    except (KeyError, TypeError) as e:
        texto_dia = f"Error de formato de datos: {e}"
        print(f"Error: {e}")  # Mostrar el error en la consola

    etiquetaDia = tkinter.Label(frame, text=texto_dia, justify="left")
    etiquetaDia.pack()

    # Botones de navegación
    if indice_dia > 0:
        botonAnterior = tkinter.Button(frame, text="Día anterior", command=lambda: navegar_dia(-1))
        botonAnterior.pack(side="left", padx=5)
    if indice_dia < len(dias_pronostico) - 1:
        botonSiguiente = tkinter.Button(frame, text="Día siguiente", command=lambda: navegar_dia(1))
        botonSiguiente.pack(side="right", padx=5)

    botonVolver = tkinter.Button(frame, text="Volver al menú", command=mostrar_menu)
    botonVolver.pack(pady=5)
    botonCerrar = tkinter.Button(frame, text="Cerrar", command=ventana.quit)
    botonCerrar.pack(pady=5)

# Función para navegar entre días
def navegar_dia(direccion):
    global indice_dia
    indice_dia += direccion
    mostrar_dia()

# Función para mostrar el resultado en la interfaz
def mostrar_resultado(resultado):
    for widget in frame.winfo_children():
        widget.destroy()

    etiquetaResultado = tkinter.Label(frame, text=resultado, justify="left", wraplength=400)
    etiquetaResultado.pack()

    botonVolver = tkinter.Button(frame, text="Volver al menú", command=mostrar_menu)
    botonVolver.pack(pady=5)
    botonCerrar = tkinter.Button(frame, text="Cerrar", command=ventana.quit)
    botonCerrar.pack(pady=5)

# Configuración de la ventana principal
ventana = tkinter.Tk()
ventana.geometry("500x500")
ventana.title("App del Clima")

# Crear un Frame para centrar el contenido
frame = tkinter.Frame(ventana)
frame.pack(expand=True)

# Mostrar el menú inicial
mostrar_menu()

# Ejecutar la aplicación
ventana.mainloop()
