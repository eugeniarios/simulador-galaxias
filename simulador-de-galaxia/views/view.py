import tkinter as tk
from tkinter import font
from tkinter import ttk
from controller.controller import obtener_eventos
from . import util_img, util_ventana
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL, COLOR_MENU_CURSOR_ENCIMA


class Gui(tk.Tk):

    def __init__(self, galaxia, viper, nebula, transporte):
        super().__init__()
        # Variables de control para las opciones seleccionadas
        self._galaxia= util_img.leer_imagen("simulador-de-galaxia/img/logo.png",(600, 400))
        self._perfil= util_img.leer_imagen("simulador-de-galaxia/img/logo.png",(100, 100))
        self._mapa= util_img.leer_imagen("simulador-de-galaxia/img/galaxias-interconectadas.png",(700, 500))
        self._opcion_nave = tk.StringVar()
        self._origen_planeta = tk.StringVar()
        self._destino_planeta = tk.StringVar()
        self._planetas = list(galaxia.get_galaxia().nodes)
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
        self.opcion_nave = tk.StringVar()
        self.origen_planeta = tk.StringVar()
        self.destino_planeta = tk.StringVar()

        # Crear un estilo ttk para dar una apariencia moderna
        estilo = ttk.Style()
        estilo.configure("TButton", padding=5, relief="flat")
        
        # Crear un marco para los controles
        controles_marco = ttk.LabelFrame(self.cuerpo_principal, text="Simulador", padding=(10, 10))
        controles_marco.pack(padx=20, pady=20)

        # Opción para seleccionar la nave
        nave_label = ttk.Label(controles_marco, text="Selecciona una nave:")
        nave_label.grid(column=0, row=0, sticky="w")

        nave_opciones = [self._nave_viper.get_nombre(), self._nave_transporte.get_nombre(), self._nave_nebula.get_nombre()]
        nave_seleccion = ttk.Combobox(controles_marco, textvariable=self.opcion_nave, values=nave_opciones)
        nave_seleccion.grid(column=1, row=0, pady=5, padx=10, sticky="w")

        # Entrada para ingresar la carga
        carga_label = ttk.Label(controles_marco, text="Carga a transportar:")
        carga_label.grid(column=0, row=1, sticky="w")

        carga_entry = ttk.Entry(controles_marco)
        carga_entry.grid(column=1, row=1, pady=5, padx=10, sticky="w")

        # Opciones para seleccionar el planeta de origen y destino
        origen_label = ttk.Label(controles_marco, text="Planeta de origen:")
        origen_label.grid(column=0, row=2, sticky="w")

        origen_seleccion = ttk.Combobox(controles_marco, textvariable=self.origen_planeta, values=self._planetas)
        origen_seleccion.grid(column=1, row=2, pady=5, padx=10, sticky="w")

        destino_label = ttk.Label(controles_marco, text="Planeta de destino:")
        destino_label.grid(column=0, row=3, sticky="w")

        destino_seleccion = ttk.Combobox(controles_marco, textvariable=self.destino_planeta, values=self._planetas)
        destino_seleccion.grid(column=1, row=3, pady=5, padx=10, sticky="w")

        # Botón para iniciar el viaje
        iniciar_button = ttk.Button(controles_marco, text="Iniciar Viaje", command=self.iniciar_simulacion)
        iniciar_button.grid(column=0, row=4, columnspan=2, pady=10)

        # Etiqueta para mostrar el resultado
        resultado_label = ttk.Label(self.cuerpo_principal, text="Detalle de ")
        resultado_label.pack()

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
        # Aquí puedes obtener los datos ingresados por el usuario y realizar la simulación
        origen = self._origen_planeta.get()
        destino = self._destino_planeta.get()
        nave = self._opcion_nave.get()
        carga = self._carga_entry.get()

        # Llamar a tu función de simulación con estos datos
        resultado_simulacion = "realizar_simulacion(origen, destino, nave, carga)"

        # Mostrar los resultados en una etiqueta o ventana emergente
        resultado_label = tk.Label(self.cuerpo_principal, text=resultado_simulacion)
        resultado_label.pack()
