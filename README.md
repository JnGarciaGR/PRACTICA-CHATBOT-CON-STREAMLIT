# ChatBot Zero - MegaMan

Chatbot basado en la inteligencia artificial usando Streamlit y LangChain, con la personalidad de Zero de la saga Megaman.

## Características

- Chatbot interactivo con IA generativa (Groq API)
- Interfaz amigable con Streamlit
- Avatar personalizado con imagen de Zero
- Historial de conversación persistente

## Requisitos

- Python 3.8+
- Streamlit
- LangChain
- Groq API Key

## Instalación

```bash
pip install streamlit langchain-groq python-dotenv
```

## Uso

```bash
streamlit run chatbot_streamlit.py
```

## Estructura del Proyecto

```
CHATBOT/
├── chatbot_streamlit.py  # Archivo principal de la aplicación
├── .env                  # Variables de entorno (NO COMMIT)
├── images/               # Carpeta con imágenes
│   ├── zero cabeza.jpg   # Avatar del chatbot
│   └── images.jpg        # Imagen adicional
├── .gitignore            # Archivos a ignorar en git
└── README.md             # Este archivo
```

## Configuración

1. Copia tu clave de API de Groq en el archivo `.env`:

```env
GROQ_API_KEY=tu_clave_aqui
```

2. Instala las dependencias con `python-dotenv`:

```bash
pip install python-dotenv
```

