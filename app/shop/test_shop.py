import pytest

from app.shop.router import add_offer, list_of_offers
from app.database import offer_db
from app.contracts import Offer


def test_basic_add_offer():
    offer_db.clear()
    offer = Offer(name="test", price=1)
    offer_id = add_offer(offer)
    assert offer_db[offer_id] == offer
    assert len(offer_db) == 1


def test_negative_price():
    offer_db.clear()
    offer = Offer(name="test", price=-1)
    offer_id = add_offer(offer)
    assert offer_id == "Wrong price"
    assert len(offer_db) == 0


def test_offer_list():
    assert list_of_offers() == {}
    offer1 = Offer(name="offer1", price=10)
    offer2 = Offer(name="offer2", price=10)
    offer_id1 = add_offer(offer1)
    assert list_of_offers() == {offer_id1: offer1}
    offer_id2 = add_offer(offer2)
    assert list_of_offers() == {offer_id1: offer1, offer_id2: offer2}
    offer_db.clear()
