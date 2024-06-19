
import datetime
from Proyecto import Proyecto
from Subtarea import Subtarea
from Tarea import Tarea
from Gestion import GestorProyectos
from Varias import mostrar_menu, comprobar_fecha
from Almacenamiento import (agregar_proyecto, actualizar_proyecto, eliminar_proyecto, agregar_subtarea_y_guardar,
    modificar_subtarea_y_guardar, eliminar_subtarea_y_guardar
)
from Consultas import *

# Función principal
def main():
    gestor = GestorProyectos()
    
    # Menú de opciones
    while True:
        opciones = mostrar_menu()
        eleccion = input("Seleccione una opción: ")

        # Agregar Proyecto 
        if opciones.index("Agregar Proyecto") + 1 == int(eleccion):
            id = input("ID: ")
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            fecha_inicio = comprobar_fecha(input("Fecha de Inicio (YYYY-MM-DD): "))
            fecha_vencimiento = comprobar_fecha(input("Fecha de Vencimiento (YYYY-MM-DD): "))
            estado = input("Estado: ")
            empresa = input("Empresa: ")
            gerente = input("Gerente: ")
            equipo = input("Equipo (separado por comas): ").split(",")

            nuevo_proyecto = Proyecto(id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo)
            gestor.agregar_proyecto(nuevo_proyecto)
            agregar_proyecto(nuevo_proyecto)
            print("")
            print("Proyecto agregado exitosamente.")

        # Modificar Proyecto
        elif opciones.index("Modificar Proyecto") + 1 == int(eleccion):
            id = input("ID del proyecto a modificar: ")
            print("Ingrese los nuevos datos del proyecto (deje en blanco para no modificar):")
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            fecha_inicio = comprobar_fecha(input("Fecha de Inicio (YYYY-MM-DD): "))
            fecha_vencimiento = comprobar_fecha(input("Fecha de Vencimiento (YYYY-MM-DD): "))
            estado = input("Estado: ")
            empresa = input("Empresa: ")
            gerente = input("Gerente: ")
            equipo = input("Equipo (separado por comas): ")

            kwargs = {}
            if nombre:
                kwargs['nombre'] = nombre
            if descripcion:
                kwargs['descripcion'] = descripcion
            if fecha_inicio:
                kwargs['fecha_inicio'] = fecha_inicio
            if fecha_vencimiento:
                kwargs['fecha_vencimiento'] = fecha_vencimiento
            if estado:
                kwargs['estado'] = estado
            if empresa:
                kwargs['empresa'] = empresa
            if gerente:
                kwargs['gerente'] = gerente
            if equipo:
                kwargs['equipo'] = equipo.split(",")

            if gestor.modificar_proyecto(id, **kwargs):
                actualizar_proyecto(gestor.obtener_proyecto(id))
                print("")
                print("Proyecto modificado exitosamente.")
            else:
                print("")
                print("Proyecto no encontrado.")

        # Buscar Proyecto
        elif opciones.index("Buscar Proyecto") + 1 == int(eleccion):
            print("Criterios de búsqueda disponibles: id, nombre, empresa, gerente")
            criterio = input("Buscar por: ").lower()
            valor = input("Valor: ")

            proyectos = gestor.buscar_proyecto(criterio, valor)
            if proyectos:
                for proyecto in proyectos:
                    print(proyecto)
            else:
                print("")
                print("Proyecto no encontrado.")

        # Eliminar Proyecto
        elif opciones.index("Eliminar Proyecto") + 1 == int(eleccion):
            id = input("ID del proyecto a eliminar: ")
            if gestor.eliminar_proyecto(id):
                eliminar_proyecto(id)
                print("Proyecto eliminado exitosamente.")
            else:
                print("Proyecto no encontrado")

        # Listar Proyectos
        elif opciones.index("Listar Proyectos") + 1 == int(eleccion):
            proyectos = gestor.listar_proyectos()
            if proyectos:
                for proyecto in proyectos:
                    print(proyecto)
            else:
                print("")
                print("No hay proyectos registrados.")

        # Listar Proyectos por Filtro
        elif opciones.index("Listar Proyectos por Filtro") + 1 == int(eleccion):
            proyectos = gestor.listar_proyectos()
            if not proyectos:
                print("")
                print("No hay proyectos registrados.")
            else:
                print("Opciones de filtro:")
                print("1. Por fecha")
                print("2. Por nombre de empresa")
                print("3. Por estatus")
                filtro = input("Eleccion: ")
                if filtro == "1":
                    print("Opciones de fecha:")
                    print("1. Fecha de Inicio")
                    print("2. Fecha de Vencimiento")
                    eleccion = input("Eleccion: ")
                    fecha = comprobar_fecha(input("Fecha: "))
                    if eleccion == "1":
                        filtrar_mostrar_proyectos(proyectos, fecha_inicio=fecha)
                    else:
                        filtrar_mostrar_proyectos(proyectos, fecha_vencimiento=fecha)
                elif filtro == "2":
                    empresa = input("Nombre de empresa: ")
                    filtrar_mostrar_proyectos(proyectos, empresa=empresa)
                else:
                    estado = input("Estado: ")
                    filtrar_mostrar_proyectos(proyectos, estado=estado)
                continue

        # Agregar tarea al final del proyecto
        elif opciones.index("Agregar Tarea al Proyecto") + 1 == int(eleccion):
        
            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea: ")
            nombre_tarea = input("Nombre de la tarea: ")
            empresa_cliente = input("Empresa cliente: ")
            descripcion = input("Descripción: ")
            fecha_inicio = datetime.now().strftime('%Y-%m-%d')
            fecha_vencimiento = comprobar_fecha(input("Fecha de Vencimiento (YYYY-MM-DD): "))
            estado_actual = input("Estado actual: ")
            porcentaje = input("Porcentaje completado: ")

            nueva_tarea = Tarea(id_tarea, nombre_tarea, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje)
            if gestor.agregar_tarea_al_final_de_proyecto(id_proyecto, nueva_tarea):
                actualizar_proyecto(gestor.obtener_proyecto(id_proyecto))
                print("Tarea agregada al final del proyecto exitosamente.")
            else:
                print("No se encontró el proyecto.")

        # Listar Tareas de Proyecto
        elif opciones.index("Listar Tareas de Proyecto") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            if not gestor.listar_tareas_de_proyecto(id_proyecto):
                print("No se encontró el proyecto.")
            else:
                continue

        # Listar Tareas de Proyecto por Estado
        elif opciones.index("Listar Tareas de Proyecto por Estado") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            proyecto = gestor.obtener_proyecto(id_proyecto)
            if not proyecto:
                print("No se encontró el proyecto.")
            else:
                estado = input("Estado de la tarea: ")
                listar_tareas_estado(proyecto.tareas, estado)
                continue

        # Listar Tareas de Proyecto por Fecha
        elif opciones.index("Listar Tareas de Proyecto por Fecha") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            proyecto = gestor.obtener_proyecto(id_proyecto)
            if not proyecto:
                print("No se encontró el proyecto.")
            else:
                print("Opciones de fecha:")
                print("1. Fecha de Inicio")
                print("2. Fecha de Vencimiento")
                fecha = input("Eleccion: ")
                if fecha == "1":
                    fecha_inicio = True
                else:
                    fecha_inicio = False
                print("Opciones de filtro:")
                print("1. Rango de fechas")
                print("2. Despues de")
                print("3. Antes de")
                filtro = input("Eleccion: ")
                if filtro == "1":
                    despues = datetime.strptime(comprobar_fecha(input("Fecha despues de (YYYY-MM-DD): ")))
                    antes = datetime.strptime(comprobar_fecha(input("Fecha antes de (YYYY-MM-DD): "))) 
                    listar_tareas_fecha(proyecto.tareas, fecha_inicio, [despues, antes])
                else:
                    if filtro == "2":
                        despues = datetime.strptime(input("Fecha despues de (YYYY-MM-DD): "))
                        listar_tareas_fecha(proyecto.tareas, fecha_inicio, fecha_despues=despues)
                    else:
                        antes = datetime.strptime(input("Fecha antes de (YYYY-MM-DD): "))
                        listar_tareas_fecha(proyecto.tareas, fecha_inicio, fecha_antes=antes)
                continue
            
        # Eliminar Tarea del Proyecto
        elif opciones.index("Eliminar Tarea del Proyecto") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea a eliminar: ")
            if gestor.eliminar_tarea_de_proyecto(id_proyecto, id_tarea):
                actualizar_proyecto(gestor.obtener_proyecto(id_proyecto))
                print("Tarea eliminada exitosamente.")
            else:
                print("No se encontró el proyecto o la tarea.")

        # Agregar Tarea en Posición Específica del Proyecto
        elif opciones.index("Agregar Tarea en Posición Específica del Proyecto") + 1 == int(eleccion):
            
            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea: ")
            nombre_tarea = input("Nombre de la tarea: ")
            empresa_cliente = input("Empresa cliente: ")
            descripcion = input("Descripción: ")
            fecha_inicio = datetime.date.today()
            fecha_vencimiento = comprobar_fecha(input("Fecha de Vencimiento (YYYY-MM-DD): "))
            estado_actual = input("Estado actual: ")
            porcentaje = input("Porcentaje completado: ")
            posicion = int(input("Posición en la lista de tareas: "))

            nueva_tarea = Tarea(id_tarea, nombre_tarea, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje)
            if gestor.agregar_tarea_en_posicion_de_proyecto(id_proyecto, posicion, nueva_tarea):
                actualizar_proyecto(gestor.obtener_proyecto(id_proyecto))
                print(f"Tarea agregada en la posición {posicion} del proyecto exitosamente.")
            else:
                print("No se encontró el proyecto.")

        # Buscar Tareas por Nombre en Proyecto
        elif opciones.index("Buscar Tareas por Nombre en Proyecto") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            nombre_tarea = input("Nombre de la tarea: ")
            tareas_encontradas = gestor.buscar_tareas_por_nombre_en_proyecto(id_proyecto, nombre_tarea)
            if tareas_encontradas:
                for tarea in tareas_encontradas:
                    print(tarea)
            else:
                print("No se encontraron tareas con ese nombre en el proyecto.")

        # Actualizar Tarea en Proyecto
        elif opciones.index("Actualizar Tarea en Proyecto") + 1 == int(eleccion):

            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea a actualizar: ")
            proyecto = gestor.buscar_proyecto('id', id_proyecto)
            if proyecto:
                print("Ingrese los nuevos datos de la tarea (deje en blanco para mantener los valores actuales):")
                nombre_tarea = input("Nuevo nombre de la tarea: ")
                empresa_cliente = input("Nueva empresa cliente: ")
                descripcion = input("Nueva descripción: ")
                fecha_vencimiento = comprobar_fecha(input("Fecha de Vencimiento (YYYY-MM-DD): "))
                estado_actual = input("Nuevo estado actual: ")
                porcentaje = input("Nuevo porcentaje completado: ")

                kwargs = {
                    'nombre': nombre_tarea,
                    'empresa_cliente': empresa_cliente,
                    'descripcion': descripcion,
                    'fecha_vencimiento': fecha_vencimiento,
                    'estado_actual': estado_actual,
                    'porcentaje': porcentaje
                }
                
                if gestor.actualizar_tarea_en_proyecto(id_proyecto, id_tarea, **kwargs):
                    actualizar_proyecto(gestor.obtener_proyecto(id_proyecto))
                    print("Tarea actualizada exitosamente.")
                else:
                    print("No se pudo actualizar la tarea.")
            else:
                print("No se encontró el proyecto.")

        # Agregar Subtarea a Tarea
        elif opciones.index("Agregar Subtarea a Tarea") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            if not gestor.proyecto_existe(id_proyecto):
                print("No se encontró el proyecto.")
                continue

            id_tarea = input("ID de la tarea: ")
            id_subtarea = input("ID de la subtarea: ")
            nombre_subtarea = input("Nombre de la subtarea: ")
            descripcion = input("Descripción: ")
            estado_actual = input("Estado actual: ")
            porcentaje = input("Porcentaje completado: ")

            nueva_subtarea = Subtarea(id_subtarea, nombre_subtarea, descripcion, estado_actual, porcentaje)
            if gestor.agregar_subtarea_a_tarea_en_proyecto(id_proyecto, id_tarea, nueva_subtarea):
                agregar_subtarea_y_guardar(id_tarea, nueva_subtarea, id_proyecto)
                print("Subtarea agregada exitosamente.")
            else:
                print("No se encontró el proyecto o la tarea.")

        # Listar Subtareas de Tarea
        elif opciones.index("Listar Subtareas de Tarea") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            if not gestor.proyecto_existe(id_proyecto):
                print("No se encontró el proyecto.")
                continue

            id_tarea = input("ID de la tarea: ")
            subtareas = gestor.listar_subtareas_de_tarea_en_proyecto(id_proyecto, id_tarea)
            if subtareas:
                for subtarea in subtareas:
                    print(subtarea)
            else:
                print("No se encontraron subtareas para la tarea especificada.")
        
        # Listar Subtareas de Tarea y las Tareas
        elif opciones.index("Listar Subtareas de Tarea y las Tareas") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            if not gestor.proyecto_existe(id_proyecto):
                print("No se encontró el proyecto.")
                continue

            for tarea in proyectos.tareas:
                subtareas = gestor.listar_subtareas_de_tarea_en_proyecto(id_proyecto, tarea.id)
                if subtareas:
                    listar_subtareas_tareas(subtareas, tarea)
                else:
                    print("No se encontraron subtareas para la tarea {0}.".format(tarea.id))

        # Eliminar Subtarea de Tarea
        elif opciones.index("Eliminar Subtarea de Tarea") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            if not gestor.proyecto_existe(id_proyecto):
                print("No se encontró el proyecto.")
                continue

            id_tarea = input("ID de la tarea: ")
            id_subtarea = input("ID de la subtarea a eliminar: ")
            if gestor.eliminar_subtarea_de_tarea_en_proyecto(id_proyecto, id_tarea, id_subtarea):
                eliminar_subtarea_y_guardar(id_tarea, id_subtarea, id_proyecto)
                print("Subtarea eliminada exitosamente.")
            else:
                print("No se encontró el proyecto, la tarea o la subtarea.")    

        # Actualizar Subtarea de Tarea
        elif opciones.index("Actualizar Subtarea de Tarea") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            if not gestor.proyecto_existe(id_proyecto):
                print("No se encontró el proyecto.")
                continue

            id_tarea = input("ID de la tarea: ")
            id_subtarea = input("ID de la subtarea a actualizar: ")
            print("Ingrese los nuevos datos de la subtarea (deje en blanco para mantener los valores actuales):")
            nombre_subtarea = input("Nuevo nombre de la subtarea: ")
            descripcion = input("Nueva descripción: ")
            estado_actual = input("Nuevo estado actual: ")
            porcentaje = input("Nuevo porcentaje completado: ")

            kwargs = {
                'nombre': nombre_subtarea,
                'descripcion': descripcion,
                'estado_actual': estado_actual,
                'porcentaje': porcentaje
            }

            if gestor.actualizar_subtarea_en_tarea_en_proyecto(id_proyecto, id_tarea, id_subtarea, **kwargs):
                modificar_subtarea_y_guardar(id_tarea, id_subtarea, id_proyecto, **kwargs)
                print("Subtarea actualizada exitosamente.")
            else:
                print("No se pudo actualizar la subtarea o no se encontró el proyecto, la tarea o la subtarea.")

        # Agregar Tarea Prioritaria
        elif opciones.index("Agregar Tarea Prioritaria") + 1 == int(eleccion):
            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea prioritaria: ")
            nombre_tarea = input("Nombre de la tarea prioritaria: ")
            empresa_cliente = input("Empresa cliente: ")
            descripcion = input("Descripción: ")
            fecha_inicio = datetime.date.today()
            fecha_vencimiento = comprobar_fecha(input("Fecha de Vencimiento (YYYY-MM-DD): "))
            estado_actual = input("Estado actual: ")
            porcentaje = input("Porcentaje completado: ")

            nueva_tarea = Tarea(id_tarea, nombre_tarea, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje)
            if gestor.agregar_tarea_prioritaria_a_proyecto(id_proyecto, nueva_tarea):
                actualizar_proyecto(gestor.obtener_proyecto(id_proyecto))
                print("Tarea prioritaria agregada al proyecto exitosamente.")
            else:
                print("No se encontró el proyecto.")

        # Eliminar Tarea Prioritaria de la Cima del proyecto
        elif opciones.index("Eliminar Tarea Prioritaria de la Cima") + 1 == int(eleccion):

            id_proyecto = input("ID del proyecto: ")
            tarea_prioritaria_eliminada = gestor.eliminar_tarea_prioritaria_de_proyecto(id_proyecto)
            if tarea_prioritaria_eliminada:
                actualizar_proyecto(gestor.obtener_proyecto(id_proyecto))
                print(f"Tarea prioritaria eliminada del proyecto: {tarea_prioritaria_eliminada.nombre}")
            else:
                print("No se encontró el proyecto o no hay tareas prioritarias.")

        # Consultar Tarea Prioritaria en la Cima
        elif opciones.index("Consultar Tarea Prioritaria en la Cima") + 1 == int(eleccion):

            id_proyecto = input("ID del proyecto: ")
            tarea_prioritaria = gestor.consultar_tarea_prioritaria_de_proyecto(id_proyecto)
            if tarea_prioritaria:
                print(f"Tarea prioritaria del proyecto: {tarea_prioritaria}")
            else:
                print("No se encontró el proyecto o no hay tareas prioritarias.")

        elif opciones.index("Consultar Tiempo de las Tareas Prioritarias") + 1 == int(eleccion):

            id_proyecto = input("ID del proyecto: ")
            tiempo = gestor.consultar_tiempo_tareas_prioritarias(id_proyecto)
            if tiempo:
                print(f"Tiempo de las Tareas prioritarias del proyecto: {tiempo}")
            else:
                print("No se encontró el proyecto o no hay tareas prioritarias.")

        # Salir del programa
        elif opciones.index("Salir") + 1 == int(eleccion):
            # Salir del programa
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        
if __name__ == "__main__":
    main()