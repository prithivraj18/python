from fastapi import FastAPI
app = FastAPI()

@app.get("/cpr")
def compare(str1:str,str2:str):
    if str1 == str2:
        return{
            "message":"both string are equal"
        }
    else:
        return{
            "messgae":"both the string are not equal"
        }
    