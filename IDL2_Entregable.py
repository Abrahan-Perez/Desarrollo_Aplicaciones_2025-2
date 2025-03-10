import streamlit as st

st.title("Formulario de Productos - Confitería Dulcino")
#Creando entrada para nombre del producto
nombre_producto = st.text_input("Nombre del producto", max_chars=20)
#Entrada para el precio
precio = st.text_input("Precio del producto")
#Lista de categorias permitidas
categorias_permitidas = ["Chocolates", "Caramelos", "Mashmelo", "Galletas", "Salados", "Gomas de mascar"]
#Seleccion de categorias
categorias_seleccionadas = st.multiselect("Categoría del producto", categorias_permitidas)
#Opción de definir si el producto está en venta
en_venta = st.radio("¿El producto está en venta?", ["SÍ, No"])

