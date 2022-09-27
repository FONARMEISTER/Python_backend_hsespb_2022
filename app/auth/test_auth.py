import pytest

from app.database import user_db
from app.auth.router import user_auth
from app.contracts import UserIn, User


def test_basic_auth():
    user_db.clear()
    userin = UserIn(name="test")
    user_id = user_auth(userin)
    user = User(name=userin.name)
    assert len(user_db) == 1
    assert user_db[user_id] == user


def test_twice_auth():
    user_db.clear()
    userin1 = UserIn(name="user1")
    userin2 = UserIn(name="user2")
    user_id1 = user_auth(userin1)
    user_id2 = user_auth(userin2)
    user1 = User(name=userin1.name)
    user2 = User(name=userin2.name)
    assert len(user_db) == 2
    assert user_db[user_id1] == user1
    assert user_db[user_id2] == user2
