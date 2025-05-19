# supabase_config.py

from supabase import create_client, Client
from datetime import datetime

# ⚙️ CONFIGURA TU SUPABASE (Rellena esto con tus datos)
SUPABASE_URL = "https://ffhgrwciuzauohqzjqku.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZmaGdyd2NpdXphdW9ocXpqcWt1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5MTc5MTMsImV4cCI6MjA2MDQ5MzkxM30.1TeeoSwwvm-dxj0wZiQWVKzgSM3Aqf_ri5uY2tGMAuk"

# Cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def insertar_detecciones(nombre_objeto, counts):
    """Guarda los resultados en Supabase"""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for clase, cantidad in counts.items():
        data = {
            "nombre": nombre_objeto,
            "clase": clase,
            "cantidad": cantidad,
            "fecha": fecha,
            "imagen_url": None  # puedes agregar esto si guardas imágenes luego
        }
        supabase.table("residuos").insert(data).execute()


def obtener_estadisticas():
    """Devuelve un resumen de cantidad por clase"""
    # Esto requiere una función SQL en Supabase llamada `get_material_counts`
    response = supabase.rpc("get_material_counts").execute()
    return response.data if response.data else []


def obtener_historial():
    """Devuelve todas las detecciones ordenadas por fecha"""
    response = supabase.table("residuos").select(
        "nombre, clase, cantidad, fecha"
    ).order("fecha", desc=True).execute()
    return response.data
