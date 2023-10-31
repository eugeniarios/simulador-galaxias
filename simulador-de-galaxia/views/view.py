import tkinter as tk
from tkinter import font
from tkinter import ttk
from . import util_img, util_ventana
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL, COLOR_MENU_CURSOR_ENCIMA
from config import LOGO,MAPA
from controller.controller import simular_viaje

class Gui(tk.Tk):

    def __init__(self, galaxia, arbol, viper, nebula, transporte):
        super().__init__()
        
        # Variables de control para las opciones seleccionadas
        self._galaxia= util_img.leer_imagen(LOGO,(400, 400))
        self._perfil= util_img.leer_imagen(LOGO,(100, 100))
        self._mapa= util_img.leer_imagen(MAPA,(700, 500))
        self._opcion_nave = tk.StringVar()
        self._origen_planeta = tk.StringVar()
        self._destino_planeta = tk.StringVar()
        self._planetas = list(galaxia.get_galaxia().nodes)
        self._grafo= galaxia.get_galaxia()
        self._arbol= arbol
        self._nave_viper= viper
        self._nave_nebula=nebula
        self._nave_transporte=transporte

        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()


    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Simulador de Rutas de Naves Espaciales en una Galaxia')
        
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(
        self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(
        self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="☰", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="GalaxySimulator")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Euge")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)


    def mostrar_vista_simulador(self):
        # Oculta la vista de la galaxia y muestra la vista del simulador
        self.cuerpo_principal.pack_forget()
        self.crear_vista_simulador()

    def crear_vista_simulador(self):
        # Crear y mostrar los controles de simulación en el cuerpo principal
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
        self._opcion_nave = tk.StringVar()
        self._origen_planeta = tk.StringVar()
        self._destino_planeta = tk.StringVar()
        
        # Crear un estilo ttk para dar una apariencia moderna
        estilo = ttk.Style()
        estilo.configure("TButton", padding=5, relief="flat")
        
        # Crear un marco para los controles
        controles_marco = ttk.LabelFrame(self.cuerpo_principal, text="Simulador", padding=(10, 10))
        controles_marco.pack(padx=20, pady=20, fill='both', expand=True)

        # Opción para seleccionar la nave
        nave_label = ttk.Label(controles_marco, text="Selecciona una nave:")
        nave_label.grid(column=0, row=0, sticky="w")

        nave_opciones = [self._nave_viper, self._nave_transporte, self._nave_nebula]
        nave_seleccion = ttk.Combobox(controles_marco, textvariable=self._opcion_nave, values=nave_opciones, width=60)
        nave_seleccion.grid(column=1, row=0, pady=5, padx=10, sticky="w")
        self._indice_nave= nave_seleccion.current()
        # Entrada para ingresar la carga
        carga_label = ttk.Label(controles_marco, text="Carga a transportar:")
        carga_label.grid(column=0, row=1, sticky="w")
        self._carga_entry = ttk.Entry(controles_marco)
        self._carga_entry.grid(column=1, row=1, pady=5, padx=10, sticky="w")

        # Opciones para seleccionar el planeta de origen y destino
        origen_label = ttk.Label(controles_marco, text="Planeta de origen:")
        origen_label.grid(column=0, row=2, sticky="w")

        origen_seleccion = ttk.Combobox(controles_marco, textvariable=self._origen_planeta, values=self._planetas)
        origen_seleccion.grid(column=1, row=2, pady=5, padx=10, sticky="w")

        destino_label = ttk.Label(controles_marco, text="Planeta de destino:")
        destino_label.grid(column=0, row=3, sticky="w")

        destino_seleccion = ttk.Combobox(controles_marco, textvariable=self._destino_planeta, values=self._planetas)
        destino_seleccion.grid(column=1, row=3, pady=5, padx=10, sticky="w")

        # Botón para iniciar el viaje
        iniciar_button = ttk.Button(controles_marco, text="Iniciar Viaje", command=self.iniciar_simulacion)
        iniciar_button.grid(column=0, row=4, columnspan=2, pady=10)

        # Etiqueta para mostrar el resultado 
        resultado_label = ttk.Label(controles_marco, text="Resultado simulación de viaje")
        resultado_label.grid(column=0, row=5, columnspan=2, pady=10)

        # Cuadro para mostrar el mensaje
        self._resultado = tk.StringVar()
        self._resultado.set("Elija antes de iniciar viaje...")

        # Crear un Canvas para el cuadro de texto con scrollbar
        canvas = tk.Canvas(controles_marco)
        canvas.grid(column=0, row=6, columnspan=2, pady=10, padx=10, sticky="nsew")

        # Agregar scrollbar vertical al canvas
        scrollbar = ttk.Scrollbar(controles_marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.grid(column=3, row=6, sticky='ns')

        # Configurar el canvas para permitir desplazamiento vertical
        canvas.config(yscrollcommand=scrollbar.set)

        # Crear un cuadro de texto dentro del canvas
        self._mensaje_cuadro = tk.Text(canvas, wrap=tk.WORD, background="white", foreground="black", width=80, height=15)
        self._mensaje_cuadro.grid(row=0, column=0, rowspan=5, columnspan=5, sticky="nsew")  # Ajusta los valores de rowspan y columnspan según sea necesario
        self._mensaje_cuadro.insert('1.0', self._resultado.get())  # Insertar contenido inicial

        # Configurar el canvas para contener el cuadro de texto
        canvas.create_window((0, 0), window=self._mensaje_cuadro, anchor='nw')

        # Configura la expansión de la cuadrícula en ambas direcciones
        controles_marco.columnconfigure(0, weight=1)  # Columna 0
        controles_marco.columnconfigure(1, weight=1)  # Columna 1
        canvas.grid(column=0, columnspan=15, rowspan=5, pady=1, padx=1, sticky="nsew")

    def mostrar_vista_galaxia(self):
        #oculta el simulador y muestra el mapa de la galaxia
        self.cuerpo_principal.pack_forget()
        self.crear_vista_galaxia()

    def crear_vista_galaxia(self):
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self._mapa, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
         # Etiqueta de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self._perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        self.buttonGrafo = tk.Button(self.menu_lateral, command=self.mostrar_vista_galaxia)        
        self.buttonSimulador = tk.Button(self.menu_lateral, command=self.mostrar_vista_simulador)        

        buttons_info = [
            ("Grafo de galaxia", "◉", self.buttonGrafo),
            ("Simulador", "◉", self.buttonSimulador),
        ]

        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)   

    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self._galaxia,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def iniciar_simulacion(self):
        self._resultado.set("Ejecutando de la simulación...")
        self.update_idletasks()

        origen = self._origen_planeta.get()
        destino = self._destino_planeta.get()
        carga = float(self._carga_entry.get())
        naves= [
            self._nave_viper, 
            self._nave_nebula, 
            self._nave_transporte
        ]
        
        # Llamar a tu función de simulación con estos datos
        resultado_simulacion = simular_viaje(naves[self._indice_nave-1],self._grafo,origen,destino,carga,self._arbol)

        # Mostrar los resultados en una etiqueta o ventana emergente
        self._resultado.set(resultado_simulacion)
        self.update_idletasks()
        self._mensaje_cuadro.delete('1.0', tk.END)  
        self._mensaje_cuadro.insert('1.0', resultado_simulacion)