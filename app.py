from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Render FastAPI!"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to my API."}
