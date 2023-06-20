#Librerias

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

#Configuración de página, puede ser "centered" o "wide"

st.set_page_config(page_title="BUSCADOR", layout="wide",page_icon="🔍")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("<h1>6. Buscador </h1>",unsafe_allow_html=True)

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
DatosTitanic1['N_T'] = [DatosTitanic1 ['Ticket'].value_counts()[billete] for billete in DatosTitanic1['Ticket']]
DatosTitanic1['FarePP'] = DatosTitanic1['Fare'] / DatosTitanic1['N_T'].round(2)
DatosTitanic1.drop('N_T', axis=1, inplace=True)

#st.dataframe(DatosTitanic1)
st.write("")
st.write("")
nom = st.checkbox("Busqueda personas por apellido")
if nom:
    apellido = st.text_input('Busqueda personas')
    dfnombre = DatosTitanic1[DatosTitanic1['Last Name'].str.contains(apellido, case=False)]
    st.dataframe(dfnombre) 

st.write("")
st.write("")

busq = st.checkbox("Busqueda personas con filtros")
if busq:
 st.write("")
 st.write("")
 st.text("Podemos utilizar los filtros de la derecha para hacer busquedas mas especificas")    
 st.write("")
 st.write("")
 st.write("")

  #Sidebar con filtros

 # filtro_gen = st.sidebar.selectbox("Genero", np.append(DatosTitanic1["Sex"].unique(),' '))

 # if filtro_gen:
 #     if filtro_gen == ' ':
 #         datfiltro_gen = ' '
  #     else:
 #         df1 = DatosTitanic1.loc[DatosTitanic1["Sex"]==filtro_gen]
 #         datfiltro_gen=DatosTitanic1["Sex"]
 # filtro_tar = st.sidebar.selectbox("Genero", np.append(DatosTitanic1["Sex"].unique(),' ',Menos de 1000','Mas de 1000'))

 # if filtro_tar:
 #     if filtro_tar == ' ':
 #         datfiltro_tar = ' '
 #     if filtro_tar == 'Menos de 1000':
 #         datfiltro_tar = ''
 #     if filtro_tar == 'Mas de 1000':
 #         datfiltro_tar = ''

    
 # else:
  #    df1 = DatosTitanic1.loc[DatosTitanic1['FarePP']==filtro_tar]
 #    datfiltro_tar=DatosTitanic1['FarePP']

 # if filtro_gen and filtro_class and filtro_sur and filtro_emb and filtro_gru: 
 #     df2 = DatosTitanic1.loc[
  #                          (DatosTitanic1["Sex"] == filtro_gen) & 
 #                          (DatosTitanic1['Survived']==filtro_sur) &  
   #                          (DatosTitanic1['Pclass']==filtro_class) &
 #                          (DatosTitanic1['Embarked']==filtro_emb) & 
  #                          (DatosTitanic1['Group']==filtro_gru) 
 #                           ]


 st.sidebar.title('Filtros')

 filtro_gen = st.sidebar.multiselect("Genero", DatosTitanic1["Sex"].unique())

 filtro_sur = st.sidebar.multiselect('Superviviente',DatosTitanic1['Survived'].unique())

 filtro_class = st.sidebar.multiselect('Clase', DatosTitanic1['Pclass'].unique())

 filtro_emb = st.sidebar.multiselect('Puerto', DatosTitanic1['Embarked'].unique())

 filtro_gru = st.sidebar.multiselect('Rango edad', DatosTitanic1['Group'].unique())

 filtro_edad = st.sidebar.slider('Edad', min_value=0, max_value=90, value=(0, 90))

 filtro_fare = st.sidebar.slider('Trifa', min_value=0, max_value=550, value=(0, 550))

 #Dibujar dataframe con los filtros
 DatosFiltrados = DatosTitanic1.copy()
 if filtro_gen:
    DatosFiltrados = DatosFiltrados[DatosFiltrados['Sex'].isin(filtro_gen)]
 if filtro_sur:
    DatosFiltrados = DatosFiltrados[DatosFiltrados['Survived'].isin(filtro_sur)]
 if filtro_class:
    DatosFiltrados = DatosFiltrados[DatosFiltrados['Pclass'].isin(filtro_class)]
 if filtro_emb:
    DatosFiltrados = DatosFiltrados[DatosFiltrados['Embarked'].isin(filtro_emb)]
 if filtro_gru:
    DatosFiltrados = DatosFiltrados[DatosFiltrados['Group'].isin(filtro_gru)]
 if filtro_edad:
    DatosFiltrados =  DatosFiltrados[( DatosFiltrados['Age'] >= filtro_edad[0]) & ( DatosFiltrados['Age'] <= filtro_edad[1])]
 if filtro_fare:
    DatosFiltrados =  DatosFiltrados[( DatosFiltrados['Fare'] >= filtro_fare[0]) & ( DatosFiltrados['Fare'] <= filtro_fare[1])]

 st.dataframe(DatosFiltrados)

 st.write("")
 st.write("")
 grafics = st.checkbox("Graficas")
 if grafics:
  col1, col2, col3 = st.columns(3)
  with col1:
    st.subheader("Genero")
    sex_count = DatosFiltrados["Sex"].value_counts()
    custom_colors = ['#FF1C22', '#1FFA5B']
    fig1 = px.pie(sex_count, values="Sex", names=sex_count.index,color_discrete_sequence=custom_colors)
    st.plotly_chart(fig1, use_container_width=True)
  with col2:
     st.subheader("Grupos de edad")
     age_group = DatosFiltrados["Group"].value_counts()
     custom_colors = ['#1FFA5B']
     fig2 = px.bar(age_group, y="Group", x=age_group.index, color_discrete_sequence=custom_colors)
     st.plotly_chart(fig2, use_container_width=True)
  with col3:
     st.subheader("Clase")
     soc_class = DatosFiltrados["Pclass"].value_counts()
     custom_colors = ['#FF1C22']
     fig3 = px.bar(soc_class, y=soc_class.index, x="Pclass", orientation='h',color_discrete_sequence=custom_colors )
     #fig3.set_xlabel()
     st.plotly_chart(fig3, use_container_width=True)

st.write("")
st.write("")

enlace = st.checkbox("Enlaces Externos")
if enlace:
 st.markdown("<h3>Enlaces Externos </h3>",unsafe_allow_html=True)
 st.write("")
 col1,col2,col3 = st.columns(3)    
 with col1:
    st.write("")
 with col2:
    st.write("")
    st.text("Enlace a Wikipedia")
    st.write("")
    st.markdown("https://es.wikipedia.org/wiki/RMS_Titanic")
    st.write("")
    st.write("")
    st.video("https://www.youtube.com/watch?v=FiRVcExwBVA")
    st.write("") 
 with col3:
    st.write("")

