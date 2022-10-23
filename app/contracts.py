from pydantic import BaseModel


class Cake(BaseModel):
    """Contract for cake."""

    name: str
    description: str | None = None
    price: float
    amount: int
