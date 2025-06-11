# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Análisis de Anuncios de Coches",
    page_icon="🚗",
    layout="wide"
)

# --- Carga de datos ---
# Usamos un try-except para manejar el error si el archivo no se encuentra
try:
    df = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("El archivo 'vehicles_us.csv' no se encontró. Asegúrate de que esté en el directorio raíz.")
    st.stop() # Detiene la ejecución si no se encuentran los datos
    
# --- Título y Encabezado ---
st.title('🚗 Análisis de Datos de Anuncios de Vehículos')
st.header('Herramienta para el Análisis Exploratorio de Datos')
st.write("Usa los botones a continuación para generar visualizaciones interactivas.")


# --- Botón para el Histograma ---
st.subheader('Distribución de una variable')
hist_button = st.button('Construir histograma de odómetro')

if hist_button: # se ejecuta cuando el usuario hace clic en el botón
    # Escribir un mensaje informativo
    st.write('Creación de un histograma para la columna del odómetro del conjunto de datos.')

    # Crear un histograma con Plotly Express
    fig_hist = px.histogram(df, x="odometer", title="Distribución del Odómetro")

    # Mostrar el gráfico interactivo en Streamlit
    # use_container_width=True hace que el gráfico ocupe todo el ancho disponible
    st.plotly_chart(fig_hist, use_container_width=True)
    
# --- Botón para el Gráfico de Dispersión ---
st.subheader('Relación entre dos variables')
scatter_button = st.button('Construir gráfico de dispersión de precio vs. año')

if scatter_button: # se ejecuta cuando el usuario hace clic en este otro botón
    # Escribir un mensaje informativo
    st.write('Creación de un gráfico de dispersión para ver la relación entre el año del modelo y el precio.')

    # Crear un gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(df, x="model_year", y="price", title="Precio vs. Año del Modelo")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)        
