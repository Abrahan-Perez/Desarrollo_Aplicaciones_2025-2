import streamlit as st

st.title("Formulario de Productos - Confitería Dulcino")
#Creando entrada para nombre del producto
nombre_producto = st.text_input("Nombre del producto", max_chras=20)
#Entrada para el precio
precio = st.text_input("Precio del producto")
#Lista de categorias permitidas
categorias_permitidas = ["Chocolates", "Caramelos", "Mashmelo", "Galletas", "Salados", "Gomas de mascar"]
