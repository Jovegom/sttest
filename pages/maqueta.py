import os
import streamlit as st
#from langchain.llms import OpenAI

@st.cache_resource
def load_models():
    """
    Cargar los modelos generativos para generación de texto y multimodal.
    """
    return 'Respuesta modelo de texto', 'Respuesta modelo multimodal'

def get_text_response(model=None, prompt=None, config=None, stream=True):
    """
    Obtener respuesta de texto utilizando el modelo de texto.
    """
    return "Respuesta de texto del modelo de texto."

def get_vision_response(model=None, prompt_list=None, config={}, stream=True):
    """
    Obtener respuesta multimodal utilizando el modelo de visión.
    """
    return "Respuesta de imagen del modelo de multimodal."

# Inicializar modelos
st.header("Vertex AI Gemini 1.0 API")
text_model_pro, multimodal_model_pro = load_models()

# Crear pestañas
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Generar historia", "Campaña de marketing", "Imagen", "Video", "Chatbot"])

# Pestaña 1: Generar historia
with tab1:
    st.subheader("Generar una historia")
    character_name = st.text_input("Nombre del personaje:", "Mittens")
    character_type = st.text_input("Tipo de personaje:", "Gato")
    character_persona = st.text_input("Personalidad del personaje:", "Muy amigable")
    character_location = st.text_input("Ubicación del personaje:", "Galaxia de Andrómeda")
    story_premise = st.multiselect("Premisa de la historia:", ["Amor", "Aventura", "Misterio"], default=["Amor", "Aventura"])
    creative_control = st.radio("Nivel de creatividad:", ["Bajo", "Alto"], horizontal=True)
    length_of_story = st.radio("Longitud de la historia:", ["Corta", "Larga"], horizontal=True)

    # Nuevo: Añadir un selector de fecha
    publish_date = st.date_input("Fecha de publicación")

    if st.button("Generar mi historia"):
        temperature = 0.3 if creative_control == "Bajo" else 0.95
        prompt = f"""Escribe una historia {length_of_story} basada en los siguientes detalles: 
        Nombre: {character_name}
        Tipo: {character_type}
        Personalidad: {character_persona}
        Ubicación: {character_location}
        Premisa: {", ".join(story_premise)}
        Fecha de publicación: {publish_date}
        Debe incluir introducción, capítulos y conclusión."""
        config = {"temperature": 0.8, "max_output_tokens": 2048}
        with st.spinner("Generando historia..."):
            response = get_text_response(text_model_pro, prompt, config)
            st.write(response)

# Pestaña 2: Campaña de marketing
with tab2:
    st.subheader("Generar una campaña de marketing")
    product_name = st.text_input("Nombre del producto:", "ZomZoo")
    product_category = st.radio("Categoría del producto:", ["Ropa", "Electrónica", "Alimentos"], horizontal=True)
    target_audience_age = st.radio("Edad del público objetivo:", ["18-24", "25-34"], horizontal=True)
    target_audience_location = st.radio("Ubicación del público objetivo:", ["Urbana", "Suburbana"], horizontal=True)
    campaign_goal = st.multiselect("Objetivo de la campaña:", ["Aumentar la conciencia de marca", "Generar leads"], default=["Aumentar la conciencia de marca"])
    brand_voice = st.radio("Tono de la marca:", ["Formal", "Informal"], horizontal=True)
    estimated_budget = st.radio("Presupuesto estimado ($):", ["1000-5000", "5000-10000"], horizontal=True)

    # Nuevo: Añadir un campo de entrada de texto para la descripción del producto
    product_description = st.text_area("Descripción del producto")

    if st.button("Generar mi campaña"):
        prompt = f"""Genera una campaña de marketing para {product_name}, un producto de {product_category} destinado a personas de {target_audience_age} años en áreas {target_audience_location}.
        Objetivo principal: {", ".join(campaign_goal)}.
        Tono de la marca: {brand_voice}.
        Presupuesto: {estimated_budget}.
        Descripción del producto: {product_description}"""
        config = {"temperature": 0.8, "max_output_tokens": 2048}
        with st.spinner("Generando campaña..."):
            response = get_text_response(text_model_pro, prompt, config)
            st.write(response)
        
# Pestaña 3: Imagen
with tab3:
    st.subheader("Entendimiento visual")
    
    # Nuevo: Añadir un cargador de archivos para subir imágenes
    uploaded_file = st.file_uploader("Subir una imagen", type=["jpg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Imagen cargada")
        if st.button("Generar descripción de la imagen"):
            prompt = "Describe la imagen proporcionada y explica su contenido."
            with st.spinner("Generando descripción..."):
                response = get_vision_response()
                st.write(response)

# Pestaña 4: Video
with tab4:
    st.subheader("Entendimiento de video")
    st.video('https://www.youtube.com/watch?v=4hUop8jWPJE')

    # Nuevo: Añadir un selector de archivo para cargar videos locales
    uploaded_video = st.file_uploader("Subir un video", type=["mp4"])
    
    if uploaded_video is not None:
        st.video(uploaded_video)
        if st.button("Generar descripción del video"):
            prompt = "Describe el contenido del video y proporciona un resumen."
            with st.spinner("Generando descripción..."):
                response = get_vision_response()
                st.write(response)

    if st.button("Generar descripción del video en YouTube"):
        prompt = "Describe el contenido del video y proporciona un resumen."
        with st.spinner("Generando descripción..."):
            response = get_vision_response()
            st.write(response)

# Pestaña 5: Chatbot
with tab5:
    st.subheader("Chatbot")
    
    # Obtener la clave de API de OpenAI del usuario
    openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
    
    def generate_response(input_text):
        #llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        st.info('Respuesta del LLM')
    
    with st.form('chatbot_form'):
        text = st.text_area('Ingresa tu mensaje:', '¿Cómo puedo ayudarte hoy?')
        submitted = st.form_submit_button('Enviar')
        if not openai_api_key.startswith('sk-'):
            st.warning('¡Por favor ingresa tu clave de API de OpenAI!', icon='⚠')
        if submitted and openai_api_key.startswith('sk-'):
            generate_response(text)
