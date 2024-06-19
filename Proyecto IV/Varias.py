from datetime import datetime

# Función para mostrar el menú de opciones
def mostrar_menu():
    opciones = ["Agregar Proyecto", "Modificar Proyecto", "Buscar Proyecto", "Eliminar Proyecto",
        "Listar Proyectos", "Listar Proyectos por Filtro", "Agregar Tarea al Proyecto", "Listar Tareas de Proyecto",
        "Listar Tareas de Proyecto por Estado", "Listar Tareas de Proyecto por Fecha",
        "Eliminar Tarea del Proyecto", "Agregar Tarea en Posición Específica del Proyecto", "Buscar Tareas por Nombre en Proyecto",
        "Actualizar Tarea en Proyecto", "Agregar Subtarea a Tarea", "Listar Subtareas de Tarea", "Listar Subtareas de Tarea y las Tareas", "Eliminar Subtarea de Tarea",
        "Actualizar Subtarea de Tarea", "Agregar Tarea Prioritaria", "Eliminar Tarea Prioritaria de la Cima",
        "Consultar Tarea Prioritaria en la Cima", "Consultar Tiempo de las Tareas Prioritarias", "Salir"
    ]
    print("Menú de Opciones")
    for opcion in opciones:
        print(f"{opciones.index(opcion) + 1}. {opcion}")

    return opciones

def es_fecha(fecha):
    try:
        datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except:
        return False

def comprobar_fecha(fecha):
    if es_fecha(fecha):
        return fecha
    else:
        return comprobar_fecha(input("Fecha en el formato incorrecto por favor ingresela en el formato(YYYY-MM-DD): ")) 
    
def tarea_a_diccionario(tarea):
    return {
        "id": tarea.id,
        "nombre": tarea.nombre,
        "empresa_cliente": tarea.empresa_cliente,
        "descripcion": tarea.descripcion,
        "fecha_inicio": tarea.fecha_inicio,
        "fecha_vencimiento": tarea.fecha_vencimiento,
        "estado_actual": tarea.estado_actual,
        "porcentaje": tarea.porcentaje
    }

def proyecto_a_diccionario(proyecto):
    return {
        "id": proyecto.id,
        "nombre": proyecto.nombre,
        "descripcion": proyecto.descripcion,
        "fecha_inicio": proyecto.fecha_inicio,
        "fecha_vencimiento": proyecto.fecha_vencimiento,
        "estado": proyecto.estado,
        "empresa": proyecto.empresa,
        "gerente": proyecto.gerente,
        "equipo": proyecto.equipo
    }

def verificar_convertir(fecha):
    if type(fecha) != datetime:
        try:
            return datetime.strptime(fecha, '%Y-%m-%d')
        except:
            return datetime.strptime(fecha[:-9], '%Y-%m-%d')