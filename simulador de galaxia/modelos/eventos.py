class Evento: 
    def __init__(self, nombre, descripcion, modificador_distancia):
        self._nombre= nombre
        self._descripcion= descripcion
        self._modificador_distancia=modificador_distancia
        self._hijo_derecho=None
        self._hijo_izquierdo=None


    def get_nombre(self):
        return self._nombre
    def get_descripcion(self):
        return self._descripcion
    def get_modificador_distancia(self):
        return self._modificador_distancia
    def get_hijo_derecho(self):
        return self._hijo_derecho
    def get_hijo_izquierdo(self):
        return self._hijo_izquierdo

    
    def set_nombre(self, nombre):
        self._nombre=nombre
    def set_descripcion(self, descripcion):
        self._descripcion= descripcion
    def set_modificador_distancia(self, modificador_distancia):
        self._modificador_distancia=modificador_distancia
    def set_hijo_derecho(self, hijo_derecho):
        self._hijo_derecho=hijo_derecho
    def set_hijo_izquierdo(self, hijo_izquierdo):
        self._hijo_izquierdo=hijo_izquierdo

    def __str__(self):
        return f"{self._nombre} - {self._descripcion} - distancia afectada: {self._modificador_distancia}"
    



