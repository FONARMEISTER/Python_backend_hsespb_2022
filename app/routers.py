from turtle import pu
from fastapi import APIRouter

import contracts

router = APIRouter()


@router.get("/")
def read_root():
    return "Welcome to our bakery!"


@router.get("/cakes/{cake_name}")
async def cake_item(cake_name: str):
    return {"cake_name": cake_name}


@router.get("/users/")
async def read_user(user_id: str, name: str | None = None):
    if name == "Oleg":
        return "Do not service Olegs!"
    return {"item_id": user_id, "name" : name}


@router.get("/users/{user_id}/cakes/{cake_name}")
async def sell_cake_to_user(
    user_id: int, cake_name: str, wishes: str | None = None
):
    purchase = {"cake_name": cake_name, "owner_id": user_id}
    if wishes and "tasty" in wishes:
        purchase.update({"bonus_info": "tasty"})
    else:
        purchase.update({"bonus_info": "default"})
    return purchase


@router.post("/cakes/")
async def deliver_cake(cake: contracts.Cake):
    cake_dict = cake.dict()

    if cake.amount == 0:
        return "You cannot deliver 0 cakes to us!"
    if cake.price <= 0:
        return "It's disadvantageous!"
    new_price = cake.price * 1.1  #resale!
    cake_dict.update({"price": new_price})
    return cake_dict
