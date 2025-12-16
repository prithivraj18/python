from fastapi import FastAPI
app = FastAPI()

@app.get("/len_str/")
def lenght_string(word:str):
    return{
        "the lenght of the word is:":len(word)
    }