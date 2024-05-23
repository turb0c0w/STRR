from http import HTTPStatus
from unittest.mock import patch

from tests.unit.utils.mocks import fake_get_token_auth_header, fake_user_from_token, no_op


@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_registrations_200(client):
    rv = client.get("/registrations")
    assert rv.status_code == HTTPStatus.OK


def test_registrations_401(client):
    rv = client.get("/registrations")
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
