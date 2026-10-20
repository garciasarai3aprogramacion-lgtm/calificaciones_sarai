from nicegui import ui

datos = []

columnas = [
    {"name": "nombre", "label": "Alumno", "field": "nombre"},
    {"name": "calificacion", "label": "Calificación", "field": "calificacion"},
]

def actualizar_grafica():
    nombres = [d["nombre"] for d in datos]
    calificaciones = [d["calificacion"] for d in datos]

    grafica.options["xAxis"]["data"] = nombres
    grafica.options["series"][0]["data"] = calificaciones
    grafica.update()

def registrar():
    if not nombre.value or calificacion.value is None:
        ui.notify("Completa todos los campos")
        return

    datos.append({
        "nombre": nombre.value,
        "calificacion": calificacion.value
    })

    tabla.rows = datos
    tabla.update()
    actualizar_grafica()
    ui.notify("Alumno registrado")

    nombre.value = ""
    calificacion.value = None

with ui.column().classes("w-full items-center"):
    ui.label("Registro de Calificaciones").style(
        "font-size: 28px; font-weight: bold"
    )

    nombre = ui.input("Nombre del alumno").style("width: 320px")
    calificacion = ui.number("Calificación").style("width: 320px")

    ui.button("Registrar", on_click=registrar)

    tabla = ui.table(columns=columnas, rows=datos).style("width: 520px")

    grafica = ui.echart({
        "xAxis": {"type": "category", "data": []},
        "yAxis": {"type": "value"},
        "series": [{
            "type": "bar",
            "data": []
        }]
    }).style("width: 520px; height: 320px")

ui.run