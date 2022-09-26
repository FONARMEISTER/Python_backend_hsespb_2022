import pytest

from app.database import user_db
from app.auth import user_auth
from app.contracts import UserIn, User


class AuthTests:
    def test_basic_auth():
        userin = UserIn("test")
        user_id = user_auth(userin)
        user = User(userin)
        assert user_db[user_id] == user

    def test_twice_auth():
        userin1 = UserIn("user1")
        userin2 = UserIn("user2")
        user_id1 = user_auth(userin1)
        user_id2 = user_auth(userin2)
        user1 = User(userin1)
        user2 = User(userin2)
        assert len(user_db) == 2
        assert user_db[user_id1] == user1
        assert user_db[user_id2] == user2
    
        