from fastapi import APIRouter

from app.database import user_db, offer_db, user_operations
from app.classes import Operation

router = APIRouter(
    prefix="/user/{user_id}"
)


@router.post("/buy/{offer_id}")
async def buy_product(user_id: str, offer_id: str):
    balance = user_db[user_id].balance
    price = offer_db[offer_id].price
    if balance < price:
        return "Not enough balance"
    balance -= price
    user_operations[user_id].append(Operation("buy", offer_id))
    user_db[user_id].balance = balance
    return "OK"


@router.post("/sell/{offer_id}")
async def sell_product(user_id: str, offer_id: str):
    balance = user_db[user_id].balance
    price = offer_db[offer_id].price
    balance += price
    user_operations[user_id].append(Operation("sell", offer_id))
    user_db[user_id].balance = balance
    return "OK"


@router.get("operations")
async def list_of_operations(user_id: str):
    return user_operations[user_id]
