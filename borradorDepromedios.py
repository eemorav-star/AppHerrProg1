import streamlit as st

st.set_page_config(page_title="App de Promedios", page_icon="😄")

# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# PROYECTO CALCULADORA DE PROMEDIOS ESTUDIANTILES
# Creadores del proyecto: Adrian Luna , Kathia Jaen, Elpidio Mora
# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo


#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# ENTRADAS
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
st.title(" Programa para el calculo de promedios MEDUCA PANAMA")

st.header(" Las notas van de 1.0 a 5.0")

nombre = st.text_input("Ingrese el nombre del estudiante")
nota1 = st.number_input("Ingrese la Nota 1", min_value=1.0, max_value=5.0)
nota2 = st.number_input("Ingrese la Nota 2", min_value=1.0, max_value=5.0)
nota3 = st.number_input("Ingrese la Nota 3", min_value=1.0, max_value=5.0)

# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# PROCESO
# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
st.header("Dar clic en el botón")

if st.button("Calcular promedio"):

    promedio = (nota1 + nota2 + nota3) / 3

    # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    #  SALIDA
    # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    st.header(" Resultados de estos calculo del promedio")

    st.write("Nombre del estudiante:", nombre)
    st.write("Nota 1:", nota1)
    st.write("Nota 2:", nota2)
    st.write("Nota 3:", nota3)

    st.success(f"El promedio final es: {promedio:.2f}")