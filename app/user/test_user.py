import pytest

from app.user.router import buy_product, sell_product, list_of_operations
from app.contracts import User, Offer, UserIn
from app.classes import Operation
from app.database import user_db, offer_db, user_operations
from app.auth.router import user_auth
from app.shop.router import add_offer


def test_buy():
    user_db.clear()
    offer_db.clear()
    user_operations.clear()

    user_id1 = user_auth(UserIn(name='1'))
    user_id3 = user_auth(UserIn(name='3'))
    offer_id1 = add_offer(Offer(name="1", price=99))
    offer_id2 = add_offer(Offer(name="2", price=100))
    offer_id3 = add_offer(Offer(name="3", price=101))
    
    assert buy_product('10', offer_id1) != "OK"

    assert buy_product(user_id3, '20') != "OK"
    assert user_db[user_id3].balance == 100
    assert list_of_operations(user_id3) == []

    assert buy_product(user_id1, offer_id2) == "OK"
    assert user_db[user_id1].balance == 0
    assert len(list_of_operations(user_id1)) == 1

    assert buy_product(user_id1, offer_id2) != "OK"
    assert user_db[user_id1].balance == 0
    assert len(list_of_operations(user_id1)) == 1

    buy_product(user_id3, offer_id1)
    assert buy_product(user_id3, offer_id3) != "OK"
    assert user_db[user_id3].balance == 1
    assert len(list_of_operations(user_id3)) == 1


def test_sell():

    user_db.clear()
    offer_db.clear()
    user_operations.clear()

    user_id1 = user_auth(UserIn(name='1'))
    user_id3 = user_auth(UserIn(name='3'))
    offer_id1 = add_offer(Offer(name="1", price=99))
    offer_id2 = add_offer(Offer(name="2", price=100))
    offer_id3 = add_offer(Offer(name="3", price=101))

    assert sell_product('10', offer_id2) != "OK"

    assert sell_product(user_id3, '20') != "OK"
    assert user_db[user_id3].balance == 100
    assert list_of_operations(user_id3) == []

    assert sell_product(user_id1, offer_id2) == "OK"
    assert user_db[user_id1].balance == 200
    assert len(list_of_operations(user_id1)) == 1

    assert sell_product(user_id1, offer_id3) == "OK"
    assert user_db[user_id1].balance == 301
    assert len(list_of_operations(user_id1)) == 2
    
    assert sell_product(user_id3, offer_id1) == "OK"
    assert user_db[user_id3].balance == 199
    assert len(list_of_operations(user_id3)) == 1
