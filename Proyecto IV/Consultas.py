def listar_tareas_estado(tareas, estado_filtro):
    if tareas:
        for tarea in tareas:
            if tarea.estado_actual == estado_filtro:
                print(tarea)
    else:
        print("No hay tareas registradas para este proyecto.")