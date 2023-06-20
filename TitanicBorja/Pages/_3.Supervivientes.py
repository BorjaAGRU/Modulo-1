#Librerias

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

#Configuración de página, puede ser "centered" o "wide"

st.set_page_config(page_title="SUPERVIVIENTES", layout="wide",page_icon="🛟")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("<h1>3. Supervivientes </h1>",unsafe_allow_html=True)

DatosTitanic0 = pd.read_csv(r'Datos/titanic.csv')
#st.dataframe(DatosTitanic0)

DatosTitanic1 = DatosTitanic0.copy()

DatosTitanic1 = DatosTitanic1.set_index(DatosTitanic1.columns[0])
DatosTitanic1.drop("Cabin", axis=1, inplace=True)
MEDIAEDAD = DatosTitanic1['Age'].median()
DatosTitanic1['Age'].fillna(MEDIAEDAD, inplace=True)
DatosTitanic1['Age'] = DatosTitanic1['Age'].astype(int)
MODAEMB = DatosTitanic1['Embarked'].mode()[0]
DatosTitanic1['Embarked'].fillna(MODAEMB, inplace=True)
DatosTitanic1['First Name'] = DatosTitanic1['Name'].str.split(',').str[1].str.split('.').str[1]
DatosTitanic1['Last Name'] = DatosTitanic1['Name'].str.split(',').str[0]
def obtener_group(edad):
    if edad <= 15:
        return 'niño'
    elif edad <= 25:
        return 'adolescente'
    elif edad <= 35:
        return 'joven'
    elif edad <= 60:
        return 'adulto'
    else:
        return 'anciano'

    
DatosTitanic1['Group'] = DatosTitanic1['Age'].apply(obtener_group) 
sus = {0: 'No', 1: 'Yes'}
DatosTitanic1['Survived'] = DatosTitanic1['Survived'].replace(sus)
sus2 = {'C': 'Cherbourg', 'Q' : 'Queenstown' , 'S' : 'Southampton'}
DatosTitanic1['Embarked'] = DatosTitanic1['Embarked'].replace(sus2)
nom = DatosTitanic1.pop('First Name')
DatosTitanic1.insert(3,'First Name',nom)
ape = DatosTitanic1.pop('Last Name')
DatosTitanic1.insert(4,'Last Name',ape)
DatosTitanic1.drop('Name', axis=1, inplace=True)

#st.dataframe(DatosTitanic1)


st.write("")
st.write("")
col1,col2 = st.columns(2)    
with col1:
 st.markdown("<h3> Totales </h3>",unsafe_allow_html=True)
 st.write("")
 sur = DatosTitanic1['Survived'].value_counts()
 sur
 colores = ['#FA1915', '#2EF421']
 fig = px.pie(sur, values='Survived',width=700, height=700, color_discrete_sequence=colores)
 st.plotly_chart(fig)
with col2:
 st.markdown("<h3> Puertos </h3>",unsafe_allow_html=True)
 st.write("")
 sexossalvados = DatosTitanic1.groupby(['Embarked'])['Survived'].value_counts()
 sexossalvados
 sexossalvados = DatosTitanic1.groupby(['Embarked', 'Survived'])['Survived'].count().reset_index(name='cantidad')
 color= sns.color_palette(['#1FFA5B','#F7F7FC','#FF1C22'])
 sns.barplot(x='Survived', y='cantidad', hue='Embarked', data=sexossalvados,palette=color, edgecolor='black')
 sns.color_palette("bright")
 st.pyplot()

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.markdown("<h1>¿Mujeres y niños primero?</h1>",unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")


# scatter = px.scatter(DatosTitanic1,'Age', 'Sex', color='Survived', color_discrete_sequence=['#FA1915', '#2EF421'],title="Superviventes Edad-Genero",category_orders={'Sex': ['male', 'female']})
# scatter.update_layout(height=400,width=1600)
# scatter.update_layout(yaxis=dict(tickmode='linear', tickangle=45))
# scatter.update_layout(xaxis=dict(tickmode='linear', dtick=3, range=[0, scatter.data[0]['x'].max()]))
# st.plotly_chart(scatter)
scatter = px.scatter(DatosTitanic1, 'Age', 'Sex', color='Survived', color_discrete_sequence=['#FA1915', '#2EF421'], title="Supervivientes Edad-Genero", category_orders={'Sex': ['male', 'female']})
scatter.update_layout(height=400, width=1600)
scatter.update_layout(yaxis=dict(tickmode='linear', tickangle=45))
scatter.update_layout(xaxis=dict(tickmode='linear', dtick=3, range=[0, scatter.data[0]['x'].max()]))
st.plotly_chart(scatter)

st.write("")
st.write("")
st.write("") 
st.write("")

col1,col2 = st.columns(2)    
with col1:
 st.markdown("<h3> Noticias </h3>",unsafe_allow_html=True)
 st.write("")
 st.text("BBC")
 st.write("")
 st.markdown("https://www.bbc.com/mundo/noticias/2012/04/120413_mujeres_ninos_primero_mito_adz")
 st.write("")
 st.text("ABC")
 st.write("")
 st.markdown("https://www.abc.es/ciencia/abci-mujeres-ninos-primero-mito-201207310000_noticia.html")
 st.write("")
 st.write("")
with col2:
 st.write("")
 st.write("")
 st.image("Imagen/leo2.png",width=500)
 