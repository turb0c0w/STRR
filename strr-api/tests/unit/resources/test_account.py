import json
import os
from http import HTTPStatus
from unittest.mock import patch

from flask import g

from tests.unit.utils.mocks import (
    empty_json,
    fake_get_token_auth_header,
    fake_user_from_token,
    keycloak_profile_json,
    no_op,
)

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


@patch("strr_api.services.AuthService.create_user_account", new=empty_json)
@patch("strr_api.models.user.User.get_or_create_user_by_jwt", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_create_account_201(client):
    with open(MOCK_ACCOUNT_REQUEST) as f:
        g.jwt_oidc_token_info = None
        data = json.load(f)
        rv = client.post("/account", json=data)
        assert rv.status_code == HTTPStatus.CREATED


@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_create_account_400(client):
    rv = client.post("/account", json={})
    assert rv.status_code == HTTPStatus.BAD_REQUEST


def test_create_account_401(client):
    rv = client.post("/account", json={"name": "test"})
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
