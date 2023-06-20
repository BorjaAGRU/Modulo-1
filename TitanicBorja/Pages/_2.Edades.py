#Librerias

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

#Configuración de página, puede ser "centered" o "wide"

st.set_page_config(page_title="EDADES", layout="wide",page_icon="👨‍👩‍👧‍👧")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("<h1>2. Edades </h1>",unsafe_allow_html=True)

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
DatosTitanic1['Fare'] = DatosTitanic1['Fare'].astype(str).str.replace('.', '', regex=True)  
DatosTitanic1['Fare'] = DatosTitanic1['Fare'].astype(int) 
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
# st.subheader("Datos :blue[Edades]")
st.write("")
st.write("")

st.subheader("Rango Edades")
st.write("")
st.write("")

col1,col2,col3,col4 = st.columns(4)
with col1:
 st.write("")
with col2:
 st.text("Tabla")
 grupos = DatosTitanic1['Group'].value_counts()
 grupos
with col3:
 st.text("Grafica")
 colores = ['#1FFA5B', '#93FFB1', '#F7F7FC', '#F58C8F', '#FF1C22']
 fig = px.pie(grupos.head(10), values="Group",color_discrete_sequence=colores)
 st.plotly_chart(fig)
with col4:
 st.write("")

st.write("")
st.write("")
st.subheader("Analisis Rango Edades")
st.write("")
st.write("")
st.write("")

col1,col2 = st.columns(2)
with col1:
    colores = ['#1FFA5B', '#93FFB1', '#F7F7FC', '#F58C8F', '#FF1C22']
    groupgen = DatosTitanic1.groupby(['Group', 'Sex']).size().reset_index(name='count')
    grafica1 = px.bar(groupgen, x='Sex', y='count', color='Group', barmode='group', color_discrete_sequence=colores)
    grafica1.update_layout(title='GENERO')      
    st.plotly_chart(grafica1)
with col2:
    colores = ['#1FFA5B', '#93FFB1', '#F7F7FC', '#F58C8F', '#FF1C22']
    groupclass = DatosTitanic1.groupby(['Group', 'Pclass']).size().reset_index(name='count')
    grafica2 = px.bar(groupclass, x='Pclass', y='count', color='Group', barmode='group', color_discrete_sequence=colores)
    grafica2.update_layout(title='CLASE')      
    st.plotly_chart(grafica2)

st.write("")

col1,col2 = st.columns(2)    
with col1:
    colores = ['#1FFA5B', '#93FFB1', '#F7F7FC', '#F58C8F', '#FF1C22']
    groupsal = DatosTitanic1.groupby(['Group', 'Survived']).size().reset_index(name='count')
    grafica3 = px.bar(groupsal, x='Survived', y='count', color='Group', barmode='group', color_discrete_sequence=colores)
    grafica3.update_layout(title='SUPERVIVIENTES')      
    st.plotly_chart(grafica3)
with col2:
    colores = ['#1FFA5B', '#93FFB1', '#F7F7FC', '#F58C8F', '#FF1C22']
    groupemb = DatosTitanic1.groupby(['Group', 'Embarked']).size().reset_index(name='count')
    grafica4 = px.bar(groupemb, x='Embarked', y='count', color='Group', barmode='group', color_discrete_sequence=colores)
    grafica4.update_layout(title='PUERTOS')      
    st.plotly_chart(grafica4)

st.write("")
st.write("")

st.markdown("<h5 style=>Distribución de pasajeros en función de su edadla , clase , tarifa y genero </h5>", unsafe_allow_html=True)

custom_colors = ['#FF1C22', '#1FFA5B']
fig2 = px.scatter_3d(DatosTitanic1, x='Age', y='Pclass', z='Fare', color='Sex', color_discrete_sequence=custom_colors)
fig2.update_layout(scene=dict(
    yaxis=dict(
        tickvals=[1, 2, 3]
    )
))
st.plotly_chart(fig2, theme = None, use_container_width=True)
