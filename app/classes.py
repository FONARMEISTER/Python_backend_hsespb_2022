import string
import types


class Operation:
    def __init__(self, type, offer_id):
        self.type = type
        self.offer_id = offer_id
    type: string
    offer_id: str
