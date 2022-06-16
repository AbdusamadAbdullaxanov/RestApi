from fastapi import APIRouter, HTTPException, status
from googletrans import Translator
from Schemas import TranslatorAPI

apirouter = APIRouter(prefix='/utils')
content = Translator()


@apirouter.post("/translator")
def translate_txt(data: TranslatorAPI) -> str:
    try:
        translated = content.translate(**data.dict()).text
        return translated
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))
