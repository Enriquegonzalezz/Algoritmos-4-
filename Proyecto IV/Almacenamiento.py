import json

def cargar_proyectos(archivo='proyectos.json'):
    with open(archivo, 'r') as file:
        return json.load(file)

# Método para guardar los proyectos en un archivo JSON
def guardar_proyectos(proyectos, archivo='proyectos.json'):
    with open(archivo, 'w') as file:
        json.dump(proyectos, file, indent=4)

# Método para agregar un proyecto al archivo JSON
def agregar_proyecto(proyecto, archivo='proyectos.json'):
    proyectos = cargar_proyectos(archivo)
    proyectos['proyectos'].append(proyecto.__dict__)
    guardar_proyectos(proyectos, archivo)

# Método para actualizar un proyecto en el archivo JSON
def actualizar_proyecto(proyecto, archivo='proyectos.json'):
    proyectos = cargar_proyectos(archivo)
    for proyecto in proyectos['proyectos']:
        if proyecto['id'] == proyecto.id:
            proyecto.update(proyecto.__dict__)
    guardar_proyectos(proyectos, archivo)

# Método para eliminar un proyecto del archivo JSON
def eliminar_proyecto(id_proyecto, archivo='proyectos.json'):
    proyectos = cargar_proyectos(archivo)
    proyectos['proyectos'] = [proyecto for proyecto in proyectos['proyectos'] if proyecto['id'] != id_proyecto]
    guardar_proyectos(proyectos, archivo)

def agregar_tarea_y_guardar(proyecto, tarea, archivo='proyectos.json'):
    proyecto.agregar_tarea(tarea)
    actualizar_proyecto(proyecto, archivo)

# Método para modificar una tarea existente y guardar el cambio en el archivo JSON
def modificar_tarea_y_guardar(proyecto, id_tarea, archivo='proyectos.json', **kwargs):
    if proyecto.actualizar_tarea(id_tarea, **kwargs):
        actualizar_proyecto(proyecto, archivo)
        return True
    return False

# Método para eliminar una tarea del proyecto y guardar el cambio en el archivo JSON
def eliminar_tarea_y_guardar(proyecto, id_tarea, archivo='proyectos.json'):
    if proyecto.eliminar_tarea(id_tarea):
        actualizar_proyecto(proyecto, archivo)
        return True
    return False

# Método para cargar las subtareas desde un archivo JSON
def cargar_subtareas(archivo='subtareas.json'):
    with open(archivo, 'r') as file:
        return json.load(file)

# Método para guardar las subtareas en un archivo JSON
def guardar_subtareas(subtareas_por_tarea, archivo='subtareas.json'):
    with open(archivo, 'w') as file:
        json.dump(subtareas_por_tarea, file, indent=4)

# Método para agregar una subtarea a la tarea y guardar el cambio en el archivo JSON
def agregar_subtarea_y_guardar(tarea, subtarea, id_proyecto, archivo='subtareas.json'):
    tarea.agregar_subtarea(subtarea)
    subtareas_por_tarea = cargar_subtareas(archivo)
    for entrada in subtareas_por_tarea['subtareas_por_tarea']:
        if entrada['id_proyecto'] == id_proyecto and entrada['id_tarea'] == tarea.id:
            entrada['subtareas'].append(subtarea.__dict__)
            break
    else:
        subtareas_por_tarea['subtareas_por_tarea'].append({
            "id_proyecto": id_proyecto,
            "id_tarea": tarea.id,
            "subtareas": [subtarea.__dict__]
        })
    guardar_subtareas(subtareas_por_tarea, archivo)

# Método para modificar una subtarea existente y guardar el cambio en el archivo JSON
def modificar_subtarea_y_guardar(tarea, id_subtarea, id_proyecto, archivo='subtareas.json', **kwargs):
    if tarea.actualizar_subtarea(id_subtarea, **kwargs):
        subtareas_por_tarea = cargar_subtareas(archivo)
        for entrada in subtareas_por_tarea['subtareas_por_tarea']:
            if entrada['id_proyecto'] == id_proyecto and entrada['id_tarea'] == tarea.id:
                for subtarea in entrada['subtareas']:
                    if subtarea['id_subtarea'] == id_subtarea:
                        subtarea.update(kwargs)
                        guardar_subtareas(subtareas_por_tarea, archivo)
                        return True
    return False

# Método para eliminar una subtarea de la tarea y guardar el cambio en el archivo JSON
def eliminar_subtarea_y_guardar(tarea, id_subtarea, id_proyecto, archivo='subtareas.json'):
    if tarea.eliminar_subtarea(id_subtarea):
        subtareas_por_tarea = cargar_subtareas(archivo)
        for entrada in subtareas_por_tarea['subtareas_por_tarea']:
            if entrada['id_proyecto'] == id_proyecto and entrada['id_tarea'] == tarea.id:
                entrada['subtareas'] = [subtarea for subtarea in entrada['subtareas'] if subtarea['id_subtarea'] != id_subtarea]
                guardar_subtareas(subtareas_por_tarea, archivo)
                return True
    return False