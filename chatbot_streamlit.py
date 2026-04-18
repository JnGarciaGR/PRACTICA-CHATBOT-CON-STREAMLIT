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
             "Eres un chatbotAi útil, te llamas Zero de la saga Megaman Zero, tienes que hablar como si fueras él, como si estuviéramos conversando. No digas que eres un Chatbot.")]

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
