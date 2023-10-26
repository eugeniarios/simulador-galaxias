import tkinter as tk
from controller.controller import obtener_eventos
from main import nave_viper, nave_nebula, nave_transporte, galaxia, arbol

planetas= list(galaxia.get_galaxia().nodes)


# Función que se ejecutará cuando se haga clic en el botón "Iniciar Viaje"
def iniciar_viaje():
    naves = {
        nave_viper.get_nombre() : nave_viper,
        nave_nebula.get_nombre() : nave_nebula,
        nave_transporte.get_nombre() : nave_transporte 
    }
    nave_seleccionada= naves[opcion_nave.get()]
    evento= obtener_eventos(arbol)
    carga = carga_entry.get()
    origen = origen_planeta.get()
    destino = destino_planeta.get()
    ruta= nave_seleccionada.encontar_ruta(galaxia.get_galaxia(), origen, destino, int(carga))
    distancia_total= ruta["distancia_carga"] + evento.get_modificador_distancia()

    # Aquí puedes usar los datos ingresados para realizar el viaje, calculando la ruta y otros detalles.

    # Por ahora, solo mostraremos un mensaje de confirmación
    mensaje=f"""
        ---------------------Simulador de galaxias---------------------\n
        ------------Detalle nave------------------\n
        Nave: {nave_seleccionada.get_nombre()}\n Velocidad: {nave_seleccionada.get_velocidad()}\n Capacidad: {nave_seleccionada.get_capacidad_carga()}
        ------------Creando evento----------------
        Evento espacial: {evento}
        ------------Calculando ruta---------------
        Planeta de partida: {origen}\n Planeta destino: {destino}\n Carga: {carga}\n Ruta mas corta: {ruta['ruta']} - Parsecs: {ruta['distancia_od']} \n Parsecs de ruta realizada por {nave_seleccionada.get_nombre()}: {ruta['distancia_carga']}
        Distancia total con evento: {distancia_total}
        ------------Fin viaje----------------
    """
    resultado_label.config(text=mensaje)




# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulador de Rutas de Naves Espaciales en una Galaxia")

# Variables de control para las opciones seleccionadas
opcion_nave = tk.StringVar()
origen_planeta = tk.StringVar()
destino_planeta = tk.StringVar()

# Etiqueta para el título
titulo_label = tk.Label(ventana, text="Simulador de Rutas de Naves Espaciales en una Galaxia")
titulo_label.pack()

# Opción para seleccionar la nave
nave_label = tk.Label(ventana, text="Selecciona una nave:")
nave_label.pack()
nave_opciones = [nave_viper.get_nombre(), nave_transporte.get_nombre(), nave_nebula.get_nombre()]
nave_seleccion = tk.OptionMenu(ventana, opcion_nave, *nave_opciones)
nave_seleccion.pack()

# Entrada para ingresar la carga
carga_label = tk.Label(ventana, text="Carga a transportar:")
carga_label.pack()
carga_entry = tk.Entry(ventana)
carga_entry.pack()

# Opciones para seleccionar el planeta de origen y destino
origen_label = tk.Label(ventana, text="Planeta de origen:")
origen_label.pack()
origen_opciones = planetas
origen_seleccion = tk.OptionMenu(ventana, origen_planeta, *origen_opciones)
origen_seleccion.pack()

destino_label = tk.Label(ventana, text="Planeta de destino:")
destino_label.pack()
destino_opciones = planetas
destino_seleccion = tk.OptionMenu(ventana, destino_planeta, *destino_opciones)
destino_seleccion.pack()

# Botón para iniciar el viaje
iniciar_button = tk.Button(ventana, text="Iniciar Viaje", command=iniciar_viaje)
iniciar_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()