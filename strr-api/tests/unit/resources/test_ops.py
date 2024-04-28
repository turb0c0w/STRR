from http import HTTPStatus


def test_healthz_200(client):
    rv = client.get('/ops/healthz')
    assert rv.status_code == HTTPStatus.OK


def test_readyz_200(client):
    rv = client.get('/ops/readyz')
    assert rv.status_code == HTTPStatus.OK
