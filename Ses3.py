import streamlit as st

def clasificar_puntaje(puntaje):
    if puntaje >= 85:
        return "Excelente"
    elif puntaje >= 70:
        return "Bueno"
    else:
        return "Necesita Mejorar"
    
# Interfaz en Streamlit

st.title("Clasificación de Puntajes")
st.write("Ingrese un puntaje y el sistema lo calsificará. ")

# Entrada de usuario
puntaje = st.number_input("Ingrese un puntaje (0-100):", min_value=0, max_value=100, step=1)

# Boton para clasificar

if st.button("Clasificar"):
    resultado = clasificar_puntaje(puntaje)
    st.sucess(f"El puntaje {puntaje} es clasificado como: {resultado}")