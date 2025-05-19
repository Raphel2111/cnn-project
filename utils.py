import csv

# Información por tipo de material
info_material = {
    "plastic": {
        "desc": "El plástico es un material derivado del petróleo.",
        "recom": "Contenedor amarillo. Limpio y seco."
    },
    "metal": {
        "desc": "Incluye aluminio o acero, usado en latas.",
        "recom": "Contenedor amarillo. Aplasta para ahorrar espacio."
    },
    "glass": {
        "desc": "El vidrio es 100% reciclable sin pérdida de calidad.",
        "recom": "Contenedor verde. Quita tapas o líquidos."
    },
    "paper": {
        "desc": "Viene de árboles. Muy reciclable pero sensible a humedad.",
        "recom": "Contenedor azul. Sin restos de comida o líquidos."
    }
}


# Exportar historial a CSV
def exportar_a_csv(registros, ruta="export_detecciones.csv"):
    with open(ruta, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Clase", "Cantidad", "Fecha"])
        for fila in registros:
            writer.writerow(fila)
    return ruta


