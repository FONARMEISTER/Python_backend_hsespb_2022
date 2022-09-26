from pydantic import BaseModel


class UserIn(BaseModel):
    name: str


class User(BaseModel):
    name: str
    balance: int = 100


class Offer(BaseModel):
    name: str
    price: int
