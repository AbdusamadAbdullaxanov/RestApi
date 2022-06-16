from pydantic import BaseModel


class TranslatorAPI(BaseModel):
    text: str
    dest: str


class Comments(BaseModel):
    comment: str
