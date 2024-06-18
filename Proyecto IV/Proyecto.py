class Proyecto:
    # Constructor de la clase Proyecto
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tareas = []
        self.pila_tareas_prioritarias = []

        
    # Método para representar un objeto Proyecto como una cadena de texto
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Fecha de Inicio: {self.fecha_inicio}, Fecha de Vencimiento: {self.fecha_vencimiento}, Estado: {self.estado}, Empresa: {self.empresa}, Gerente: {self.gerente}, Equipo: {', '.join(self.equipo)}"

    # Método para agregar una tarea al proyecto
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    # Método para agregar una tarea al final de la lista de tareas
    def agregar_tarea_al_final(self, tarea):
        self.tareas.append(tarea)

    # Método para agregar una tarea en una posición específica de la lista de tareas
    def agregar_tarea_en_posicion(self, posicion, tarea):
        self.tareas.insert(posicion, tarea)

    # Método para eliminar una tarea del proyecto
    def eliminar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                self.tareas.remove(tarea)
                return True
        return False

    # Método para buscar una tarea por un criterio y un valor específico
    def buscar_tarea(self, criterio, valor):
        if criterio == 'id':
            for tarea in self.tareas:
                if tarea.id == valor:
                    return tarea
        elif criterio == 'nombre':
            for tarea in self.tareas:
                if tarea.nombre.lower() == valor.lower():
                    return tarea
        elif criterio == 'empresa':
            for tarea in self.tareas:
                if tarea.empresa_cliente.lower() == valor.lower():
                    return tarea
        return None

    # Método para actualizar una tarea por un id y un diccionario de argumentos
    def actualizar_tarea(self, id_tarea, **kwargs):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                for key, value in kwargs.items():
                    setattr(tarea, key, value)
                return True
        return False

    # Método para listar todas las tareas del proyecto
    def listar_tareas(self):
        if self.tareas:
            for tarea in self.tareas:
                print(tarea)
        else:
            print("No hay tareas registradas para este proyecto.")

    # Método para agregar una subtarea a una tarea en el proyecto
    def agregar_subtarea_a_tarea(self, id_tarea, subtarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                tarea.agregar_subtarea(subtarea)
                return True
        return False

    # Método para eliminar una subtarea de una tarea en el proyecto
    def eliminar_subtarea_de_tarea(self, id_tarea, id_subtarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                return tarea.eliminar_subtarea(id_subtarea)
        return False

    # Método para actualizar una subtarea de una tarea en el proyecto
    def actualizar_subtarea_en_tarea(self, id_tarea, id_subtarea, **kwargs):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                return tarea.actualizar_subtarea(id_subtarea, **kwargs)
        return False

    # Método para listar las subtareas de una tarea en el proyecto
    def listar_subtareas_de_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                return tarea.listar_subtareas()
        return []
    
    # Método para agregar una tarea prioritaria a la pila
    def agregar_tarea_prioritaria(self, tarea):
        self.pila_tareas_prioritarias.append(tarea)

    # Método para eliminar la tarea más prioritaria de la pila
    def eliminar_tarea_prioritaria(self):
        if self.pila_tareas_prioritarias:
            return self.pila_tareas_prioritarias.pop()
        else:
            return None
        
    # Método para consultar la tarea más prioritaria de la pila
    def consultar_tarea_prioritaria(self):
        if self.pila_tareas_prioritarias:
            return self.pila_tareas_prioritarias[-1]
        else:
            return None
        
    def consultar_tareas_prioritaria(self):
        if self.pila_tareas_prioritarias:
            return self.pila_tareas_prioritarias
        else:
            return None