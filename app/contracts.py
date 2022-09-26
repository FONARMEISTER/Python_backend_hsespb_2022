from pydantic import BaseModel


class UserIn(BaseModel):
    name: str


class User(BaseModel):
    def __init__(self, userin: UserIn):
        self.name = userin.name
        self.balance = 100
        self.operations = []
    name: str
    balance: int
    operations: list


class Offer(BaseModel):
    name: str
    price: int
