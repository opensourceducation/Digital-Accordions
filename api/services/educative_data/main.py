from fastapi import FastAPI

app = FastAPI()
app.title = "educative_data"
app.version = "0.0.0"


@app.get('/')
def establish_connection():
    return "educative_data connected!"
