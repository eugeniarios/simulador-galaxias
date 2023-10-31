from abc import ABC,abstractmethod
class NaveEspacial:
    def __init__(self, nombre, velocidad, capacidad_carga):
        self._nombre=nombre 
        self._velocidad=velocidad
        self._capacidad_carga=capacidad_carga

    def get_nombre(self): 
        return self._nombre
    def get_velocidad(self):
        return self._velocidad
    def get_capacidad_carga(self):
        return self._capacidad_carga
    def get_descripcion(self):
        return f"capacidad: {self._capacidad_carga} - velocidad: {self._velocidad}"

    
    def set_nombre(self, nombre):
        self._nombre=nombre
    def set_velocidad(self, velocidad):
        self._velocidad=velocidad 
    def set_capacidad_carga(self, capacidad_carga):
        self._capacidad_carga=capacidad_carga


    @abstractmethod
    def encontrar_ruta(self,galaxia, origen, destino, carga):
        pass