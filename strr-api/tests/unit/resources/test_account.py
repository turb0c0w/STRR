import json
from http import HTTPStatus
from unittest.mock import patch

from flask import g

from tests.unit.utils.mocks import (
    empty_json,
    fake_get_token_auth_header,
    fake_user_from_db,
    fake_user_from_token,
    keycloak_profile_json,
    mock_json_file,
    new_sbc_account,
    no_op,
)

MOCK_ACCOUNT_REQUEST = mock_json_file("new_sbc_account")
MOCK_PATCH_ACCOUNT_REQUEST = mock_json_file("patch_account_tos")


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


@patch("strr_api.services.RegistrationService.get_or_create_user", new=fake_user_from_db)
@patch("strr_api.services.AuthService.update_user_tos", new=no_op)
@patch("strr_api.services.AuthService.create_user_account", new=new_sbc_account)
@patch("strr_api.services.AuthService.add_contact_info", new=no_op)
@patch("strr_api.models.user.User.get_or_create_user_by_jwt", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_post_account_sbc_201(client):
    with open(MOCK_ACCOUNT_REQUEST) as f:
        g.jwt_oidc_token_info = None
        data = json.load(f)
        rv = client.post("/account/sbc", json=data)
        assert rv.status_code == HTTPStatus.CREATED


@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_post_account_sbc_400(client):
    rv = client.post("/account/sbc", json={})
    assert rv.status_code == HTTPStatus.BAD_REQUEST


def test_post_account_sbc_401(client):
    rv = client.post("/account/sbc", json={"name": "test"})
    assert rv.status_code == HTTPStatus.UNAUTHORIZED


@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_db)
@patch("strr_api.services.AuthService.update_user_tos", new=no_op)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_patch_account_200(client):
    with open(MOCK_PATCH_ACCOUNT_REQUEST) as f:
        g.jwt_oidc_token_info = None
        data = json.load(f)
        rv = client.patch("/account", json=data)
        assert rv.status_code == HTTPStatus.OK


@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_patch_account_400(client):
    rv = client.post("/account/sbc", json={})
    assert rv.status_code == HTTPStatus.BAD_REQUEST


def test_patch_account_401(client):
    rv = client.post("/account/sbc", json={"name": "test"})
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
