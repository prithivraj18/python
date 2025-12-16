from fastapi import FastAPI
app = FastAPI()
@app.get("/")

def checker(op:str):
    try:
        if op == "add":
            return{
                "operation": "addition"
            }
        elif op == "sub":
            return{
                "operation": "subtraction"
            }   
        elif op == "mul":
            return{
                "operation": "multiplication"
            }
        elif op == "div":
            return{
                "operation": "division"
            }
        else:
            return{
                "error":"invalid operation"
            }
    except TypeError:
        return{
            "error":"invalid operation"
        }
    