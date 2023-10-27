from controller.controller import crear_eventos
from modelos.galaxia import Galaxia
from modelos.viper import Viper
from modelos.transporte import Transporte
from modelos.nebula import Nebula
from views.view import Gui

#Se crea la galaxia
galaxia= Galaxia()
galaxia.dibujar_galaxia()
print("Grafo de galaxias creado exitosamente")

#Se crea el arbol de eventos galaticos
arbol= crear_eventos()
print("Arbol de eventos creado exitosamente")

#Se instancian las naves
nave_viper= Viper("viper", 2.5, 50)
nave_transporte= Transporte("Cargament",1,200)
nave_nebula= Nebula("Nebula",1.5,100)

#ejecuta ventana interfaz
interfaz= Gui(galaxia,nave_viper,nave_nebula,nave_transporte)
interfaz.mainloop()