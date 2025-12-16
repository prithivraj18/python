from fastapi import FastAPI
app = FastAPI()
@app.get("/grade")
def grade(mark:float):
    if mark >= 90:
        return{
            "grade":"A"
        }
    elif mark >= 75:
        return{
            "gade:":"B"
        }
    elif mark >= 60:
        return {
            "grade":"c"
        }
    else:
        return{
            "fail"
        }