class Subtarea:
    def __init__(self, id, nombre, descripcion, estado_actual, porcentaje):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Estado: {self.estado_actual}, Porcentaje: {self.porcentaje}%"