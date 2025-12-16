from fastapi import FastAPI
app = FastAPI()

@app.get("/password")
def checker(password: str):
    word = "pass1234"
    if len(password) >= 8:
        if password == word:
            return{
                "messgae":"password is correct"
            }
        
        