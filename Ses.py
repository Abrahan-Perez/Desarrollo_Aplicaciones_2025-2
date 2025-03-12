import streamlit as st
from supabase import create_client, Client
import os

# Configurar supabase

SUPABASE_URL = "https://eoxlfglsbqavwqssqkpm.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVveGxmZ2xzYnFhdndxc3Nxa3BtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE3NDU1NjMsImV4cCI6MjA1NzMyMTU2M30.U1vitSkPEkQ_CNkJgeP6yHWzQq3_i767aqPRy-rsOhc"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Gestión de Clientes - CRUD con Supabase y Streamlit")

#Formulario para agregar cliente
st.header("Agregar Cliente")
nombre = st.text_input("Nombre")
email = st.text_input("Email")
telefono = st.text_input("Teléfono")

if st.button("Agregar Cliente"):
    if nombre and email:
        data ={"nombre": nombre, "email": email, "telefono": telefono}
        response = supabase.table("clientes").insert(data).execute()
        st.success("Cliente agregado correctamente")
    else:
        st.warning("Nombre y Email son obligatorios")
        
st.header("Cliente Registrado")