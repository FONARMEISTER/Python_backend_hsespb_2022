from fastapi import APIRouter

from app.contracts import User

router = APIRouter(
    prefix="/user/auth"
)


@router.get("/")
async def user_auth(user: User):
    # TODO
    return
