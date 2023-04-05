from fastapi import FastAPI

app = FastAPI()
app.title = "login"
app.version = "0.0.0"


@app.get('/')
def establish_connection():
    return "login connected!"
# login will be builded at last
