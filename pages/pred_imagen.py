import streamlit as st
from PIL import Image
import numpy as np
from utils import predict_imagen

# Título de la aplicación
st.title('Predicción de imágenes')

# Cargar la imagen
uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])

# Si se carga una imagen
if uploaded_file is not None:
    # Mostrar la imagen
    st.write('**Vista Previa de la imagen cargada:**')
    image = Image.open(uploaded_file).resize((32, 32))
    st.image(image, caption='Imagen cargada', use_column_width=True)

    # Convertir la imagen a una matriz de valores de píxeles
    image = np.array(image) / 255.0  # Normalizar los valores de píxeles
    
    # Botón para realizar la predicción con las columnas seleccionadas
    if st.button('Realizar Predicción de la categoría de la imagen'):
        # Predecirla
        pred = predict_imagen(image)

        # Mostrar los resultados de la predicción
        st.success('Éxito al realizar la predicción!')
        st.write('La categoría predicha para la imagen:')
        st.write(pred)