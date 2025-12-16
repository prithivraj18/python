from fastapi import FastAPI
app = FastAPI()
@app.get("/exception")

def exception(num1:float,num2:float):
    try:
        result = num1/num2
        return{
            "result": result
        }
    except ZeroDivisionError:
        return{
            "error":"division cannot occur by zero"
        }