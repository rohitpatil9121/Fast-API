from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items(name: str = None, price: int = 0):
    return{
        "name": name,
        "price": price
    }



@app.get("items")
def get_items(name: str=None ,price: int=0):
    return{
        "price": price,
        "name": name

    }
















