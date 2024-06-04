from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Looking_TheWorld_API")

# Configuración de CORS para permitir todas las solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a los dominios que necesites
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/docs", status_code=308)

@app.get("/Racism")
def racism():
    data = [
        {
            "Imagen": "https://i.ibb.co/Wg4znmB/imagen-bullying-marroqui.jpg",
            "frase": "El racismo es una ___ que debemos erradicar.",
            "respuestaOK": "lacra",
            "Respuestas": ["lacra", "virtud", "alegría", "aventura"]
        },
        {
            "Imagen": "https://i.ibb.co/Wg4znmB/imagen-bullying-marroqui.jpg",
            "frase": "La discriminación racial es un ___ de odio.",
            "respuestaOK": "acto",
            "Respuestas": ["acto", "signo", "símbolo", "sonido"]
        }    
    ]

    return random.choice(data)
