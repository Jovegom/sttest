import streamlit as st
import pandas as pd
from utils import predict_flores
from datetime import date

# Título de la aplicación
st.title('Predicción manual de demanda')
st.image('demanda.jpg', caption='Imagen de demanda', use_column_width=True)

st.write('**Ingresa los datos manualmente para realizar la predicción de la demanda:**')

input_data = {}

# ===============================
# 📈 VENTAS HISTÓRICAS (mínimo 5)
# ===============================
st.subheader("Ventas históricas (mínimo 5 registros)")

ventas = []
fechas = []

for i in range(5):
    col1, col2 = st.columns(2)

    with col1:
        venta = st.number_input(
            f'Ventas #{i+1}',
            min_value=0,
            step=1,
            key=f'venta_{i}'
        )

    with col2:
        fecha = st.date_input(
            f'Fecha venta #{i+1}',
            value=date.today(),
            key=f'fecha_{i}'
        )

    ventas.append(venta)
    fechas.append(fecha)

input_data['ventas_historicas'] = ventas
input_data['fechas_ventas'] = fechas

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