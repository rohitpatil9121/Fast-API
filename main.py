from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get("/about")
def read_root():
    return {"message": "this is my about page"}
@app.get("/contact")
def read_root():
    return {"message": "this is my contact page"}
@app.get("/profile")
def read_root():
    return {"message": "this is my profile page"}
@app.get("/database")
def read_root():
    return {"message": "here is my database"}

@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id":user_id}       