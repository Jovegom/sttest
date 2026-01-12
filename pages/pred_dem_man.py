import streamlit as st
import pandas as pd
from utils import predict_flores
from datetime import date

# Título de la aplicación
st.title('Predicción manual de demanda')
st.image('demanda.jpg', caption='Imagen de demanda', use_column_width=True)

st.write('**Ingresa los datos manualmente para realizar la predicción de la demanda:**')

input_data = {}

# 📅 FECHA DE PREDICCIÓN
# ===============================
fecha_prediccion = st.date_input(
    "Fecha de predicción",
    value=date.today()
)

st.info(
    f"⚠️ La predicción para **{fecha_prediccion}** se realizará utilizando los datos históricos "
    "disponibles actualmente en el sistema. "
    "Si deseas mayor precisión, puedes subir un archivo CSV con datos actualizados."
)

# ===============================
# OPCIÓN DE SUBIR CSV
# ===============================
uploaded_file = st.file_uploader("Sube un CSV con datos de ventas históricas actualizadas (opcional)", type=["csv"])

if uploaded_file:
    st.success("CSV cargado correctamente. La predicción usará estos datos actualizados.")
            
# ===============================
# 💰 PRECIO DEL PRODUCTO (€)
# ===============================
input_data['precio_producto'] = st.number_input(
    'Precio del producto (€)',
    min_value=0.0,
    format="%.2f"
)

# ===============================
# 🔖 DESCUENTO (%)
# ===============================
input_data['descuento_aplicado'] = st.number_input(
    'Descuento aplicado (%)',
    min_value=0.0,
    max_value=100.0,
    format="%.1f"
)

# ===============================
# 👕 TIPO DE PRENDA
# ===============================
input_data['tipo_prenda'] = st.selectbox(
    'Tipo de prenda',
    (
        '561 urban hombre',
        '563 casual hombre',
        '582 punto mujer',
        '584 casual mujer',
        '583 basic mujer',
        '586 denim mujer',
        '562 collection mujer'
    )
)

# Sidebar
st.sidebar.header("Parámetros del usuario")

# ===============================
# 🔮 PREDICCIÓN
# ===============================
if st.button('Realizar Predicción'):
    input_df = pd.DataFrame([input_data])

    predicted_value = predict_flores(input_df)

    st.success('✅ Éxito al realizar la predicción')
    st.write('📈 **Resultado de la predicción:**', predicted_value[0])