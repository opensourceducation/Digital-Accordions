from fastapi import FastAPI

app = FastAPI()
app.title = "api_chatgpt"
app.version = "0.0.0"


@app.get('/')
def establish_connection():
    return "api_chatgpt connected!"
