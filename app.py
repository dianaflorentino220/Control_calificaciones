
import streamlit as st

from modulo_proceso import calcular_promedio, determinar_estado

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Calificaciones",
    page_icon="🎓"
)

# Título
st.title("🎓 Sistema de Calificaciones")

st.write("Ingresa tus datos para calcular tu promedio final.")

# Nombre del estudiante
nombre = st.text_input("Nombre del estudiante:")

# Cantidad de calificaciones
cantidad = st.selectbox(
    "Cantidad de calificaciones:",
    [1, 2, 3, 4]
)

# Formulario
with st.form("formulario_calificaciones"):

    st.subheader("Ingresa tus calificaciones")

    calificaciones = []

    for i in range(cantidad):

        nota = st.number_input(
            f"Calificación {i + 1}:",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.1
        )

        calificaciones.append(nota)

    boton = st.form_submit_button("Calcular promedio")

# Procesar los datos
if boton:

    if nombre.strip() == "":
        st.error("Debes ingresar el nombre del estudiante.")

    else:

        promedio = calcular_promedio(calificaciones)

        estado = determinar_estado(promedio)

        st.subheader("Resultados")

        st.write("Estudiante:", nombre)

        st.write("Calificaciones:", calificaciones)

        st.metric("Promedio final", f"{promedio:.2f}")

        if estado == "Aprobado":
            st.success("¡Felicidades! Estás Aprobado.")

        else:
            st.error("Estás Reprobado.")
