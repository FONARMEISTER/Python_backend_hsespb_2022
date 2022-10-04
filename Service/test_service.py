import pytest
from unittest.mock import patch
from client import search_offers
import database

@pytest.mark.parametrize("test_input,expected", [(("food", 5, 15), 1), (("food", 1, 15), 2), (("car", 100000, 150000), 0), (("shoes", 10000, 20000), 0), (("sofa", 0, 100000000), 0)])
def test_search(test_input, expected):
    with patch.object(database, 'db_offers', [("shoes", 5000), ("computer", 30000), ("food", 2), ("car", 200000), ("shoes", 1000), ("food", 10)]):
        print(database.db_offers)
        assert search_offers(test_input[0], test_input[1], test_input[2]) == expected
        print(0)