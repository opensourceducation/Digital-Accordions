from fastapi import FastAPI

app = FastAPI()
app.title = "no_sql_controller"
app.version = "0.0.0"


@app.get('/')
def establish_connection():
    return "no_sql_controller connected!"
