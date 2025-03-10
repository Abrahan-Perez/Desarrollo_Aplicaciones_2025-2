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
# Botón para agregar el producto
if st.button("Agregar Producto"):
    errores = []

    # Validar nombre del producto
    if not nombre_producto.strip():
        errores.append("⚠️ El nombre del producto no puede estar vacío.")

    # Validar precio
    try:
        precio = float(precio)  # Convertimos el precio a número
        if not (0 < precio <= 999):
            errores.append("⚠️ El precio debe estar entre 0 y 999.")
    except ValueError:
        errores.append("⚠️ Ingresa un precio válido en formato numérico.")

    # Validar categoría seleccionada con estructura de control
    if not categorias_seleccionadas:
        errores.append("⚠️ Debes seleccionar al menos una categoría.")
    else:
        for categoria in categorias_seleccionadas:
            if categoria not in categorias_permitidas:
                errores.append(f"⚠️ La categoría '{categoria}' no es válida.")
                break  # Detenemos la validación si encontramos un error

    # Si hay errores, los mostramos
    if errores:
        for error in errores:
            st.error(error)
    else:
        st.success(f"✅ Producto '{nombre_producto}' agregado con éxito.")

