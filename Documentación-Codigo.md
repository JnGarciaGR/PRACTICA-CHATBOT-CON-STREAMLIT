# Explicación del Código - ChatBot Zero

¡Hola! Aquí te explico paso a paso cómo funciona este chatbot. Lo haré de forma sencilla para que entiendas cada parte.

---

## ¿Qué hace este código?

En pocas palabras: **creas un chatbot que habla como Zero de Megaman**. Puedes escribirle mensajes y él te responde usando inteligencia artificial.

---

## Las primeras líneas (Importaciones)

```python
import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
```

Aquí estamos **trayendo herramientas** que necesitamos:

- **`streamlit`** → Crea la interfaz (los botones, cuadros de texto, etc.)
- **`langchain_groq`** → Nos conecta con la IA de Groq
- **`os`** → Para leer variables del sistema
- **`dotenv`** → Para cargar la clave de API de forma segura

---

## Cargar la Clave de API

```python
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)
```

**¿Qué pasa aquí?**

1. `load_dotenv()` → Lee el archivo `.env` donde guardamos la clave de forma segura
2. `ChatGroq()` → Configura la IA
   - `model` → Elegimos cuál IA usar (la más rápida)
   - `temperature=0` → La IA siempre da respuestas consistentes (nada al azar)
   - `groq_api_key` → Le damos la clave para que se conecte

---

## El Título

```python
st.title("ChatBot")
```

Simplemente **muestra "ChatBot" grande en la pantalla**.

---

## La Personalidad del Bot

```python
messages = [("system",
             "Eres un chatbotAi útil, te llamas Zero de la saga Megaman Zero...")]
```

Aquí le **decimos a la IA cómo debe comportarse**:
- Que se llama Zero
- Que hable como el personaje
- Que no diga que es un chatbot

Es como darle instrucciones de rol.

---

## Guardar el Historial

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

**¿Qué significa esto?**

Streamlit no recuerda nada entre mensajes por defecto. Así que creamos un "guardarropas" donde guardamos todos los mensajes:

- Si es la primera vez, creamos una lista vacía
- Si ya existe, usamos la que tenemos

---

## Mostrar Mensajes Anteriores

```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

**En español:** "Para cada mensaje que hemos guardado, muéstramelo en la pantalla".

Es como releer la conversación desde el principio.

---

## Cuando el Usuario Escribe

```python
if prompt := st.chat_input("Escribe tu mensaje..."):
```

Aquí esperamos a que **el usuario escriba algo**. El `:=` es un truco de Python que significa "si el usuario escribió algo, guárdalo en `prompt`".

---

## Mostrar el Mensaje del Usuario

```python
with st.chat_message("user", avatar="🧑"):
    st.markdown(prompt)
```

**Muestra el mensaje del usuario en la pantalla** con su avatar (un emoji de persona).

---

## Guardar el Mensaje

```python
st.session_state.messages.append({"role": "user", "content": prompt})
messages.append(["human", prompt])
```

Guardamos el mensaje en **dos lugares**:

1. `st.session_state.messages` → Para mostrar en pantalla
2. `messages` → Para que la IA sepa el contexto de la conversación

---

## Obtener la Respuesta de la IA

```python
response = llm.invoke(messages).content
```

**Aquí ocurre la magia:**

Enviamos toda la conversación a la IA (`messages`) y ella nos devuelve una respuesta. Le quitamos la envoltura (`.content`) para quedarnos solo con el texto.

---

## Mostrar la Respuesta

```python
with st.chat_message("assistant", avatar="images/zero cabeza.jpg"):
    st.markdown(response)
```

**Muestra lo que dijo la IA** con el avatar de Zero.

---

## Guardar la Respuesta

```python
st.session_state.messages.append({"role": "assistant", "content": response})
```

Guardamos la respuesta de la IA para que sea parte del historial.

---

## ¿Cómo Funciona Todo Junto?

1. **Usuario escribe** → "Hola Zero, ¿cómo estás?"
2. **Lo guardamos** → En la lista de mensajes
3. **Se lo mostramos** → En pantalla
4. **Se lo enviamos a la IA** → Con todo el contexto
5. **La IA responde** → Algo como "Soy Zero. ¿Necesitas mi ayuda?"
6. **Mostramos la respuesta** → En pantalla
7. **La guardamos** → Para que la próxima respuesta sea coherente

Y el ciclo se repite infinitas veces.

---

## Conceptos Clave

| Término | Significa |
|---------|-----------|
| **Streamlit** | Librería que hace la interfaz bonita |
| **LangChain** | Librería que facilita trabajar con IA |
| **Groq** | La compañía que proporciona la IA rápida |
| **Session State** | Memoria que Streamlit mantiene durante la sesión |
| **Prompt** | Lo que el usuario escribe |
| **Response** | Lo que la IA contesta |

---

## ¿Qué Necesitas para que Funcione?

1. **Python instalado**
2. **Instalar las librerías:**
   ```bash
   pip install streamlit langchain-groq python-dotenv
   ```
3. **Una clave de API de Groq** en el archivo `.env`
4. **Ejecutar:**
   ```bash
   streamlit run chatbot_streamlit.py
   ```

---

## Notas Finales

- La conversación se **borra si actualizas la página** (eso es normal en Streamlit)
- La IA **necesita conexión a internet**
- Zero siempre responderá **como el personaje** porque se lo indicamos al principio

---

¡Eso es todo! Ahora tienes un chatbot funcionando.
