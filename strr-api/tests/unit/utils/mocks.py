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
