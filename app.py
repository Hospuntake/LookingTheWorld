from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(title="api PA SABER KLK")

@app.get("/",include_in_schema=False)
def index():
    return RedirectResponse("/docs",status_code=308)

@app.get("/hola")
def hola():
    return {"message": "Hola"}
