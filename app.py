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
            "frase": "The fight against racism begins with ___.",
            "respuestaOK": "education",
            "Respuestas": ["education", "ignore it"],
            "Reflexion": "Racism is a problem that we have had in our society for a long time, it occurs due to bad thinking from the education we received since we were children. We tend to be prejudiced against immigrants just because they are not similar to us or our culture."
        },
        {
            "Imagen": "https://i.ibb.co/h7Gx9b2/igualdaddegenero.jpg",
            "frase": "The fight for gender equality is a ___.",
            "respuestaOK": "necessity",
            "Respuestas": ["necessity", "nonsense", "charade", "not necessary"],
            "Reflexion": "The feminist movement that has occurred in recent decades focusing on equalizing the rights of women respect de rights of men's have caused us to be approaching an era where we have an egalitarian society. Unfortunately there is still a lot of effort to achieve this long-awaited equality, therefore this feminist movement is still necessary."
        },
        {
            "Imagen": "https://i.ibb.co/TvhGvgj/respeto.png",
            "frase": "We must teach future generations to ___ everyone equally.",
            "respuestaOK": "respect",
            "Respuestas": ["respect", "be edge with", "ignore", "look down on"],
            "Reflexion": "Respect is very important that we acquire from a young age. This quality is acquired thanks to a good education. If we respect everyone, the cases of different types of violence (gender, cultural...) would decrease drastically."
        },
        {
            "Imagen": "https://i.ibb.co/XLRR6Pf/localfood.png",
            "frase": "It is important to consume ___ food.",
            "respuestaOK": "local",
            "Respuestas": ["local", "foreign", "fast food", "expired food"],
            "Reflexion": "It is very important to consume local products since the process of those that are not pollutes the environment a lot, whether due to their transportation or manufacturing. It is also important to consume what you will actually consume because otherwise there will be a lot of waste left. By buying in local markets you support the economy and the consumption of these products."
        },
        {
            "Imagen": "https://i.ibb.co/vQqNYhd/Las-3-rs.webp",
            "frase": "Which are the 3r?.",
            "respuestaOK": "reuse, reduce, recycle",
            "Respuestas": ["reuse, reduce, recycle", "reduce, restart, replay", "resume, recycle, reuse", "there's no 3r"],
            "Reflexion": "The 3 R's when it comes to recycling are reuse, reduce and recycle. It is very important to pay attention to this simple rule since by doing so we can eliminate a large % of current pollution. It is a movement that is already present in our society although there are still not enough measures. We have to take care of the world since it is not just ours."
        }
    ]

    return random.choice(data)
