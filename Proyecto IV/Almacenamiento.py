import json

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
def guardar_proyectos(proyectos, ):
    with open(proyectos_file, 'w') as file:
        json.dump(proyectos, file, indent=4)

# Método para agregar un proyecto al proyectos_file JSON
def agregar_proyecto(proyecto, ):
    proyectos = cargar_proyectos(proyectos_file)
    proyectos['proyectos'].append(proyecto.__dict__)
    guardar_proyectos(proyectos, proyectos_file)

# Método para actualizar un proyecto en el proyectos_file JSON
def actualizar_proyecto(proyecto, ):
    proyectos = cargar_proyectos(proyectos_file)
    for proyecto in proyectos['proyectos']:
        if proyecto['id'] == proyecto.id:
            proyecto.update(proyecto.__dict__)
    guardar_proyectos(proyectos, proyectos_file)

# Método para eliminar un proyecto del proyectos_file JSON
def eliminar_proyecto(id_proyecto, ):
    proyectos = cargar_proyectos(proyectos_file)
    proyectos['proyectos'] = [proyecto for proyecto in proyectos['proyectos'] if proyecto['id'] != id_proyecto]
    guardar_proyectos(proyectos, proyectos_file)

# Método para cargar las subtareas desde un proyectos_file JSON
def cargar_subtareas():
    with open(subtareas_file, 'r') as file:
        return json.load(file)

# Método para guardar las subtareas en un subtareas_file JSON
def guardar_subtareas(subtareas_por_tarea, ):
    with open(subtareas_file, 'w') as file:
        json.dump(subtareas_por_tarea, file, indent=4)

# Método para agregar una subtarea a la tarea y guardar el cambio en el subtareas_file JSON
def agregar_subtarea_y_guardar(id_tarea, subtarea, id_proyecto):
    subtareas_por_tarea = cargar_subtareas(subtareas_file)
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
    guardar_subtareas(subtareas_por_tarea, subtareas_file)

# Método para modificar una subtarea existente y guardar el cambio en el subtareas_file JSON
def modificar_subtarea_y_guardar(id_tarea, id_subtarea, id_proyecto, **kwargs):
    subtareas_por_tarea = cargar_subtareas(subtareas_file)
    for entrada in subtareas_por_tarea['subtareas_por_tarea']:
        if entrada['id_proyecto'] == id_proyecto and entrada['id_tarea'] == id_tarea:
            for subtarea in entrada['subtareas']:
                if subtarea['id_subtarea'] == id_subtarea:
                    subtarea.update(kwargs)
                    guardar_subtareas(subtareas_por_tarea, subtareas_file)
                    return True
    return False

# Método para eliminar una subtarea de la tarea y guardar el cambio en el subtareas_file JSON
def eliminar_subtarea_y_guardar(id_tarea, id_subtarea, id_proyecto):
    subtareas_por_tarea = cargar_subtareas(subtareas_file)
    for entrada in subtareas_por_tarea['subtareas_por_tarea']:
        if entrada['id_proyecto'] == id_proyecto and entrada['id_tarea'] == id_tarea:
            entrada['subtareas'] = [subtarea for subtarea in entrada['subtareas'] if subtarea['id_subtarea'] != id_subtarea]
            guardar_subtareas(subtareas_por_tarea, subtareas_file)
            return True
    return False