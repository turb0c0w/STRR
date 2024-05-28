import os
from http import HTTPStatus
from unittest.mock import patch

from tests.unit.utils.mocks import empty_json, fake_get_token_auth_header, keycloak_profile_json, no_op

REGISTRATION = "registration_new_sbc_account"
MOCK_ACCOUNT_REQUEST = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), f"../../mocks/json/{REGISTRATION}.json"
)


@patch("strr_api.services.AuthService.get_user_profile", new=keycloak_profile_json)
@patch("strr_api.services.AuthService.get_user_settings", new=empty_json)
@patch("strr_api.services.AuthService.get_user_accounts", new=empty_json)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_me_200(client):
    rv = client.get("/account/me")
    assert rv.status_code == HTTPStatus.OK


@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_me_502(client):
    rv = client.get("/account/me")
    assert rv.status_code == HTTPStatus.BAD_GATEWAY


def test_me_401(client):
    rv = client.get("/account/me")
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
