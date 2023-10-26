import random
from modelos.eventos import Evento


def crear_eventos():
    agujero_negro= Evento(1,"agujero negro, se reduce la distancia a un parsec", -1)
    tormenta_espacial= Evento(2, "tormenta espacial se incrementa la distancia en un parsec", 1)
    lluvia_meteoritos= Evento (3,"lluvia de meteoritos se incrementa la distancia en dos parsec", 2)
    evento_vacio= Evento (4, "no hay evento", 0)
    evento_vacio2=Evento (5, "no hay evento", 0)
    ataque_pirata=Evento (6,"ataque pirata se incrementa la distancia en tres parsec", 3)
    fallo_motor= Evento (7, "fallo del motor se incrementa la distancia en dos parsec", 2)

    agujero_negro.set_hijo_derecho(tormenta_espacial)
    agujero_negro.set_hijo_izquierdo(lluvia_meteoritos)
    tormenta_espacial.set_hijo_derecho(evento_vacio)
    tormenta_espacial.set_hijo_izquierdo(lluvia_meteoritos)
    lluvia_meteoritos.set_hijo_derecho(evento_vacio2)
    lluvia_meteoritos.set_hijo_izquierdo(ataque_pirata)
    ataque_pirata.set_hijo_derecho(fallo_motor)
    

    return agujero_negro

def obtener_eventos(nodo):
    eventos=[]
    def recorrer_arbol(nodo):
        if nodo is not None: 
            eventos.append(nodo)
            recorrer_arbol(nodo.get_hijo_izquierdo())
            recorrer_arbol(nodo.get_hijo_derecho())
    recorrer_arbol(nodo)
    if eventos:
        return random.choice(eventos)
    else:
        return Evento(0, "no hay eventos en el arbol",0)
    
def imprimir_resultados(nave,ruta,evento,origen,destino,carga,distancia_total):
    print("---------------------Simulador de galaxias---------------------")
    print("------------Detalle nave------------------")
    print(f"-> Nave: {nave.get_nombre()}\n-> Velocidad: {nave.get_velocidad()}\n-> Capacidad: {nave.get_capacidad_carga()}")
    print("------------Creando evento----------------")
    print(f"-> Evento espacial: {evento}")
    print("------------Calculando ruta---------------")
    print(f"-> Planeta de partida: {origen}\n-> Planeta destino: {destino}\n-> Carga: {carga}\n-> Ruta mas corta: {ruta['ruta']} - Parsecs: {ruta['distancia_od']} \n-> Parsecs de ruta realizada por {nave.get_nombre()}: {ruta['distancia_carga']}")
    print(f"-> Distancia total con evento: {distancia_total}")
    print("------------Fin viaje----------------")
