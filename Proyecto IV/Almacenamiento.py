import json
from Varias import tarea_a_diccionario, proyecto_a_diccionario

def GetConfig(route="config.txt"):
    List = []
    with open(route,"r") as file:
        for line in file:
            List.append(line.replace("\n", ""))
    return List

config = GetConfig()
proyectos_file = config[0]
subtareas_file = config[1]

def cargar_proyectos():
    with open(proyectos_file, 'r') as file:
        return json.load(file)

# Método para guardar los proyectos en un proyectos_file JSON
def guardar_proyectos(proyectos):
    with open(proyectos_file, 'w') as file:
        json.dump(proyectos, file, indent=4, default=str)

# Método para agregar un proyecto al proyectos_file JSON
def agregar_proyecto(proyecto):
    proyectos = cargar_proyectos()
    proyectos['proyectos'].append(proyecto.__dict__)
    guardar_proyectos(proyectos)

# Método para actualizar un proyecto en el proyectos_file JSON
def actualizar_proyecto(proyecto):
    proyectos = cargar_proyectos()
    for proyectoJ in proyectos['proyectos']:
        if proyectoJ['id'] == proyecto.id:
            ProyectoDict = proyecto_a_diccionario(proyecto)
            ProyectoDict['tareas'] = [tarea_a_diccionario(tarea) for tarea in proyecto.obtener_tareas()]
            ProyectoDict['pila_tareas_prioritarias'] = [tarea_a_diccionario(tarea) for tarea in proyecto.obtener_tareas_prioritarias()]
            proyectoJ.update(ProyectoDict)
    guardar_proyectos(proyectos)

# Método para eliminar un proyecto del proyectos_file JSON
def eliminar_proyecto(id_proyecto):
    proyectos = cargar_proyectos()
    proyectos['proyectos'] = [proyecto for proyecto in proyectos['proyectos'] if proyecto['id'] != id_proyecto]
    guardar_proyectos(proyectos)

# Método para cargar las subtareas desde un proyectos_file JSON
def cargar_subtareas():
    with open(subtareas_file, 'r') as file:
        return json.load(file)

# Método para guardar las subtareas en un subtareas_file JSON
def guardar_subtareas(subtareas_por_tarea):
    with open(subtareas_file, 'w') as file:
        json.dump(subtareas_por_tarea, file, indent=4, default=str)

# Método para agregar una subtarea a la tarea y guardar el cambio en el subtareas_file JSON
def agregar_subtarea_y_guardar(id_tarea, subtarea, id_proyecto):
    subtareas_por_tarea = cargar_subtareas()
    for entrada in subtareas_por_tarea['subtareas_por_tarea']:
        if entrada['id_proyecto'] == id_proyecto and entrada['id_tarea'] == id_tarea:
            entrada['subtareas'].append(subtarea.__dict__)
            break
    else:
        subtareas_por_tarea['subtareas_por_tarea'].append({
            "id_proyecto": id_proyecto,
            "id_tarea": id_tarea,
            "subtareas": [subtarea.__dict__]
        })
    guardar_subtareas(subtareas_por_tarea)

# Método para modificar una subtarea existente y guardar el cambio en el subtareas_file JSON
def modificar_subtarea_y_guardar(id_tarea, id_subtarea, id_proyecto, **kwargs):
    subtareas_por_tarea = cargar_subtareas()
    for entrada in subtareas_por_tarea['subtareas_por_tarea']:
        if entrada['id_proyecto'] == id_proyecto and entrada['id_tarea'] == id_tarea:
            for subtarea in entrada['subtareas']:
                if subtarea['id'] == id_subtarea:
                    subtarea.update(kwargs)
                    guardar_subtareas(subtareas_por_tarea)
                    return True
    return False

# Método para eliminar una subtarea de la tarea y guardar el cambio en el subtareas_file JSON
def eliminar_subtarea_y_guardar(id_tarea, id_subtarea, id_proyecto):
    subtareas_por_tarea = cargar_subtareas()
    for entrada in subtareas_por_tarea['subtareas_por_tarea']:
        if entrada['id_proyecto'] == id_proyecto and entrada['id_tarea'] == id_tarea:
            entrada['subtareas'] = [subtarea for subtarea in entrada['subtareas'] if subtarea['id'] != id_subtarea]
            guardar_subtareas(subtareas_por_tarea)
            return True
    return False