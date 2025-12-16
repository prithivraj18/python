from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def s_root(num: int):
    if num > 0:
        return {
            "square_root": num ** 0.5
        }
    else:
        return {
            "error": "invalid input"
        }
