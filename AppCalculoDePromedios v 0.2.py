
import streamlit as st

st.set_page_config(page_title="App de Promedios", page_icon="👍")

# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# PROYECTO : Calcula pormedios en el sistema de educativo de Panama 
# Creadores del proyecto: Adrian Luna , Kathia Jaen, Elpidio Mora
# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

# Varables de de los trimestres anteriores
PrimerTrimestre = 0.0
SegundoTrimestre = 0.0
TercerTrimestre = 0.0

i = 0
j = 0
promedio = 0.0
notasParciales = []
notasAP = []
promedioParciales = 0.0
promedioAp = 0.0
promediofinal = 0.0
ExamenFinal = 0.0     #representa el examen trimestral


#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# ENTRADAS 1 De notas parciales, notas de apreciacion examen, trimestral, examen final promedio final 
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
st.title(" Cálculo de notas promedios en el sistema educativo de Panama")

st.header(" Las notas van de 1.0 a 5.0")

nombre = st.text_input("Nombre del estudiante")
    
    
numeroDeNotas = st.number_input("¿Cuantas notas parciales son?", min_value=1, max_value=15, step=1)

notas = []
for i in range(i, numeroDeNotas):
    notaParcial = st.number_input(f"Ingrese la nota {i + 1}", min_value=1.0, max_value=5.0, step=0.1)
    notas.append(notaParcial)

# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# PROCESO
# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo


    promedioParciales = sum(notas) / len(notas)
   

numeroDeNotasAP = st.number_input("¿Cuantas notas de apreciación son?", min_value=1, max_value=15, step=1)
notasAP = []
for j in range(j, numeroDeNotasAP):
    notaApreciacion = st.number_input(f"Ingrese la nota de apreciación {j + 1}", min_value=1.0, max_value=5.0, step=0.1)
    notasAP.append(notaApreciacion)
    
    promedioAp = sum(notasAP) / len(notasAP)


examenFinal = st.number_input("Ingrese la nota del examen Trimestral final", min_value=1.0, max_value=5.0, step=0.1)

promediofinal = (promedioParciales + promedioAp + examenFinal) / 3

 # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
 #  SALIDA 1 Calula notas parciales, notas de apreciación y examen final para obtener el promedio final del año escolar
 # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# Botón para calcular
if st.button("Calcular Promedio de todas las notas"):
    

    st.header(" Las notas y  el promedio final es:")

    st.write("Nombre del estudiante:", nombre)
    for i, nota in enumerate(notas, start=1):
        st.write(f"Nota Parcial {i}:", nota)
    for j, nota in enumerate(notasAP, start=1):
        st.write(f"Nota de apreciación {j}:", nota)
        
        st.write(f"Nota del examen trimestral final:", f"{examenFinal:.2f}")
    st.success(f"La nota final del año escolar es: {promediofinal:.2f}")
    
    if promediofinal >= 3.0:
        st.success("¡Felicidades! Vamos bien.")
    else:
        st.write("Tu acudiente debe hablar con el docente de la materia, estas reprobando.")

 # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOO
 #  Entrada 2 Calcula la nota final del año escolar incluyendo las notas de los trimestres anteriores
 # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

st.title("¿Desea incluir notas de los trimestres anteriores?")

st.title("Calculadora de Promedio Acumulado del Año Escolar")

st.write("Ingrese únicamente los trimestres que ya han sido cursados.")

# Selección de cantidad de trimestres cursados
cantidad_trimestres = st.selectbox("¿Cuántos trimestres desea considerar?", [1, 2, 3]) # Lista para almacenar las notas

notas = []

# Primer trimestre
primer_trimestre = st.number_input("Nota del Primer Trimestre",min_value=0.0,max_value=5.0,step=0.1)
notas.append(primer_trimestre)

# Segundo trimestre (solo si aplica)
if cantidad_trimestres >= 2:
    segundo_trimestre = st.number_input("Nota del Segundo Trimestre",min_value=0.0,max_value=5.0,step=0.1)
    notas.append(segundo_trimestre)

# Tercer trimestre (solo si aplica)
if cantidad_trimestres == 3:
    tercer_trimestre = st.number_input("Nota del Tercer Trimestre",min_value=0.0, max_value=5.0,step=0.1 )
    notas.append(tercer_trimestre)

 # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOO
 #  SALIDA 2 Calcula la nota final del año escolar incluyendo las notas de los trimestres anteriores
 # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOOO


# Botón para calcular
if st.button("Calcular Promedio Acumulado"):

    promedio_anual = sum(notas) / len(notas)

    st.subheader("Resultados")

    for i, nota in enumerate(notas, start=1):
        st.write(f"Trimestre {i}: {nota:.2f}")

    st.success(f"Promedio acumulado del año escolar: {promedio_anual:.2f}")
    

    if promedio_anual >= 3.0:
        st.success("✅ Que bueno sigue asi mejorando.")
    else:
        st.error(" Estás reprobando la asignatura, tu acudiente dbe hablar con el docente." )