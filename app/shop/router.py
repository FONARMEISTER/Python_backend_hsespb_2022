from fastapi import APIRouter

from app.contracts import Offer
from app.database import offer_db
from uuid import uuid4

router = APIRouter(
    prefix="/shop"
)


@router.post("/add")
def add_offer(offer: Offer):
    # Adds offer to database and returns its unique id
    if offer.price < 0:
        return "Wrong price"
    offer_id = str(uuid4())
    offer_db[offer_id] = offer
    return offer_id


@router.get("/list")
def list_of_offers():
    # Returns list of offers
    return offer_db
