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