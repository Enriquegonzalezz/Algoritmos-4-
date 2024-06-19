class Tarea:
    def __init__(self, id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje):
        self.id = id
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje
        self.subtareas = []

    # Método para representar un objeto Tarea como una cadena de texto
    def __str__(self):
        return f"Tarea {self.id}: {self.nombre}, Cliente: {self.empresa_cliente}, Estado: {self.estado_actual}, Completado: {self.porcentaje}%"

    # Método para agregar una subtarea a la lista de subtareas
    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)

    # Método para actualizar una subtarea por un id y un diccionario de argumentos
    def actualizar_subtarea(self, id_subtarea, **kwargs):
        for subtarea in self.subtareas:
            if subtarea.id == id_subtarea:
                for key, value in kwargs.items():
                    setattr(subtarea, key, value)
                return True
        return False
    
    # Método para eliminar una subtarea por un id   
    def eliminar_subtarea(self, id_subtarea):
        for subtarea in self.subtareas:
            if subtarea.id == id_subtarea:
                self.subtareas.remove(subtarea)
                return True
        return False
    
    # Método para listar todas las subtareas
    def listar_subtareas(self):
        if self.subtareas:
            for subtarea in self.subtareas:
                print(subtarea)
        else:
            print("No hay subtareas para esta tarea.")

    def calcular_progreso(self):
        if not self.subtareas:
            return 0
        total = len(self.subtareas)
        completadas = sum(1 for subtarea in self.subtareas if subtarea.estado_actual == 'Completado')
        self.porcentaje = (completadas / total) * 100