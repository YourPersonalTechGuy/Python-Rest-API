from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {
        "data": 42,
        "other-data": {
            "list": [1, 2, 3, 4, 5],
        }
    }

@app.get("/user")
async def root():
    return [
        {
            "name": "John",
            "age": 20,
        },
        {
            "name": "Alvin",
            "age": 16,
        },
        {
            "name": "Jerome",
            "age": 25,
        },
        {
            "name": "Asgore",
            "age": 250,
        },
        {
            "name": "Frisk",
            "age": "Unknown",
        },
        {
            "name": "Guy from Fable",
            "age": 35,
        },
        {
            "name": "Toriel",
            "age": 240,
        },
    ]
@app.get("/todos")
async def todos():
    todos = requests.get("https://dummyjson.com/todos").json()
    # count = len(todos["todos"])
    return todos