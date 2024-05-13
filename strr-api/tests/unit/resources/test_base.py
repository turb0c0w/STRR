from http import HTTPStatus
from unittest.mock import patch

from strr_api.common.auth import jwt
from strr_api.services.auth_service import AuthService


def disable_jwt_requires_auth(f):
    return f


def fake_get_token_auth_header(cls):
    return "fake_jwt_token"


def keycloak_profile_json(*args, **kwargs):
    return {"keycloakGuid": "ecb1ef8f2fee443eb14a414321bbc1f2"}


def no_op(*args, **kwargs):
    None


def empty_json(*args, **kwargs):
    return {}


@patch("strr_api.services.AuthService.get_user_profile", new=keycloak_profile_json)
@patch("strr_api.services.AuthService.get_user_settings", new=empty_json)
@patch("strr_api.services.AuthService.get_user_accounts", new=empty_json)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_me_200(client):
    rv = client.get("/me")
    assert rv.status_code == HTTPStatus.OK


@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_me_502(client):
    rv = client.get("/me")
    assert rv.status_code == HTTPStatus.BAD_GATEWAY


def test_me_401(client):
    rv = client.get("/me")
    assert rv.status_code == HTTPStatus.UNAUTHORIZED


# def test_create_account_200(client):
#     rv = client.post("/create_account", json={"message": "goodbye"})
#     assert rv.status_code == HTTPStatus.OK


# def test_create_account_401(client):
#     rv = client.post("/create_account", json={})
#     assert rv.status_code == HTTPStatus.BAD_REQUEST


@patch("strr_api.services.AuthService.get_service_client_token", new=no_op)
@patch("strr_api.services.PayService.get_fee_codes", new=empty_json)
def test_fee_codes_200(client):
    rv = client.get("/fee_codes")
    assert rv.status_code == HTTPStatus.OK
