from fastapi import FastAPI

app = FastAPI()

# Temporary storage (acts like a database)
users = []

@app.post("/signup")
def signup(username: str, password: str):
    # Check if user already exists
    for user in users:
        if user["username"] == username:
            return {"error": "User already exists"}

    # Store user
    users.append({
        "username": username,
        "password": password
    })

    return {"message": "Signup successful"}