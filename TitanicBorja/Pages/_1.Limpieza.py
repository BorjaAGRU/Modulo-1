#Librerias

import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

#Configuración de página, puede ser "centered" o "wide"

st.set_page_config(page_title="LIMPIEZA", layout="wide",page_icon="🖥️")
st.set_option('deprecation.showPyplotGlobalUse', False)


st.markdown("<h1>1. Limpieza de datos </h1>",unsafe_allow_html=True)

st.write("")
st.write("")

st.text('Aqui tenemos el Dataframe original')

st.write("")
st.write("")

DatosTitanic0 = pd.read_csv(r'Datos/titanic.csv')
st.dataframe(DatosTitanic0)

DatosTitanic1 = DatosTitanic0.copy()

st.write("")
st.write("")

nuls= st.sidebar.checkbox("Análisis de nulos")
if nuls:
 st.write("")
 nuls = DatosTitanic0.isnull().sum()
 porce = (nuls / len(DatosTitanic0)) * 100
 datsfal = pd.concat([nuls, porce], axis=1, keys=['Cantidad', 'Porcentaje'])
 fig, ax = plt.subplots(figsize=(20, 10))
 sns.heatmap(datsfal, cmap='binary', annot=True, fmt='.1f')
 plt.title('Nulos')
 st.pyplot(fig)
st.write("")
st.write("")

nul= st.sidebar.checkbox("¿Como he trabajado los nulos?")
if nul:
 code1 = '''#Aqui podemos ver todo el procesamiento de los datos nulos: 
 DatosTitanic1.drop("Cabin", axis=1, inplace=True)
 MEDIAEDAD = DatosTitanic1['Age'].median()
 DatosTitanic1['Age'].fillna(MEDIAEDAD, inplace=True)
 MODAEMB = DatosTitanic1['Embarked'].mode()[0]
 DatosTitanic1['Embarked'].fillna(MODAEMB, inplace=True)'''  

 st.code(code1 , language='python')

procesamiento = st.sidebar.checkbox('Dataframe sin nulos')
if procesamiento:
    DatosTitanic0['Embarked'] = DatosTitanic0['Embarked'].fillna(DatosTitanic0['Embarked'].mode()[0])
    DatosTitanic0.drop(['Cabin'],axis=1,inplace=True)
    DatosTitanic0['Age'] = DatosTitanic0['Age'].fillna(DatosTitanic0['Age'].mean())
    st.text('Aqui podemos ver como queda el dataframe con los nulos sustituidos:')
    st.dataframe(DatosTitanic0)

st.write("")
st.write("")
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

proces= st.sidebar.checkbox("¿Como he trabajado la tabla")
if proces:
 code2 = '''#Aqui podemos ver todo el procesamiento de los datos pare tener un dataframe listo para trabajar:
 DatosTitanic1 = DatosTitanic1.set_index(DatosTitanic1.columns[0])
 DatosTitanic1['Age'] = DatosTitanic1['Age'].astype(int)
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
 DatosTitanic1.drop('Name', axis=1, inplace=True)'''
 st.code(code2 , language='python')

final= st.sidebar.checkbox("Dataframe final")
if final:
 st.text('Aqui podemos ver como queda el dataframe que vamos a analizar:')
 st.dataframe(DatosTitanic1)



