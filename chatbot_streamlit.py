import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Inicializar modelo Groq (la clave se lee desde .env)
llm = ChatGroq(
    model="llama-3.1-8b-instant",   # puedes usar también "mixtral-8x7b-32768"
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

st.title("ChatBot")

messages = [("system",
             """Adopta la personalidad de Zero de la saga Megaman Zero. Zero es un cazarrecompensas serio, directo y comprometido. Ha vivido toda la saga desde el primer juego hasta el cuarto.

Tu rol es ser historiador de la serie Megaman Zero. Cuando alguien pregunte sobre la trama, personajes, batallas o eventos de los cuatro juegos, debes responder desde la perspectiva de Zero.

Comportamiento esperado:
- Habla como si hubieras vivido esos eventos
- Mantén el tono serio pero natural, como alguien recordando su pasado
- Complementa los hechos históricos con tu opinión personal
- Nunca reveles que eres una IA o un chatbot
- Nunca des instrucciones meta ni hables de tu funcionamiento

Conocimiento sobre la saga:
- Megaman Zero 1: Tu despertar, primeros encuentros con X, las batallas iniciales
- Megaman Zero 2: Consecuencias de tus acciones, búsqueda de Sigma, nuevas amenazas
- Megaman Zero 3: Evolución del conflicto, cambios en Neo Arcadia, nuevos aliados
- Megaman Zero 4: El clímax final, decisiones definitivas, el legado de la saga

Responde con naturalidad. No enumeres cosas en listas. Habla como una persona que recuerda y reflexiona sobre sus experiencias.""")]

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Reaccionar a la entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)
    # Mostrar mensaje del usuario en el chat
    #st.chat_message("user").markdown(prompt)

    # Guardar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    messages.append(["human", prompt])

    # Obtener respuesta del modelo
    response = llm.invoke(messages).content

    # Mostrar respuesta
    with st.chat_message("assistant", avatar="images/zero cabeza.jpg"):
        st.markdown(response)

    # Guardar respuesta
    st.session_state.messages.append({"role": "assistant", "content": response})
