
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def display(num:int):
    return{
        "the number is:":num
    }