import pytest
from client import search_offers
from database import db_offers


def test_service_setup():
    db_offers.append(("food", 10))
    db_offers.append(("shoes", 1000))
    db_offers.append(("car", 200000))
    db_offers.append(("food", 2))
    db_offers.append(("computer", 30000))
    db_offers.append(("shoes", 5000))


@pytest.mark.parametrize("test_input,expected", [(("food", 5, 15), 1), (("food", 1, 15), 2), (("car", 100000, 150000), 0), (("shoes", 10000, 20000), 0), (("sofa", 0, 100000000), 0)])
def test_search(test_input, expected):
    assert search_offers(test_input[0], test_input[1], test_input[2]) == expected


def test_service_shutdown():
    db_offers.clear()
