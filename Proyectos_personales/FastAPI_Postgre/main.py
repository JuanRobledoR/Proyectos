from fastapi import FastAPI
from model.UserConnection import UserConnection

app = FastAPI()
conn = UserConnection()

@app.get("/")
def root():
    conn
    return "Hola que tal"