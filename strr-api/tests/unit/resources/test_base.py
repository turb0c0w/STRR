from http import HTTPStatus


def test_hello_200(client):
    rv = client.get("/hello")
    assert rv.status_code == HTTPStatus.OK


def test_goobye_200(client):
    rv = client.post("/goodbye", json={"message": "goodbye"})
    assert rv.status_code == HTTPStatus.OK


def test_goobye_400(client):
    rv = client.post("/goodbye", json={})
    assert rv.status_code == HTTPStatus.BAD_REQUEST


def test_me_200(client):
    rv = client.get("/me")
    assert rv.status_code == HTTPStatus.OK


def test_me_401(client):
    rv = client.get("/me")
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
