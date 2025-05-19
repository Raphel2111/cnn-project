import sqlite3
from datetime import datetime

# Conexión global
conn = sqlite3.connect("detecciones.db", check_same_thread=False)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS residuos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    clase TEXT,
    cantidad INTEGER,
    fecha TEXT
)
""")
conn.commit()


def guardar_deteccion(nombre, counts):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for clase, cantidad in counts.items():
        cursor.execute(
            "INSERT INTO residuos (nombre, clase, cantidad, fecha) VALUES (?, ?, ?, ?)",
            (nombre, clase, cantidad, fecha)
        )
    conn.commit()


def obtener_estadisticas():
    cursor.execute("SELECT clase, SUM(cantidad) FROM residuos GROUP BY clase")
    return cursor.fetchall()


def obtener_historial():
    cursor.execute("SELECT nombre, clase, cantidad, fecha FROM residuos ORDER BY fecha DESC")
    return cursor.fetchall()


def borrar_todo():
    cursor.execute("DELETE FROM residuos")
    conn.commit()
