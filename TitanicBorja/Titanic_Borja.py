#Librerias

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

#Configuración de página, puede ser "centered" o "wide"

st.set_page_config(page_title="TITANIC", layout="wide",page_icon="🚢")
st.set_option('deprecation.showPyplotGlobalUse', False)


st.markdown("<h1> Titanic </h1>",unsafe_allow_html=True)

st.write("")
st.write("")


st.text('A continuación analizaremos los datos del fichero titanic.csv, podremos ver una página como se han trabajdo los datos para poder analizarlos, y en las otras páginas')
st.text('veremos diferentes datos y gráficos en función a diferentes variables que teniamos. Finalmente tenemos un buscador por si necesitamos unos datos en especifico.')

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


st.image("Imagen/Titanic2.png",width=900)





