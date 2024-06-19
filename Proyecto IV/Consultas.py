from datetime import datetime

def listar_tareas_estado(tareas, estado_filtro):
    if len(tareas) > 0:
        for tarea in tareas:
            if tarea.estado_actual == estado_filtro:
                print(tarea)
    else:
        print("No hay tareas registradas para este proyecto.")

def listar_tareas_fecha(tareas, fecha_inicio = True, rango_fechas = None, fecha_despues = None, fecha_antes = None):
    if len(tareas) > 0:
        for tarea in tareas:
            if rango_fechas:
                if fecha_inicio:
                    if rango_fechas[0] <= tarea.fecha_inicio <= rango_fechas[1]:
                        print(tarea)
                else:
                    if rango_fechas[0] <= tarea.fecha_vencimiento <= rango_fechas[1]:
                        print(tarea)
            elif fecha_despues:
                if fecha_inicio:
                    if tarea.fecha_inicio >= fecha_despues:
                        print(tarea)
                else:
                    if tarea.fecha_vencimiento >= fecha_despues:
                        print(tarea)
            elif fecha_antes:
                if fecha_inicio:
                    if tarea.fecha_inicio <= fecha_antes:
                        print(tarea)
                else:
                    if tarea.fecha_vencimiento <= fecha_antes:
                        print(tarea)
    else:
        print("No hay tareas registradas para este proyecto.")

def calcular_porcentaje_finalizacion(tareas):
        tareas_completadas = sum(1 for tarea in tareas if tarea.estado_actual == 'Completado')
        total_tareas = len(tareas)
        return (tareas_completadas / total_tareas) * 100 if total_tareas > 0 else 0

# Método para calcular el tiempo restante aproximado para terminar el proyecto
def calcular_tiempo_restante(proyecto):
    fecha_venc = proyecto.fecha_vencimiento
    tiempo_restante = fecha_venc - datetime.now()
    return tiempo_restante.days if tiempo_restante.days > 0 else 0

# Método para filtrar y mostrar proyectos
def filtrar_mostrar_proyectos(proyectos, fecha_inicio=None, fecha_vencimiento=None, estado=None, empresa=None):
    proyectos_filtrados = []
    for proyecto in proyectos:  # Asumiendo que 'proyectos' es una lista de instancias de Proyecto
        cumple_criterios = True
        if fecha_inicio and proyecto.fecha_inicio != fecha_inicio:
            cumple_criterios = False
        if fecha_vencimiento and proyecto.fecha_vencimiento != fecha_vencimiento:
            cumple_criterios = False
        if estado and proyecto.estado != estado:
            cumple_criterios = False
        if empresa and proyecto.empresa.lower() != empresa.lower():
            cumple_criterios = False
        if cumple_criterios:
            proyectos_filtrados.append(proyecto)
    
    for proyecto in proyectos_filtrados:
        print(proyecto)
        print(f"Porcentaje de finalización: {calcular_porcentaje_finalizacion(proyecto.tareas)}%")
        print(f"Tiempo restante aproximado: {calcular_tiempo_restante(proyecto)} días")
        print('-----------------------------------')

def listar_subtareas_tareas(subtareas, tarea):
    progreso = tarea.calcular_progreso()
    print(str(tarea))
    for subtarea in subtareas:
        print(f"  - {subtarea}")
    print(f"  - Progreso: {progreso}%")