graf= st.sidebar.checkbox("Columnas principales")
if graf:
    grafico = st.selectbox('', ('Survived', 'Sex', 'Pclass', 'Age', 'Fare', 'Embarked'))
    if grafico == 'Survived':
        plt.figure(figsize=(5, 3))
        custom_colors = ['#FF1C22', '#1FFA5B']
        ax=sns.countplot(data=DatosTitanic1, x='Survived', palette=custom_colors) 
        plt.ylabel('Número de pasajeros')
        plt.xlabel('') 
        ax.set_xticklabels(['Muertos', 'Vivos'])
        st.pyplot()
        st.write(f"De los {len(DatosTitanic1['Survived'])} pasajeros totales del barco, {len(DatosTitanic1.loc[DatosTitanic1['Survived'] == 'No'])} murieron y {len(DatosTitanic1.loc[DatosTitanic1['Survived'] == 'Yes'])} sobrevivieron al naufragio.")
    elif grafico == 'Sex':
        plt.figure(figsize=(10, 6))
        custom_colors = ['#FF1C22', '#1FFA5B']
        ax1 = sns.countplot(data=DatosTitanic1, x='Sex', palette=custom_colors)
        plt.ylabel('Número de pasajeros')
        plt.xlabel('')
        ax1.set_xticklabels(['Hombres','Mujeres'])
        st.pyplot()
        st.write(f"De los {len(DatosTitanic1['Sex'])} pasajeros totales, {len(DatosTitanic1.loc[DatosTitanic1['Sex'] == 'female'])} eran mujeres y {len(DatosTitanic1.loc[DatosTitanic1['Sex'] == 'male'])} eran hombres .")    
    elif grafico == 'Pclass':
        plt.figure(figsize=(10, 6))
        color = sns.color_palette(['#1FFA5B','#F7F7FC','#FF1C22'])
        sns.countplot(data=DatosTitanic1, x='Pclass', palette=color,edgecolor='black')
        plt.ylabel('Número de pasajeros')
        plt.xlabel('Clase')
        st.pyplot()
        st.write(f"De los {len(DatosTitanic1['Pclass'])} pasajeros del Titanic, {len(DatosTitanic1.loc[DatosTitanic1['Pclass'] == 1])} viajaban en primera, {len(DatosTitanic1.loc[DatosTitanic1['Pclass'] == 2])} en segunda y {len(DatosTitanic1.loc[DatosTitanic1['Pclass'] == 3])} en trecera clase.")
    elif grafico == 'Age':
        custom_colors = ['#1FFA5B']
        sns.set_palette(custom_colors)
        plt.figure(figsize=(10, 6))
        sns.histplot(data=DatosTitanic1, x='Age', bins=10)
        plt.ylabel('Número de pasajeros')
        plt.xlabel('Edad')
        st.pyplot()
        st.write(f"La edad máxima de los pasajeros del Titanic es {DatosTitanic1['Age'].max()} años.")
        st.write(f"La edad mínima de los pasajeros del Titanic es {DatosTitanic1['Age'].min()} años.")
        st.write(f"La mediana de la edad de los pasajeros del Titanic es {DatosTitanic1['Age'].median()} años.")
    elif grafico == 'Fare':
        custom_colors = [ '#FF1C22']
        sns.set_palette(custom_colors)
        plt.figure(figsize=(10, 6))
        sns.histplot(data=DatosTitanic1, bins=15, x='Fare')
        plt.ylabel('Número de pasajeros')
        plt.xlabel('Precio billete')
        st.pyplot()
        st.write(f"El billete mas caro fue de {DatosTitanic1 ['Fare'].max()} libras.")
        st.write(f"El billete mas barato fue de {DatosTitanic1['Fare'].min()} libras.")
    else:
        plt.figure(figsize=(10, 6))
        color = sns.color_palette(['#1FFA5B','#F7F7FC','#FF1C22'])
        ax2=sns.countplot(data=DatosTitanic1, x='Embarked',  palette=color,edgecolor='black')
        plt.ylabel('Número de pasajeros')
        plt.xlabel('Puerto de embarque')
        ax2.set_xticklabels(['Southampton','Cherbourg', 'Queenstown'])
        st.pyplot() 
        st.write(f"Los pasajeros embarcados en el puerto de Southampton (Inglaterra) fueron {len(DatosTitanic1.loc[DatosTitanic1['Embarked'] == 'Southampton'])}.")
        st.write(f"Los pasajeros embarcados en el puerto de Cherbourg (Francia) fueron{len(DatosTitanic1.loc[DatosTitanic1['Embarked'] == 'Cherbourg'])}.")
        st.write(f"Los pasajeros embarcados en en el puerto de Queenstown (Irlanda) fueron {len(DatosTitanic1.loc[DatosTitanic1['Embarked'] == 'Queenstown'])}.")