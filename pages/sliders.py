#importamos lo necesario
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split,RandomizedSearchCV
from sklearn.metrics import *
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestCentroid
import pickle

with open('models/model_wine.pkl', 'rb') as file:
    model = pickle.load(file)

with open('models/scaler.pkl', 'rb') as file:
    scaler_X = pickle.load(file)

with open('models/1hot.pkl', 'rb') as file:
    preprocessor = pickle.load(file)

df=load_wine(as_frame=True)
df=df.frame
##################################################
st.title("Predicción del tipo de vino")
st.sidebar.header("Parametros del usuario")
alcohol=st.sidebar.slider("acido malico",df['malic_acid'].min(),df['malic_acid'].max(),df['malic_acid'].mean())
malic_acid=st.sidebar.slider("alcohol",df['alcohol'].min(),df['alcohol'].max(),df['alcohol'].mean())
ash=st.sidebar.slider("ash",df['ash'].min(),df['ash'].max(),df['ash'].mean())
alcalinity_of_ash=st.sidebar.slider("alcalinidad de ash",df['alcalinity_of_ash'].min(),df['alcalinity_of_ash'].max(),df['alcalinity_of_ash'].mean())
magnesium=st.sidebar.slider("magnesio",df['magnesium'].min(),df['magnesium'].max(),df['magnesium'].mean())
total_phenols=st.sidebar.slider("phenoles totales",df['total_phenols'].min(),df['total_phenols'].max(),df['total_phenols'].mean())
flavanoids=st.sidebar.slider("flavanoides",df['flavanoids'].min(),df['flavanoids'].max(),df['flavanoids'].mean())
nonflavanoid_phenols=st.sidebar.slider("nonflavanoid_phenols",df['nonflavanoid_phenols'].min(),df['nonflavanoid_phenols'].max(),df['nonflavanoid_phenols'].mean())
proanthocyanins=st.sidebar.slider("proanthocyanins",df['proanthocyanins'].min(),df['proanthocyanins'].max(),df['proanthocyanins'].mean())
color_intensity=st.sidebar.slider("intensidad del color",df['color_intensity'].min(),df['color_intensity'].max(),df['color_intensity'].mean())
hue=st.sidebar.slider("hue",df['hue'].min(),df['hue'].max(),df['hue'].mean())
od=st.sidebar.slider("diluted wines",df['od280/od315_of_diluted_wines'].min(),df['od280/od315_of_diluted_wines'].max(),df['od280/od315_of_diluted_wines'].mean())
proline=st.sidebar.slider("proline",df['proline'].min(),df['proline'].max(),df['proline'].mean())

data={
    'alcohol':malic_acid,
    'malic_acid':alcohol, 
    'ash':ash,
    'alcalinity_of_ash':alcalinity_of_ash,
    'magnesium':magnesium,
    'total_phenols':total_phenols,
    'flavanoids':flavanoids,
    'nonflavanoid_phenols':nonflavanoid_phenols,
    'proanthocyanins':proanthocyanins,
    'color_intensity':color_intensity,
    'hue':hue,
    'od280/od315_of_diluted_wines':od, 
    'proline':proline,
}
features=pd.DataFrame(data,index=[0])
st.write("Confirmación de los datos introducidos por el usuario:")
st.write(features)

#################
st.header("Vistazo general del conjunto de datos")
st.write(df.head(3))
#Escalado de características
features_sc=scaler_X.transform(features)
##########################
#Realizar las predicciones
predicciones=model.predict(features_sc)
st.header("Prediccion del modelo:")
st.write(predicciones)

##########################1-hot encoder#############################
# Crear un DataFrame de ejemplo
data_user = {
    'edad': [25],
    'ciudad': ['Madrid'],
    'ingresos': [50000],
    'genero': ['M']
}

df_ex_user = pd.DataFrame(data_user)

st.write(df_ex_user)

# Aplicar la transformación
X_transformed_u = preprocessor.transform(df_ex_user)

# Convertir el resultado a un DataFrame para mejor visualización (opcional)
X_transformed_df_u = pd.DataFrame(X_transformed_u, columns=preprocessor.get_feature_names_out())

st.write(X_transformed_df_u)

