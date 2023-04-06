from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime, timedelta
import uvicorn

app = FastAPI()
app.title = "login"
app.version = "0.0.0"


# OAuth2 config
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# JWT config
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class ClientCredentials(BaseModel):
    client_id: str
    client_secret: str


VALID_CLIENT_CREDENTIALS = {
    "client_id": "example_id",
    "client_secret": "example_secret",
}


def validate_client_credentials(credentials: ClientCredentials):
    if (
        credentials.client_id == VALID_CLIENT_CREDENTIALS["client_id"]
        and credentials.client_secret == VALID_CLIENT_CREDENTIALS["client_secret"]
    ):
        return True
    return False


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/token")
async def generate_token(credentials: ClientCredentials):
    if not validate_client_credentials(credentials):
        raise HTTPException(
            status_code=400, detail="Invalid client credentials")

    access_token = create_access_token({"sub": credentials.client_id})
    return {"access_token": access_token, "token_type": "bearer"}


async def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        client_id = payload.get("sub")
        if client_id is None:
            raise HTTPException(status_code=400, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")

    return client_id


@app.get("/protected-resource")
async def access_protected_resource(current_client_id: str = Depends(verify_token)):
    return {"message": f"Hello, client {current_client_id}!"}


@app.get('/')
def establish_connection():
    return "login connected!"
