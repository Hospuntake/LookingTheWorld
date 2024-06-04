from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import random

app = FastAPI(title="Looking_TheWorld_API")

@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/docs", status_code=308)

@app.get("/Racism")
def racism():
    data = [
        {
            "Imagen": "https://example.com/image1.jpg",
            "frase": "El racismo es una ___ que debemos erradicar.",
            "respuestaOK": "lacra",
            "Respuestas": ["lacra", "virtud", "alegría", "aventura"]
        },
        {
            "Imagen": "https://example.com/image2.jpg",
            "frase": "La discriminación racial es un ___ de odio.",
            "respuestaOK": "acto",
            "Respuestas": ["acto", "signo", "símbolo", "sonido"]
        },
        {
            "Imagen": "https://example.com/image3.jpg",
            "frase": "La igualdad racial debe ser un ___ en nuestra sociedad.",
            "respuestaOK": "objetivo",
            "Respuestas": ["objetivo", "problema", "desastre", "mito"]
        },
        {
            "Imagen": "https://example.com/image4.jpg",
            "frase": "La lucha contra el racismo comienza con la ___.",
            "respuestaOK": "educación",
            "Respuestas": ["educación", "ignorancia", "pereza", "destrucción"]
        },
        {
            "Imagen": "https://example.com/image5.jpg",
            "frase": "Es vital promover la ___ entre todas las razas.",
            "respuestaOK": "tolerancia",
            "Respuestas": ["tolerancia", "agresión", "intolerancia", "apatía"]
        },
        {
            "Imagen": "https://example.com/image6.jpg",
            "frase": "El racismo sistémico es una ___ compleja.",
            "respuestaOK": "problemática",
            "Respuestas": ["problemática", "solución", "comedia", "anécdota"]
        },
        {
            "Imagen": "https://example.com/image7.jpg",
            "frase": "Debemos enseñar a las futuras generaciones a ___ a todos por igual.",
            "respuestaOK": "respetar",
            "Respuestas": ["respetar", "odiar", "ignorar", "despreciar"]
        },
        {
            "Imagen": "https://example.com/image8.jpg",
            "frase": "La diversidad racial es una ___ que nos enriquece.",
            "respuestaOK": "fortaleza",
            "Respuestas": ["fortaleza", "debilidad", "enfermedad", "maldición"]
        }
    ]

    return random.choice(data)
