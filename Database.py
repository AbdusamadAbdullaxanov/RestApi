from pydantic import EmailStr
from intiate_sqlalchemy import Session
from models import start
from utils import hash_pwd, verify_pwd
from models import Users, BigMetadata, Posts
from OAuth2 import access_token
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse


class UserFunction:
    def __init__(self):
        start()
        self.session = Session()

    def register(self, email: str, password: str) -> str:
        try:
            hashed = hash_pwd(password)
            query = Users(email=email, password=hashed)
            self.session.begin()
            self.session.add(query)
            self.session.commit()
            user_id = self.session.query(Users.id).filter(Users.email == email).first()
            token = access_token(user_id[0], email, hashed)
            return token
        except:
            return f"User with {email} already exists!"

    def login(self, email: str, password: str) -> str:
        search = self.session.query(Users.password).filter(Users.email == email).first()[0]
        print(search)
        return f"You are welcome {email}!!!" if search is not None and verify_pwd(password,
                                                                                  search) else "Unauthorized account"

    def verify_user(self, email: EmailStr):
        try:
            user_id = self.session.query(Users.id).filter(Users.email == email).first()[0]
            if user_id is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Not authorized")
            return user_id
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))


class Main_output:
    def __init__(self):
        self.session = Session()
        self.session.begin()

    def search_texts(self, id: str):
        response = self.session.query(BigMetadata).filter(BigMetadata.title.like(f"%{id}%")).all()
        print(response)
        if not response:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f"Sorry, text with title {id} not found")
        return response


class Posts_base:
    def __init__(self):
        self.session = Session()
        self.session.begin()

    async def insert_post(self, txt: str, owner_id: int) -> None:
        insert = Posts(comment=txt, owner_id=owner_id)
        self.session.add(insert)
        self.session.commit()
