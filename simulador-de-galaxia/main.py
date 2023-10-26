from controller.controller import crear_eventos
from modelos.galaxia import Galaxia
from modelos.viper import Viper
from modelos.transporte import Transporte
from modelos.nebula import Nebula

#Se crea la galaxia
galaxia= Galaxia()
galaxia.dibujar_galaxia()

#Se crea el arbol de eventos galaticos
arbol= crear_eventos()

#Se instancian las naves
nave_viper= Viper("viper", 2.5, 50)
nave_transporte= Transporte("Cargament",1,200)
nave_nebula= Nebula("Nebula",1.5,100)