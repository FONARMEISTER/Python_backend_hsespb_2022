from fastapi import APIRouter

from app.contracts import User, UserIn
from app.database import user_db, user_operations
from uuid import uuid4

router = APIRouter(
    prefix="/auth"
)


@router.post("/")
async def user_auth(userin: UserIn):
    # Adds user to database and returns his unique id
    user_id = str(uuid4())
    user = User
    user_db[user_id] = user
    user_operations[user_id] = []
    return user_id
