from .nave import NaveEspacial


class Transporte(NaveEspacial):
     def encontrar_ruta(self, grafo, origen, destino, carga):
        distancias = {nodo: float('inf') for nodo in grafo.nodes}
        distancias[origen] = 0
        nodos_no_visitados = set(grafo.nodes)
        distancia_origen_destino = 0
        padres = {}
        
        while nodos_no_visitados:
            nodo_actual = min(nodos_no_visitados, key=lambda nodo: distancias[nodo])
            nodos_no_visitados.remove(nodo_actual)
            
            for vecino in grafo.neighbors(nodo_actual):
                distancia_arco = grafo.get_edge_data(nodo_actual, vecino)["distancia"]
                velocidad_nave = self._velocidad
                

                if self._capacidad_carga / 2 < carga: 
                    distancia_arco = max( distancia_arco + 1)
                
                distancia_total = distancias[nodo_actual] + distancia_arco / velocidad_nave

                if distancia_total < distancias[vecino]:
                    distancias[vecino] = distancia_total
                    padres[vecino] = nodo_actual
        
        # Reconstruir la ruta
        ruta = [destino]
        actual = destino
        while actual != origen:
            actual = padres[actual]
            ruta.insert(0, actual)

        for i in range(len(ruta) - 1):
            distancia_origen_destino += grafo.get_edge_data(ruta[i], ruta[i+1])["distancia"]
        
        distancia_total_con_carga= lambda distancia_origen_destino: distancia_origen_destino + 1 if self._capacidad_carga / 2 < carga else distancia_origen_destino
        
        
        datos= {
            "ruta":ruta,
            "distancia_carga":distancia_total_con_carga(distancia_origen_destino), 
            "distancia_od":distancia_origen_destino
        }

        return datos
     