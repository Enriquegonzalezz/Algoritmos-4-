from datetime import datetime

def listar_tareas_estado(tareas, estado_filtro):
    if tareas:
        for tarea in tareas:
            if tarea.estado_actual == estado_filtro:
                print(tarea)
    else:
        print("No hay tareas registradas para este proyecto.")

def listar_tareas_fecha(tareas, fecha_inicio = True, rango_fechas = None, fecha_despues = None, fecha_antes = None):
    if tareas:
        for tarea in tareas:
            if rango_fechas:
                if fecha_inicio:
                    if rango_fechas[0] <= tarea.fecha_inicio <= rango_fechas[1]:
                        print(tarea)
                else:
                    if rango_fechas[0] <= datetime.strptime(tarea.fecha_vencimiento,'%Y-%m-%d') <= rango_fechas[1]:
                        print(tarea)
            elif fecha_despues:
                if fecha_inicio:
                    if tarea.fecha_inicio >= fecha_despues:
                        print(tarea)
                else:
                    if datetime.strptime(tarea.fecha_vencimiento,'%Y-%m-%d') >= fecha_despues:
                        print(tarea)
            elif fecha_antes:
                if fecha_inicio:
                    if tarea.fecha_inicio <= fecha_antes:
                        print(tarea)
                else:
                    if datetime.strptime(tarea.fecha_vencimiento,'%Y-%m-%d') <= fecha_antes:
                        print(tarea)
    else:
        print("No hay tareas registradas para este proyecto.")