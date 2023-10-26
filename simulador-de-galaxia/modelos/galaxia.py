import networkx as nx 
import matplotlib.pyplot as plt

class Galaxia:
    def __init__(self): 
        planetas = [
            "Aquarion", 
            "Aerilon", 
            "Caprica", 
            "Canceron", 
            "Sagitara", 
            "Scorpia", 
            "Tauron", 
            "Libran", 
            "Picon", 
            "Leonis", 
            "Virgon", 
            "Gemenon"
        ]

            # Definimos las distancias entre planetas
        distancias = {
            "Aquarion": {"Aerilon": 5, "Canceron": 4},
            "Aerilon": {"Caprica": 3},
            "Caprica": {"Tauron": 5, "Sagitara": 6},
            "Canceron": {"Scorpia": 3, "Sagitara": 4},
            "Sagitara": {"Scorpia": 3, "Gemenon": 4, "Virgon": 5, "Tauron": 6},
            "Scorpia": {"Gemenon": 5},
            "Tauron": {"Libran": 5, "Picon": 4},
            "Libran": {"Picon": 4},
            "Picon": {"Leonis": 5},
            "Leonis": {"Gemenon": 3},
            "Virgon": {"Leonis": 3},
            "Gemenon": {}
        }
        self._galaxia= nx.Graph() 
        self._galaxia.add_nodes_from(planetas)
        
        for origen, destinos in distancias.items():
            for destino, distancia in destinos.items():
                self._galaxia.add_edge(origen, destino, distancia=distancia)

    def get_galaxia(self):
        return self._galaxia
    
    def set_galaxia(self,galaxia): 
        self._galaxia= galaxia

  


    def dibujar_galaxia(self):
        etiquetas={}
        for planeta_a, planeta_b in self._galaxia.edges():
            distancia= self._galaxia.get_edge_data(planeta_a, planeta_b)["distancia"]
            etiquetas[(planeta_a, planeta_b)]= f"{distancia}"
        
        pos= nx.spring_layout(self._galaxia)
        nx.draw(self._galaxia, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold')
        nx.draw_networkx_edges(self._galaxia, pos)
        nx.draw_networkx_edge_labels(self._galaxia, pos, edge_labels=etiquetas, font_size=8, font_color='black', verticalalignment="bottom")


        plt.title("GalaxiasInterconectadas")
        plt.savefig("simulador-galaxias\simulador-de-galaxia\grafo_img\galaxias-interconectadas.png")   

