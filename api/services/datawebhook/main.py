from fastapi import FastAPI

app = FastAPI()
app.title = "datawebhook"
app.version = "0.0.0"


@app.get('/')
def establish_connection():
    return "datawebhook connected!"
