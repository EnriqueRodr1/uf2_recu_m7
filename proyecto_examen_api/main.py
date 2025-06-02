from fastapi import FastAPI
from services import user
from services.user import tabla_users

app = FastAPI()
tabla_users()  # Crear tabla si no existe

@app.get("/")
def root():
    return {"msg": "API en funcionamiento"}

@app.get("/usuarios/get", response_model= list[dict])
async def find_users():
    result = user.getusuarios()
    return result

@app.post(path="/users/post", response_model=dict)
async def insert_user(name: str, surname: str):
    result = user.postusuario(name, surname)
    return result

@app.put(path="/users/put", response_model=dict)
async def update_user(user_id: int, name: str, surname: str):
    result = user.putusuario(user_id, name, surname)
    return result

@app.delete(path="/users/delete", response_model=dict)
async def delete_user(user_id: int):
    result = user.deleteusuario(user_id)
    return result
