from fastapi import FastAPI
app = FastAPI()

@app.get("/is_even/{num}")
def even(num:float):
    if num%2 == 0:
        return{
            "message":"the number is even"
        }
    else:
        return{
            "message":"the given number is odd"
        }
    