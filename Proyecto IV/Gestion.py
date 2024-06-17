# Clase para gestionar los proyectos
class GestorProyectos:
    def __init__(self):
        self.proyectos = []
    # Método para agregar un proyecto a la lista de proyectos
    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
    # Método para buscar un proyecto por un criterio y un valor específico 
    def buscar_proyecto(self, criterio, valor):
        return [proyecto for proyecto in self.proyectos if getattr(proyecto, criterio, None) == valor]
    
    def obtener_proyecto(self, id):
        for proyecto in self.proyectos:
            if proyecto.id == id:
                return proyecto
        return False

    # Método para modificar un proyecto por un id y un diccionario de argumentos
    def modificar_proyecto(self, id, **kwargs):
        for proyecto in self.proyectos:
            if proyecto.id == id:
                for key, value in kwargs.items():
                    setattr(proyecto, key, value)
                return True
        return False

    # Método para eliminar un proyecto por un id
    def eliminar_proyecto(self, id):
        for proyecto in self.proyectos:
            if proyecto.id == id:
                self.proyectos.remove(proyecto)
                return True
        return False
    
    # Método para listar todos los proyectos
    def listar_proyectos(self):
        return self.proyectos

    # Método para agregar una tarea a un proyecto
    def agregar_tarea_a_proyecto(self, id_proyecto, tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                proyecto.agregar_tarea(tarea)
                return True
        return False
    
    # Método para agregar una tarea al final de un proyecto
    def agregar_tarea_al_final_de_proyecto(self, id_proyecto, tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                proyecto.agregar_tarea_al_final(tarea)
                return True
        return False
    
    # Método para agregar una tarea en una posición específica de un proyecto
    def agregar_tarea_en_posicion_de_proyecto(self, id_proyecto, posicion, tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                proyecto.agregar_tarea_en_posicion(posicion, tarea)
                return True
        return False
    
    # Método para actualizar una tarea en un proyecto
    def actualizar_tarea_en_proyecto(self, id_proyecto, id_tarea, **kwargs):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.actualizar_tarea(id_tarea, **kwargs)
        return False

    # Método para eliminar una tarea de un proyecto
    def eliminar_tarea_de_proyecto(self, id_proyecto, id_tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.eliminar_tarea(id_tarea)

    # Método para buscar tareas por nombre en un proyecto      
    def buscar_tareas_por_nombre_en_proyecto(self, id_proyecto, nombre_tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return [tarea for tarea in proyecto.tareas if tarea.nombre.lower() == nombre_tarea.lower()]
        return []
    
    # Método para listar las tareas de un proyecto
    def listar_tareas_de_proyecto(self, id_proyecto):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                proyecto.listar_tareas()
                return True
        return False

    # Método para verificar si un proyecto existe
    def proyecto_existe(self, id_proyecto):
        return any(proyecto.id == id_proyecto for proyecto in self.proyectos)

    # Método para agregar subtarea a tarea en proyecto  
    def agregar_subtarea_a_tarea_en_proyecto(self, id_proyecto, id_tarea, subtarea):
        if not self.proyecto_existe(id_proyecto):
            return False
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.agregar_subtarea_a_tarea(id_tarea, subtarea)
        return False

    # Método para eliminar subtarea de tarea en proyecto
    def eliminar_subtarea_de_tarea_en_proyecto(self, id_proyecto, id_tarea, id_subtarea):
        if not self.proyecto_existe(id_proyecto):
            return False
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.eliminar_subtarea_de_tarea(id_tarea, id_subtarea)
        return False

    # Método para actualizar subtarea de tarea en proyecto
    def actualizar_subtarea_en_tarea_en_proyecto(self, id_proyecto, id_tarea, id_subtarea, **kwargs):
        if not self.proyecto_existe(id_proyecto):
            return False
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.actualizar_subtarea_en_tarea(id_tarea, id_subtarea, **kwargs)
        return False

    # Método para listar subtareas de tarea en proyecto
    def listar_subtareas_de_tarea_en_proyecto(self, id_proyecto, id_tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                for tarea in proyecto.tareas:
                    if tarea.id == id_tarea:
                        return tarea.subtareas
        return []

    # Método para agregar tarea prioritaria a proyecto
    def agregar_tarea_prioritaria_a_proyecto(self, id_proyecto, tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                proyecto.agregar_tarea_prioritaria(tarea)
                return True
        return False

    # Método para eliminar tarea prioritaria de proyecto
    def eliminar_tarea_prioritaria_de_proyecto(self, id_proyecto):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.eliminar_tarea_prioritaria()
        return None

    # Método para consultar tarea prioritaria de proyecto
    def consultar_tarea_prioritaria_de_proyecto(self, id_proyecto):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.consultar_tarea_prioritaria()
        return None