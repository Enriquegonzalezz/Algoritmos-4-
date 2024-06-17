# Módulo 1. Gestión de proyectos

import datetime
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
        
    # Método para representar un objeto Proyecto como una cadena de texto
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Fecha de Inicio: {self.fecha_inicio}, Fecha de Vencimiento: {self.fecha_vencimiento}, Estado: {self.estado}, Empresa: {self.empresa}, Gerente: {self.gerente}, Equipo: {', '.join(self.equipo)}"

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def agregar_tarea_al_final(self, tarea):
        self.tareas.append(tarea)

    def agregar_tarea_en_posicion(self, posicion, tarea):
        self.tareas.insert(posicion, tarea)


    def eliminar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                self.tareas.remove(tarea)
                return True
        return False

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

    def actualizar_tarea(self, id_tarea, **kwargs):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                for key, value in kwargs.items():
                    setattr(tarea, key, value)
                return True
        return False

    def listar_tareas(self):
        if self.tareas:
            for tarea in self.tareas:
                print(tarea)
        else:
            print("No hay tareas registradas para este proyecto.")

    def agregar_subtarea_a_tarea(self, id_tarea, subtarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                tarea.agregar_subtarea(subtarea)
                return True
        return False

    def eliminar_subtarea_de_tarea(self, id_tarea, id_subtarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                return tarea.eliminar_subtarea(id_subtarea)
        return False

    def actualizar_subtarea_en_tarea(self, id_tarea, id_subtarea, **kwargs):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                return tarea.actualizar_subtarea(id_subtarea, **kwargs)
        return False

    def listar_subtareas_de_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                return tarea.listar_subtareas()
        return []
    
class Subtarea:
    def __init__(self, id, nombre, descripcion, estado_actual, porcentaje):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Estado: {self.estado_actual}, Porcentaje: {self.porcentaje}%"


class Tarea:
    def __init__(self, id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje):
        self.id = id
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje
        self.subtareas = []

    def __str__(self):
        return f"Tarea {self.id}: {self.nombre}, Cliente: {self.empresa_cliente}, Estado: {self.estado_actual}, Completado: {self.porcentaje}%"

    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)

    def actualizar_subtarea(self, id_subtarea, **kwargs):
        for subtarea in self.subtareas:
            if subtarea.id == id_subtarea:
                for key, value in kwargs.items():
                    setattr(subtarea, key, value)
                return True
        return False
    
    def eliminar_subtarea(self, id_subtarea):
        for subtarea in self.subtareas:
            if subtarea.id == id_subtarea:
                self.subtareas.remove(subtarea)
                return True
        return False
    
    def listar_subtareas(self):
        if self.subtareas:
            for subtarea in self.subtareas:
                print(subtarea)
        else:
            print("No hay subtareas para esta tarea.")
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


    def agregar_tarea_a_proyecto(self, id_proyecto, tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                proyecto.agregar_tarea(tarea)
                return True
        return False
    
    def agregar_tarea_al_final_de_proyecto(self, id_proyecto, tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                proyecto.agregar_tarea_al_final(tarea)
                return True
        return False
    
    def agregar_tarea_en_posicion_de_proyecto(self, id_proyecto, posicion, tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                proyecto.agregar_tarea_en_posicion(posicion, tarea)
                return True
        return False
    
   
    def actualizar_tarea_en_proyecto(self, id_proyecto, id_tarea, **kwargs):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.actualizar_tarea(id_tarea, **kwargs)
        return False

    def eliminar_tarea_de_proyecto(self, id_proyecto, id_tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.eliminar_tarea(id_tarea)
            
    def buscar_tareas_por_nombre_en_proyecto(self, id_proyecto, nombre_tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return [tarea for tarea in proyecto.tareas if tarea.nombre.lower() == nombre_tarea.lower()]
        return []
    
    def listar_tareas_de_proyecto(self, id_proyecto):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                proyecto.listar_tareas()
                return True
        return False

    def proyecto_existe(self, id_proyecto):
        return any(proyecto.id == id_proyecto for proyecto in self.proyectos)
    
    def agregar_subtarea_a_tarea_en_proyecto(self, id_proyecto, id_tarea, subtarea):
        if not self.proyecto_existe(id_proyecto):
            return False
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.agregar_subtarea_a_tarea(id_tarea, subtarea)
        return False

    def eliminar_subtarea_de_tarea_en_proyecto(self, id_proyecto, id_tarea, id_subtarea):
        if not self.proyecto_existe(id_proyecto):
            return False
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.eliminar_subtarea_de_tarea(id_tarea, id_subtarea)
        return False

    def actualizar_subtarea_en_tarea_en_proyecto(self, id_proyecto, id_tarea, id_subtarea, **kwargs):
        if not self.proyecto_existe(id_proyecto):
            return False
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                return proyecto.actualizar_subtarea_en_tarea(id_tarea, id_subtarea, **kwargs)
        return False
    
    def listar_subtareas_de_tarea_en_proyecto(self, id_proyecto, id_tarea):
        for proyecto in self.proyectos:
            if proyecto.id == id_proyecto:
                for tarea in proyecto.tareas:
                    if tarea.id == id_tarea:
                        return tarea.subtareas
        return []
# Función para mostrar el menú de opciones
def mostrar_menu():
    print("Menú de Opciones")
    print("1. Agregar Proyecto")
    print("2. Modificar Proyecto")
    print("3. Buscar Proyecto")
    print("4. Eliminar Proyecto")
    print("5. Listar Proyectos")
    print("6. Agregar Tarea al Proyecto")
    print("7. Listar Tareas de Proyecto")
    print("8. Eliminar Tarea del Proyecto")
    print("9. Agregar Tarea en Posición Específica del Proyecto")
    print("10. Buscar Tareas por Nombre en Proyecto")
    print("11. Actualizar Tarea en Proyecto")
    print("12. Agregar Subtarea a Tarea")
    print("13. Listar Subtareas de Tarea")
    print("14. Eliminar Subtarea de Tarea")
    print("15. Actualizar Subtarea de Tarea")
    print("16. Salir")

# Función principal
def main():
    gestor = GestorProyectos()
    
    # Menú de opciones
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

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

        elif opcion == '4':
            id = input("ID del proyecto a eliminar: ")
            if gestor.eliminar_proyecto(id):
                print("Proyecto eliminado exitosamente.")
            else:
                print("Proyecto no encontrado")

        elif opcion == '5':
            proyectos = gestor.listar_proyectos()
            if proyectos:
                for proyecto in proyectos:
                    print(proyecto)
            else:
                print("")
                print("No hay proyectos registrados.")

        elif opcion == '6':
            # Agregar tarea al final del proyecto
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


        elif opcion == '7':
            id_proyecto = input("ID del proyecto: ")
            if not gestor.listar_tareas_de_proyecto(id_proyecto):
                print("No se encontró el proyecto.")
            else:
                continue
            

        elif opcion == '8':
            id_proyecto = input("ID del proyecto: ")
            id_tarea = input("ID de la tarea a eliminar: ")
            if gestor.eliminar_tarea_de_proyecto(id_proyecto, id_tarea):
                print("Tarea eliminada exitosamente.")
            else:
                print("No se encontró el proyecto o la tarea.")

        elif opcion == '9':
            # Agregar tarea en posición específica del proyecto
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

        elif opcion == '10':
            # Buscar tareas por nombre en un proyecto
            id_proyecto = input("ID del proyecto: ")
            nombre_tarea = input("Nombre de la tarea: ")
            tareas_encontradas = gestor.buscar_tareas_por_nombre_en_proyecto(id_proyecto, nombre_tarea)
            if tareas_encontradas:
                for tarea in tareas_encontradas:
                    print(tarea)
            else:
                print("No se encontraron tareas con ese nombre en el proyecto.")

        elif opcion == '11':
    # Actualizar tarea en un proyecto
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

        elif opcion == '16':
            # Salir del programa
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


            
if __name__ == "__main__":
    main()