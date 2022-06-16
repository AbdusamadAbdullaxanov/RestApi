from fastapi.responses import JSONResponse
from fastapi import APIRouter
from Database import Main_output
from fastapi.templating import Jinja2Templates

router = APIRouter()
template = Jinja2Templates(directory="templates")


@router.get("/search/{id}", response_class=JSONResponse)
async def search_texts(id: str):
    obj = Main_output()
    return obj.search_texts(id)
