import streamlit as st
from PIL import Image
import tempfile
import os
import matplotlib.pyplot as plt

from detector import detectar_objetos
from db import guardar_deteccion, obtener_estadisticas, obtener_historial, borrar_todo
from utils import info_material, exportar_a_csv

st.set_page_config(page_title="Dashboard de Reciclaje", layout="centered")
st.title("Dashboard Inteligente de Reciclaje")
st.write("Análisis y clasificación automática de residuos para fomentar el reciclaje inteligente")
st.write("---")

#subir imagen
st.subheader("Paso 1: Subir imagen")
uploaded_file = st.file_uploader("Selecciona una imagen para analizar (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        image.save(temp.name)
        temp_path = temp.name

    img_array, counts = detectar_objetos(temp_path)

    #visualización
    st.subheader("Paso 2: Visualización del análisis")
    col_img1, col_img2 = st.columns(2)
    col_img1.image(image, caption="Imagen original", width=300)
    col_img2.image(img_array, caption="Resultado del modelo", width=300)

    #materiales detectados
    st.subheader("Paso 3: Materiales detectados")
    for clase, cantidad in counts.items():
        clase_lower = clase.lower()
        desc = info_material.get(clase_lower, {}).get("desc", "No disponible")
        recom = info_material.get(clase_lower, {}).get("recom", "No disponible")

        with st.container():
            st.markdown(f"Material: {clase.capitalize()} — {cantidad} detectado(s)")
            st.markdown(f"Descripción: {desc}")
            st.markdown(f"Recomendación: {recom}")
            st.write("---")

    #guardar en base de datos
    st.subheader("Paso 4: Registrar esta detección")
    nombre = st.text_input("Nombre para esta detección (ejemplo: Botella de agua)")
    if st.button("Guardar en base de datos"):
        guardar_deteccion(nombre, counts)
        st.success("Detección guardada correctamente en la base de datos.")

    os.remove(temp_path)

#Estadísticas 
st.write("---")
st.subheader("Estadísticas generales del reciclaje")
if st.button("Mostrar resumen de materiales detectados"):
    data = obtener_estadisticas()
    if data:
        st.markdown("Total acumulado por tipo de material")
        clases, cantidades = zip(*data)
        col1, col2 = st.columns([1, 2])
        with col1:
            for c, q in zip(clases, cantidades):
                st.markdown(f"{c.capitalize()}: {q} unidades")
        with col2:
            fig, ax = plt.subplots()
            ax.pie(cantidades, labels=clases, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
    else:
        st.info("No hay estadísticas registradas.")

#Historial
st.write("---")
with st.expander("Ver historial de detecciones", expanded=False):
    historial = obtener_historial()
    if historial:
        st.markdown("Historial de objetos detectados")
        for nombre, clase, cantidad, fecha in historial:
            st.markdown(f"{nombre} — {clase.capitalize()} ({cantidad}) — {fecha}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Exportar historial a CSV"):
                ruta = exportar_a_csv(historial)
                with open(ruta, "rb") as f:
                    st.download_button("Descargar CSV", f, file_name=ruta)
        with col2:
            if st.button("Borrar todos los registros"):
                borrar_todo()
                st.warning("Todos los registros fueron eliminados correctamente.")
    else:
        st.info("No hay detecciones registradas aún.")
