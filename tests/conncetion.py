from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List


class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME="Abdusamad Abdullakhanov",
    MAIL_PASSWORD="$enterpassword$",
    MAIL_FROM="pythondeveloper441@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="stmp.gmail.com",
    MAIL_FROM_NAME="Random Name",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

app = FastAPI()

html = """
<p>Hi this test mail, thanks for using Fastapi-mail</p> 
"""


@app.post("/")
async def simple_send(email: EmailSchema) -> JSONResponse:
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass
        body=html,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
