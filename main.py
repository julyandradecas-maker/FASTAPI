from fastapi import FastAPI
from sqlmodel import SQLModel

app = FastAPI()


class User(SQLModel):
    username: str
    password: str


db_users = [
    User(username="admin", password="admin"),
    User(username="user", password="user"),
    User(username="guest", password="guest"),
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login")
def login(user: User):
    for db_user in db_users:
        if db_user.username == user.username and db_user.password == user.password:
            return {"success": True, "message": f"Bienvenido, {user.username}"}
        else:
           return {"success": False, "message": "Usuario o contraseña incorrectos"}
