from fastapi import FastAPI
from users import route
from posts import router
from main_output import router as r
from about_us import app
from fastapi.middleware.cors import CORSMiddleware
from models import start

application = FastAPI()
application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)
application.include_router(route)
application.include_router(router)
application.include_router(r)
application.include_router(app)
start()


@application.get("/")
def hello():
    return {"msg": "hello Abdusamad! get yourself farther from Lalisa and laziness"}


if __name__ == '__main__':
    print(len(
        "create you customized application which works online! That makes sense, cause online application works with API"))
