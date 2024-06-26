from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Looking_TheWorld_API")

# Configuración de CORS para permitir todas las solicitudes desde cualquier origen
# Configuración básica permitiendo todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Datos de las preguntas
data = [
    {
        "Imagen": "https://i.ibb.co/Wg4znmB/imagen-bullying-marroqui.jpg",
        "NombreImagen": "imagen-bullying-marroqui.png",
        "frase": "The fight against racism begins with ___.",
        "respuestaOK": "Education",
        "Respuestas": ["Education", "Ignore it", "Been passive", "Be racist"],
        "Reflexion": "Racism is a problem that we have had in our society for a long time. It occurs due to bad thinking from the education we received since we were children. We tend to be prejudiced against immigrants just because they are not similar to us or our culture."
    },
    {
        "Imagen": "https://i.ibb.co/h7Gx9b2/igualdaddegenero.jpg",
        "NombreImagen": "igualdaddegenero.jpg",
        "frase": "The fight for gender equality is a ___.",
        "respuestaOK": "Necessity",
        "Respuestas": ["Necessity", "Nonsense", "Charade", "Not necessary"],
        "Reflexion": "The feminist movement that has occurred in recent decades focusing on equalizing the rights of women respect the rights of men has brought us closer to an era where we have an egalitarian society. Unfortunately, there is still a lot of effort needed to achieve this long-awaited equality; therefore, this feminist movement is still necessary."
    },
    {
        "Imagen": "https://i.ibb.co/TvhGvgj/respeto.jpg",
        "NombreImagen": "respeto.png",
        "frase": "We must teach future generations to ___ everyone equally.",
        "respuestaOK": "Respect",
        "Respuestas": ["Respect", "Re edge with", "Rgnore", "Look down on"],
        "Reflexion": "Respect is very important to acquire from a young age. This quality is acquired thanks to a good education. If we respect everyone, the cases of different types of violence (gender, cultural...) would decrease drastically."
    },
    {
        "Imagen": "https://i.ibb.co/XLRR6Pf/localfood.jpg",
        "NombreImagen": "localfood.png",
        "frase": "It is important to consume ___ food.",
        "respuestaOK": "Local",
        "Respuestas": ["Local", "Foreign", "Fast food", "Expired food"],
        "Reflexion": "It is very important to consume local products since the process of those that are not pollutes the environment a lot, whether due to their transportation or manufacturing. It is also important to consume what you will actually consume because otherwise, there will be a lot of waste left. By buying in local markets you support the economy and the consumption of these products."
    },
    {
        "Imagen": "https://i.ibb.co/vQqNYhd/Las-3-rs.jpg",
        "NombreImagen": "Las-3-rs.png",
        "frase": "Which are the 3r?.",
        "respuestaOK": "Reuse, Reduce, Recycle",
        "Respuestas": ["Reuse, Reduce, Recycle", "Reduce, Restart, Replay", "Resume, Recycle, Reuse", "There's no 3r"],
        "Reflexion": "The 3 R's when it comes to recycling are reuse, reduce, and recycle. It is very important to pay attention to this simple rule since by doing so we can eliminate a large percentage of current pollution. It is a movement that is already present in our society, although there are still not enough measures. We have to take care of the world since it is not just ours."
    },
    {
        "Imagen": "https://i.ibb.co/Zdfb0PB/VIOLENCIA.jpg",
        "NombreImagen": "VIOLENCIA.png",
        "frase": "Is it the same conflict and violence?",
        "respuestaOK": "No",
        "Respuestas": ["Yes", "No"],
        "Reflexion": "It's not the same. If violence occurs there will always be a conflict previously, but it's not necessary for violence to always precede a conflict. Conflicts happen every day; you need to know how to solve them without violence."
    },
    {
        "Imagen": "https://i.ibb.co/vZw1hfq/4-estaciones.jpg",
        "NombreImagen": "4-estaciones.png",
        "frase": "It is important to respect the 4 seasons of fruit/vegetables",
        "respuestaOK": "Yes",
        "Respuestas": ["Yes", "No"],
        "Reflexion": "It is important to respect the different seasons regarding fruits and vegetables for a simple reason. When you eat food that is not in season, that food comes from facilities that send to different supermarkets. Storing all that food is already quite polluting, but it is not only the storage but also the transportation."
    },
    {
        "Imagen": "https://i.ibb.co/KDw9S3Q/pegar.jpg",
        "NombreImagen": "pegar.png",
        "frase": "You see a man hit a woman in the middle of the street and there is no one else besides you. Do you also suspect that the man has a weapon, how should you act?",
        "respuestaOK": "Report the situation to the police through 016 or ask for help at 112 emergencies",
        "Respuestas": ["Report the situation to the police through 016 or ask for help at 112 emergencies", "Run away", "Hit the man", "Start screaming"],
        "Reflexion": "This situation is very complicated and at the same time dangerous, as it is a situation where there are no other people and you can suspect that the individual is carrying a weapon. It is best to call the authorities and have them take charge, always being careful to maintain a safe distance. Unfortunately, these events continue to occur in our society, and some unexpected day you"
    }
]

current_question_index = 0  # Índice de la pregunta actual

@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/docs", status_code=308)

@app.get("/Racism")
def racism():
    global current_question_index  # Accede a la variable global current_question_index
    question = data[current_question_index]  # Obtiene la pregunta actual

    current_question_index = (current_question_index + 1) % len(data)  # Incrementa el índice de la pregunta, volviendo a cero si llega al final de la lista

    return question
