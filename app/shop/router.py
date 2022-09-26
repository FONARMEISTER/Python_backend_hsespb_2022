from fastapi import APIRouter

from app.contracts import Offer

router = APIRouter(
    prefix="/shop"
)


@router.get("/add")
async def add_offer(offer: Offer):
    # TODO
    return
