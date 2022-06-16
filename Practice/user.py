from fastapi import FastAPI, Request, UploadFile, File, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import sqlite3


class Recieve(BaseModel):
    text: str
    number: int


class Database:
    def __init__(self):
        self.cursor = sqlite3.connect("New.db")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS User (txt text, number integer)""")

    def login(self, email: str):
        ls = [email]
        ret = self.cursor.execute("""SELECT * FROM User WHERE txt=?""", ls)
        return ret.fetchall()


template = Jinja2Templates(directory='templates')

app = FastAPI()


@app.get("/user/{item}")
async def random(item: str, request: Request):
    return template.TemplateResponse("home.html", {"request": request, "item": item})


@app.post("/user/posts")
async def send(request2: Request, data: str = Form(...)):
    dat = Database()
    fetch = dat.login(data)
    ret = {"request": request2, "user": str(fetch)}
    if not fetch or fetch is None:
        return {"message": "Not found account"}
    else:
        return template.TemplateResponse("home.html", ret)


if __name__ == '__main__':
    # D = Database()
    print(len("""My_love = does not exist, but I have laptop
My_friend = does not exist, But I have Python
nobody I love except Acer and Python. Cause not people but they  pay attention to my needs"""))