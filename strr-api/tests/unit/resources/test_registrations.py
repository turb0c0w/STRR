import json
import os
from http import HTTPStatus
from unittest.mock import patch

from flask import g

from tests.unit.utils.mocks import (
    fake_document,
    fake_get_token_auth_header,
    fake_registration,
    fake_user_from_token,
    no_op,
)

REGISTRATION = "registration_use_sbc_account"
REGISTRATION_MINIMUM_FIELDS = "registration_use_sbc_account_minimum"
MOCK_ACCOUNT_REQUEST = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), f"../../mocks/json/{REGISTRATION}.json"
)
MOCK_ACCOUNT_MINIMUM_FIELDS_REQUEST = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), f"../../mocks/json/{REGISTRATION_MINIMUM_FIELDS}.json"
)
MOCK_DOCUMENT_UPLOAD = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../mocks/file/document_upload.txt")


@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_get_registrations_200(client):
    g.jwt_oidc_token_info = None
    rv = client.get("/registrations")
    assert rv.status_code == HTTPStatus.OK


def test_get_registrations_401(client):
    rv = client.get("/registrations")
    assert rv.status_code == HTTPStatus.UNAUTHORIZED


@patch("strr_api.models.user.User.get_or_create_user_by_jwt", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_post_registrations_201(client):
    with open(MOCK_ACCOUNT_REQUEST) as f:
        g.jwt_oidc_token_info = None
        data = json.load(f)
        rv = client.post("/registrations", json=data)
        assert rv.status_code == HTTPStatus.CREATED


@patch("strr_api.models.user.User.get_or_create_user_by_jwt", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_post_registrations_minimum_fields_201(client):
    with open(MOCK_ACCOUNT_MINIMUM_FIELDS_REQUEST) as f:
        g.jwt_oidc_token_info = None
        data = json.load(f)
        rv = client.post("/registrations", json=data)
        assert rv.status_code == HTTPStatus.CREATED


@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_post_registrations_400(client):
    rv = client.post("/registrations", json={})
    assert rv.status_code == HTTPStatus.BAD_REQUEST


def test_post_registrations_401(client):
    rv = client.post("/registrations", json={"name": "test"})
    assert rv.status_code == HTTPStatus.UNAUTHORIZED


@patch("strr_api.services.registration_service.RegistrationService.get_registration", new=fake_registration)
@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_get_registration_documents_200(client):
    rv = client.get("/registrations/1/documents")
    assert rv.status_code == HTTPStatus.OK


def test_get_registration_documents_401(client):
    rv = client.get("/registrations/1/documents")
    assert rv.status_code == HTTPStatus.UNAUTHORIZED


@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_get_registration_documents_403(client):
    rv = client.get("/registrations/1/documents")
    assert rv.status_code == HTTPStatus.FORBIDDEN


@patch("strr_api.services.registration_service.RegistrationService.save_registration_document", new=fake_document)
@patch("strr_api.services.registration_service.RegistrationService.get_registration", new=fake_registration)
@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_post_registration_documents_201(client):
    with open(MOCK_ACCOUNT_REQUEST, "rb") as f:
        data = {"file": (f, MOCK_DOCUMENT_UPLOAD)}
        rv = client.post("/registrations/1/documents", content_type="multipart/form-data", data=data)
        assert rv.status_code == HTTPStatus.CREATED


@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_post_registration_documents_400(client):
    rv = client.post("/registrations/1/documents", content_type="multipart/form-data", data={})
    assert rv.status_code == HTTPStatus.BAD_REQUEST


def test_post_registration_documents_401(client):
    with open(MOCK_ACCOUNT_REQUEST, "rb") as f:
        data = {"file": (f, MOCK_DOCUMENT_UPLOAD)}
        rv = client.post("/registrations/1/documents", content_type="multipart/form-data", data=data)
        assert rv.status_code == HTTPStatus.UNAUTHORIZED


@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_post_registration_documents_403(client):
    with open(MOCK_ACCOUNT_REQUEST, "rb") as f:
        data = {"file": (f, MOCK_DOCUMENT_UPLOAD)}
        rv = client.post("/registrations/1/documents", content_type="multipart/form-data", data=data)
        assert rv.status_code == HTTPStatus.FORBIDDEN


@patch("strr_api.services.registration_service.RegistrationService.get_registration", new=fake_registration)
@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_delete_registration_documents_204(client):
    rv = client.delete("/registrations/1/documents/1")
    assert rv.status_code == HTTPStatus.NO_CONTENT


def test_delete_registration_documents_401(client):
    rv = client.delete("/registrations/1/documents/1")
    assert rv.status_code == HTTPStatus.UNAUTHORIZED


@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_delete_registration_documents_403(client):
    rv = client.delete("/registrations/1/documents/1")
    assert rv.status_code == HTTPStatus.FORBIDDEN


@patch("strr_api.services.registration_service.RegistrationService.get_registration_document", new=fake_document)
@patch("strr_api.services.registration_service.RegistrationService.get_registration", new=fake_registration)
@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_get_registration_document_200(client):
    rv = client.get("/registrations/1/documents/1")
    assert rv.status_code == HTTPStatus.OK


def test_get_registration_document_401(client):
    rv = client.get("/registrations/1/documents/1")
    assert rv.status_code == HTTPStatus.UNAUTHORIZED


@patch("strr_api.models.user.User.find_by_jwt_token", new=fake_user_from_token)
@patch("flask_jwt_oidc.JwtManager.get_token_auth_header", new=fake_get_token_auth_header)
@patch("flask_jwt_oidc.JwtManager._validate_token", new=no_op)
def test_get_registration_document_403(client):
    rv = client.get("/registrations/1/documents/1")
    assert rv.status_code == HTTPStatus.FORBIDDEN
