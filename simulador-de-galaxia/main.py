from modelos.galaxia import Galaxia
from modelos.viper import Viper
from modelos.transporte import Transporte
from modelos.nebula import Nebula
from modelos.eventos import Evento
import random 
from controller.controller import crear_eventos, obtener_eventos, imprimir_resultados


galaxia= Galaxia()
galaxia.dibujar_galaxia()

nave_viper= Viper("viper", 2.5, 50)
nave_transporte= Transporte("Cargament",1,200)
nave_nebula= Nebula("Nebula",1.5,100)
carga= 20
origen= "Picon" 
destino= "Aquarion"

arbol= crear_eventos()
ruta= nave_nebula.encontar_ruta(galaxia.get_galaxia(), origen, destino, carga)
evento= obtener_eventos(arbol)
modificador= evento.get_modificador_distancia()
distancia_total= ruta["distancia_carga"] + modificador

imprimir_resultados(nave_nebula,ruta,evento,origen,destino,carga,distancia_total)