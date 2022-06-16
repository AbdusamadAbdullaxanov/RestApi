from fastapi import APIRouter, Depends, HTTPException, status
from OAuth2 import get_current_user_id
from Database import Posts_base
from Schemas import Comments

router = APIRouter(prefix='/posts')


@router.get("/Intro")
async def introduction():
    return {"message": "This is comment section"}


@router.post("/comment")
async def comment(comment_txt: Comments, user_id: int = Depends(get_current_user_id)):
    insert = Posts_base()
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
    await insert.insert_post(comment_txt.comment, user_id)
    return f"{user_id}: {comment_txt.comment}"
