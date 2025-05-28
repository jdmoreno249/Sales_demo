# Import libraries

import streamlit as st
import pandas as pd

# General configuration

st.set_page_config(

    page_title= "Demo ventas semanales",
    layout= "wide",
    initial_sidebar_state= "expanded"

)

# Creation of dataset

data = {

        "dia": ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"],
        "ventas": [150, 200, 180, 220, 300, 250, 190]

}

df = pd.DataFrame(data)

# sidebar: filters

st.sidebar.header("Filtros de Visualización")
dias = df["dia"].tolist()

seleccion = st.sidebar.multiselect(

    "Selecciona los días a mostrar",
    options = dias,
    default = dias


)

df_filt = df[df["dia"].isin(seleccion)]

# Title & Description of the main area

st.title("Dashboard de ventas semanales")

st.markdown("Este dashboard muestra las ventas semanales por día,"

            "Ahora filtrable desde la barra lateral."

)

# Showing the filtered data table

st.subheader("Datos de Ventas")
st.dataframe(df_filt)

# Total sales KPI´s

total_ventas = df_filt["ventas"].sum()
st.metric("Ventas totales",f"{total_ventas}")

# Bar chart for sales

st.subheader("Ventas por Día")
st.bar_chart(df_filt.set_index("dia")["ventas"])

# Final messages with ending horizontal line

st.markdown("---")
st.markdown("Gracias por su atención")
