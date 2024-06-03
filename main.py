from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/hola")
async def hola():
    return {"message": "Hola"}

@app.get("/adios")
async def adios():
    return {"message": "Adiós"}

@app.get("/bienvenido")
async def bienvenido():
    return {"message": "Bienvenido"}
