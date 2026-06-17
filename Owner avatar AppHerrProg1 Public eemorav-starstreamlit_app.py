import streamlit as st

# Título de la aplicación
# ==========================================
# PROYECTO 1
# CALCULADORA DE PROMEDIOS ESTUDIANTILES
# ==========================================

print("===================================")
print(" CALCULADORA DE PROMEDIOS")
print("===================================")
st.title("📚 Calculadora de Promedios Estudiantiles")

# Datos del estudiante
nombre_estudiante = st.text_input(
    "Nombre del estudiante"
)

nota1 = st.number_input(
    "Nota #1",
    min_value=0.0,
    max_value=100.0
)

nota2 = st.number_input(
    "Nota #2",
    min_value=0.0,
    max_value=100.0
)

nota3 = st.number_input(
    "Nota #3",
    min_value=0.0,
    max_value=100.0
)

# Botón
if st.button("Calcular Promedio"):

    promedio = (nota1 + nota2 + nota3) / 3

    st.subheader("Resultados")

    st.write("Estudiante:", nombre_estudiante)
    st.write("Promedio:", round(promedio, 2))

    if promedio >= 71:
        st.success("✅ APROBADO")
    else:
        st.error("❌ REPROBADO")
