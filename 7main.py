from fastapi import FastAPI

app = FastAPI()

@app.post("/create_user")
def create_user(name: str, age: int, collage:str,semester:int):
    return {
        "message": "user created",
        "data": {
            "name": name,
            "age": age,
            "collage": collage,
            "semester": semester
        }
    }