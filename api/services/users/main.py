from fastapi import FastAPI

app = FastAPI()
app.title = "users"
app.version = "0.0.0"


@app.get('/')
def establish_connection():
    return "users connected!"
