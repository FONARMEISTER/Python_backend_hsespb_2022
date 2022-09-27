from fastapi.testclient import TestClient
from app.main import app
from app.contracts import Offer


def test_integration():
    client = TestClient(app)
    user_id = client.post('/auth/', json={'name': 'user'}).json()
    offer_id = client.post('/shop/add', json={'name': 'offer', 'price': 70}).json()
    offer_list = client.get('/shop/list')
    assert offer_list.status_code == 200
    assert len(dict(offer_list.json())) == 1
    assert dict(offer_list.json())[offer_id] == Offer(name='offer', price=70)
    res = client.post('/user/buy', params={'user_id': user_id, 'offer_id': offer_id})
    assert res.status_code == 200
    assert res.json() == 'OK'
    res = client.post('/user/buy', params={'user_id': user_id, 'offer_id': offer_id})
    assert res.status_code == 200
    assert res.json() != 'OK'
    res = client.post('/user/sell', params={'user_id': user_id, 'offer_id': offer_id})
    assert res.status_code == 200
    assert res.json() == 'OK'
    operations = client.get('/user/operations', params={'user_id': user_id})
    assert len(operations.json()) == 2
