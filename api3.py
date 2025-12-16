from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def data(name:str,age:int,city:str):
    return{
        "name":name,
        "age":age,
        "city":city 
        }
