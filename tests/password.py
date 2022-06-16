from fastapi import FastAPI, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

app = FastAPI()


@app.post("/login")
def login(info: OAuth2PasswordRequestForm = Depends()):
    print(info.username)
    print(info.password)
    return {"msg": "mmm"}
