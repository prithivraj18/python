from fastapi import FastAPI
app = FastAPI()
@app.get("/greet")
def greet(name:str):
    return{
         "hello",name
    }