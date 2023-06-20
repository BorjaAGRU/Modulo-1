#Librerias

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

#Configuración de página, puede ser "centered" o "wide"

st.set_page_config(page_title="TARIFAS", layout="wide",page_icon="💰")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("<h1>4. Tarifas </h1>",unsafe_allow_html=True)

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


st.write("")
st.text('Para esta pestaña he modificado el dataframe, añadiendo una columna que nos calcula la tarifa por persona')
st.write("")
st.write("")
st.dataframe(DatosTitanic1)

st.title("Tarifas PP")
st.write("")
st.write("")
st.write("")
col1,col2,col3,col4 = st.columns(4)
with col1:
 dinemb = DatosTitanic1.groupby('Embarked')['FarePP'].sum().round(2)
 dinemb 
with col2:
 dinembse = DatosTitanic1.groupby(['Embarked','Survived'])['FarePP'].sum().round(2)
 dinembse 
with col3:
 dinembsecl = DatosTitanic1.groupby(['Embarked','Survived','Pclass'])['FarePP'].sum().round(2)
 dinembsecl
with col4:
 dinembseclsur = DatosTitanic1.groupby(['Embarked','Survived','Pclass','Sex'])['FarePP'].sum().round(2)
 dinembseclsur

st.write("")
st.write("")
st.write("")

# gr = sns.lmplot(x='FarePP',y='Fare',data=DatosTitanic1,col='Embarked',hue='Sex',palette='coolwarm',aspect=1)
# gr.set(xlim=(0, 2500000), ylim=(0, 5500000))
# gr.set_axis_labels('Tarifa por persona', 'Tarifas Totales')
# gr.axes[0,0].set_xticks(range(0, 2500000, 100))  
# gr.axes[0,0].set_yticks(range(0, 5500000, 100))  
# st.pyplot()

# gr = sns.lmplot(x='FarePP',y='Fare',data=DatosTitanic1,col='Embarked',hue='Sex',palette='coolwarm',aspect=1)
# gr.set(xlim=(0, 2500000), ylim=(0, 5500000))
# gr.set_axis_labels('Tarifa por persona', 'Tarifas Totales')
# gr.axes[0,0].set_xticks(range(0, 2500000, 10))  
# gr.axes[0,0].set_yticks(range(0, 5500000, 10))  
# st.pyplot()

sns.lmplot(x='FarePP',y='Fare',data=DatosTitanic1,col='Embarked',hue='Sex',palette='coolwarm',aspect=1)
st.pyplot()

# DatosT2 = DatosTitanic1.copy(deep=True)
# DatosTitanicT2 = pd.DataFrame(DatosT2)
# maxi = DatosTitanicT2['Fare'].idxmax()
# DatosTitanicT2 = DatosTitanicT2.drop(maxi)
# st.dataframe(DatosTitanicT2)

# sns.lmplot(x='FarePP',y='Fare',data=DatosTitanicT2,col='Embarked',hue='Sex',palette='coolwarm',aspect=1)
# st.pyplot()
st.write("")
st.write("")
st.write("")

sns.lmplot(x='FarePP',y='Fare',data=DatosTitanic1,col='Pclass',hue='Sex',palette='coolwarm',aspect=1)
st.pyplot()