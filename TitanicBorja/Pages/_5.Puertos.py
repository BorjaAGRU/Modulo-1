#Librerias

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

#Configuración de página, puede ser "centered" o "wide"

st.set_page_config(page_title="PUERTOS", layout="centered",page_icon="⚓")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("<h1>5. Puertos </h1>",unsafe_allow_html=True)

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


# embarked = st.sidebar.checkbox("Análisis con la columna 'Embarked'")
# if embarked:
#     st.markdown("<center><h2><l style='color:black; font-size: 30px'>Análisis con la columna 'Embarked'</h2></center>", unsafe_allow_html=True)
#     st.markdown("<center><h2><l style='color:black; font-size: 25px'>Selecciona el dato que deseas obtener:</h2></center>", unsafe_allow_html=True)
filtro_emb = st.selectbox('Embarked',('Southampton','Cherbourg','Queenstown'))
col1,col2,col3 = st.columns(3)
if filtro_emb=='Southampton':
        st.dataframe(DatosTitanic1[DatosTitanic1['Embarked']=='Southampton'])
        with col2:
            st.map(pd.DataFrame(data=[[50.90924579946069, -1.415602588636794]],columns=['lat','lon']),use_container_width=True,zoom=10)
            st.markdown("<l style='color:black; font-size: 20px'>{} pasajeros son de Southampton.".format(DatosTitanic1['Embarked'].str.count('Southampton').sum()), unsafe_allow_html=True)
    
if filtro_emb=='Cherbourg':
        st.dataframe(DatosTitanic1[DatosTitanic1['Embarked']=='Cherbourg'])
        with col2:
            st.map(pd.DataFrame(data=[[49.63517232850006, -1.6226017632949319]],columns=['lat','lon']),use_container_width=True,zoom=10)
            st.markdown("<l style='color:black; font-size: 20px'>{} pasajeros son de Cherbourg.".format(DatosTitanic1['Embarked'].str.count('Cherbourg').sum()), unsafe_allow_html=True)
    
if filtro_emb=='Queenstown':
        st.dataframe(DatosTitanic1[DatosTitanic1['Embarked']=='Queenstown'])
        with col2:
            st.map(pd.DataFrame(data=[[51.84966781537349, -8.293537771378299]],columns=['lat','lon']),use_container_width=True,zoom=10)
            st.markdown("<l style='color:black; font-size: 20px'>{} pasajeros son de Queenstown (actualmente Cobh).".format(DatosTitanic1['Embarked'].str.count('Queenstown').sum()), unsafe_allow_html=True)

