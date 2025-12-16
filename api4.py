from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def square(number:float):
    return{
        "square:":number**2
    }