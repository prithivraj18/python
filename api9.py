from fastapi import FastAPI
app = FastAPI()
@app.get("/voter")
def checker(age:int):
    if age >=18:
        return{
            "messgae":"the student is eligible to vote"
        }
    else:
        return{
            "message":"the student is not eligible to vote"
        }
    