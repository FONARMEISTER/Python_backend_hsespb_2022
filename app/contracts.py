from pydantic import BaseModel


class User(BaseModel):
    name: str
    balance: int


class Offer(BaseModel):
    name: str
    price: int
    offer_id: int
