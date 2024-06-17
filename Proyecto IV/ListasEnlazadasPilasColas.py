
import datetime
from Proyecto import Proyecto
from Subtarea import Subtarea
from Tarea import Tarea
from Gestion import GestorProyectos
from Varias import mostrar_menu

# Función principal
def main():
    gestor = GestorProyectos()
    
    # Menú de opciones
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # Agregar Proyecto 
        if opcion == '1':
            id = input("ID: ")
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            fecha_inicio = input("Fecha de Inicio (YYYY-MM-DD): ")
            fecha_vencimiento = input("Fecha de Vencimiento (YYYY-MM-DD): ")
            estado = input("Estado: ")
            empresa = input("Empresa: ")
            gerente = input("Gerente: ")
            equipo = input("Equipo (separado por comas): ").split(",")

            nuevo_proyecto = Proyecto(id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo)
            gestor.agregar_proyecto(nuevo_proyecto)
            print("")
            print("Proyecto agregado exitosamente.")

        # Modificar Proyecto
        elif opcion == '2':
            id = input("ID del proyecto a modificar: ")
            print("Ingrese los nuevos datos del proyecto (deje en blanco para no modificar):")
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            fecha_inicio = input("Fecha de Inicio (YYYY-MM-DD): ")
            fecha_vencimiento = input("Fecha de Vencimiento (YYYY-MM-DD): ")
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
                print("")
                print("Proyecto modificado exitosamente.")
            else:
                print("")
                print("Proyecto no encontrado.")

        # Buscar Proyecto
        elif opcion == '3':
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
        elif opcion == '4':
            id = input("ID del proyecto a eliminar: ")
            if gestor.eliminar_proyecto(id):
                print("Proyecto eliminado exitosamente.")
            else:
                print("Proyecto no encontrado")

        # Listar Proyectos
        elif opcion == '5':
            proyectos = gestor.listar_proyectos()
            if proyectos:
                for proyecto in proyectos:
                    print(proyecto)
            else:
                print("")
                print("No hay proyectos registrados.")

        # Agregar tarea al final del proyecto
        elif opcion == '6':
        
            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea: ")
            nombre_tarea = input("Nombre de la tarea: ")
            empresa_cliente = input("Empresa cliente: ")
            descripcion = input("Descripción: ")
            fecha_inicio = datetime.date.today()
            fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
            estado_actual = input("Estado actual: ")
            porcentaje = input("Porcentaje completado: ")

            nueva_tarea = Tarea(id_tarea, nombre_tarea, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje)
            if gestor.agregar_tarea_al_final_de_proyecto(id_proyecto, nueva_tarea):
                print("Tarea agregada al final del proyecto exitosamente.")
            else:
                print("No se encontró el proyecto.")

        # Listar Tareas de Proyecto
        elif opcion == '7':
            id_proyecto = input("ID del proyecto: ")
            if not gestor.listar_tareas_de_proyecto(id_proyecto):
                print("No se encontró el proyecto.")
            else:
                continue
            
        # Eliminar Tarea del Proyecto
        elif opcion == '8':
            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea a eliminar: ")
            if gestor.eliminar_tarea_de_proyecto(id_proyecto, id_tarea):
                print("Tarea eliminada exitosamente.")
            else:
                print("No se encontró el proyecto o la tarea.")

        # Agregar Tarea en Posición Específica del Proyecto
        elif opcion == '9':
            
            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea: ")
            nombre_tarea = input("Nombre de la tarea: ")
            empresa_cliente = input("Empresa cliente: ")
            descripcion = input("Descripción: ")
            fecha_inicio = datetime.date.today()
            fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
            estado_actual = input("Estado actual: ")
            porcentaje = input("Porcentaje completado: ")
            posicion = int(input("Posición en la lista de tareas: "))

            nueva_tarea = Tarea(id_tarea, nombre_tarea, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje)
            if gestor.agregar_tarea_en_posicion_de_proyecto(id_proyecto, posicion, nueva_tarea):
                print(f"Tarea agregada en la posición {posicion} del proyecto exitosamente.")
            else:
                print("No se encontró el proyecto.")

        # Buscar Tareas por Nombre en Proyecto
        elif opcion == '10':
            id_proyecto = input("ID del proyecto: ")
            nombre_tarea = input("Nombre de la tarea: ")
            tareas_encontradas = gestor.buscar_tareas_por_nombre_en_proyecto(id_proyecto, nombre_tarea)
            if tareas_encontradas:
                for tarea in tareas_encontradas:
                    print(tarea)
            else:
                print("No se encontraron tareas con ese nombre en el proyecto.")

        # Actualizar Tarea en Proyecto
        elif opcion == '11':

            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea a actualizar: ")
            proyecto = gestor.buscar_proyecto('id', id_proyecto)
            if proyecto:
                print("Ingrese los nuevos datos de la tarea (deje en blanco para mantener los valores actuales):")
                nombre_tarea = input("Nuevo nombre de la tarea: ")
                empresa_cliente = input("Nueva empresa cliente: ")
                descripcion = input("Nueva descripción: ")
                fecha_vencimiento = input("Nueva fecha de vencimiento: ")
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
                    print("Tarea actualizada exitosamente.")
                else:
                    print("No se pudo actualizar la tarea.")
            else:
                print("No se encontró el proyecto.")

        # Agregar Subtarea a Tarea
        elif opcion == '12':
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
                print("Subtarea agregada exitosamente.")
            else:
                print("No se encontró el proyecto o la tarea.")

        # Listar Subtareas de Tarea
        elif opcion == '13':
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

        # Eliminar Subtarea de Tarea
        elif opcion == '14':
            id_proyecto = input("ID del proyecto: ")
            if not gestor.proyecto_existe(id_proyecto):
                print("No se encontró el proyecto.")
                continue

            id_tarea = input("ID de la tarea: ")
            id_subtarea = input("ID de la subtarea a eliminar: ")
            if gestor.eliminar_subtarea_de_tarea_en_proyecto(id_proyecto, id_tarea, id_subtarea):
                print("Subtarea eliminada exitosamente.")
            else:
                print("No se encontró el proyecto, la tarea o la subtarea.")    

        # Actualizar Subtarea de Tarea
        elif opcion == '15':
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
                print("Subtarea actualizada exitosamente.")
            else:
                print("No se pudo actualizar la subtarea o no se encontró el proyecto, la tarea o la subtarea.")

        # Agregar Tarea Prioritaria
        elif opcion == '16':
            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea prioritaria: ")
            nombre_tarea = input("Nombre de la tarea prioritaria: ")
            empresa_cliente = input("Empresa cliente: ")
            descripcion = input("Descripción: ")
            fecha_inicio = datetime.date.today()
            fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
            estado_actual = input("Estado actual: ")
            porcentaje = input("Porcentaje completado: ")

            nueva_tarea = Tarea(id_tarea, nombre_tarea, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje)
            if gestor.agregar_tarea_prioritaria_a_proyecto(id_proyecto, nueva_tarea):
                print("Tarea prioritaria agregada al proyecto exitosamente.")
            else:
                print("No se encontró el proyecto.")

        # Eliminar Tarea Prioritaria de la Cima del proyecto
        elif opcion == '17':

            id_proyecto = input("ID del proyecto: ")
            tarea_prioritaria_eliminada = gestor.eliminar_tarea_prioritaria_de_proyecto(id_proyecto)
            if tarea_prioritaria_eliminada:
                print(f"Tarea prioritaria eliminada del proyecto: {tarea_prioritaria_eliminada.nombre}")
            else:
                print("No se encontró el proyecto o no hay tareas prioritarias.")

        # Consultar Tarea Prioritaria en la Cima
        elif opcion == '18':

            id_proyecto = input("ID del proyecto: ")
            tarea_prioritaria = gestor.consultar_tarea_prioritaria_de_proyecto(id_proyecto)
            if tarea_prioritaria:
                print(f"Tarea prioritaria del proyecto: {tarea_prioritaria}")
            else:
                print("No se encontró el proyecto o no hay tareas prioritarias.")

        # Salir del programa
        elif opcion == '20':
            # Salir del programa
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


            
if __name__ == "__main__":
    main()