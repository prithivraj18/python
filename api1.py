from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def display():
    return{
        "message":"this is my first api"
    }
