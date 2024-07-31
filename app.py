import streamlit as st
import pandas as pd 
import plotly_express as pl

vehiculos = pd.read_csv('C:/Users/andre/Documents/TRIPLETEN ANALISIS DE DATOS/PROYECTOS CON GITHUB Y VS/clonacion_VS/proyect_6_trip/vehicles_us.csv')
st.header('Autos')
boton_hist_1 = st.button('Construir histograma') # crear un botón para el histograma
boton_disp_1 = st.button('Contruir grafico de dispersion')# crea boton para diagrama de dispersion

if boton_hist_1: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

if boton_disp_1:
        #se escribe el mensaje
        st.write('Creacion de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
        #crea el diagrama de dispersion, Reemplaza 'column_name' y 'value_column' con los nombres de las columnas
        fig_bar = px.bar(vehiculos, x='column_name', y='value_column')  
        #muestra un grafico 
        st.plotly_chart(fig_bar)
        
        

