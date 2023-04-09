from fastapi import FastAPI

app = FastAPI()
app.title = "educative_data"
app.version = "0.0.0"


@app.get('/')
def establish_connection():
    return "educative_data connected!"


@app.post('/create')
def create_educative_data():
    return "educative_data created!"
