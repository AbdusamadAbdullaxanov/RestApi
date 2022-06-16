from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Database import UserFunction
from fastapi.responses import JSONResponse

route = APIRouter(prefix='/users')


@route.post("/sign-up")
async def signup(user_data: OAuth2PasswordRequestForm = Depends()):
    user = UserFunction()
    return user.register(user_data.username, user_data.password)


@route.post("/login")
async def login(user_data: OAuth2PasswordRequestForm = Depends()):
    user = UserFunction()
    log = user.login(user_data.username, user_data.password)
    return JSONResponse(content=log)
