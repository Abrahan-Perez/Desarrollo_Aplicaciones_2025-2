import streamlit as st
# Titulo de la aplicación
st.title("Bienvanido a mi aplicación")

#Solicitar nombre

nombre = st.text_input("Por favor ingresa tu nombre")

#Mostrar el saludo si el usuario ingresa su nombre

if nombre:
    st.write(f"Hola, {nombre}! Bienvenido a esta aplicación web de Streamlit")