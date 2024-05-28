from strr_api.models import User


def disable_jwt_requires_auth(f):
    return f


def fake_get_token_auth_header(cls):
    return "fake_jwt_token"


def fake_user_from_token(cls):
    return User(
        firstname="First",
        lastname="last",
        email="test@test.test",
    )


def keycloak_profile_json(*args, **kwargs):
    return {"keycloakGuid": "ecb1ef8f2fee443eb14a414321bbc1f2"}


def no_op(*args, **kwargs):
    None


def empty_json(*args, **kwargs):
    return {}
