from strr_api.models import Document, Eligibility, Registration, User


def disable_jwt_requires_auth(f):
    return f


def fake_get_token_auth_header(arg):
    return "fake_jwt_token"


def fake_user_from_token(arg):
    return User(
        firstname="First",
        lastname="last",
        email="test@test.test",
        idp_userid="ABCDEFG",
    )


def fake_user_from_db(*args, **kwargs):
    return User(
        id=1,
        firstname="First",
        lastname="last",
        email="test@test.test",
        idp_userid="ABCDEFG",
    )


def fake_registration(token, registration_id):
    return Registration(
        id=registration_id,
        user_id=1,
        sbc_account_id="sbc",
        eligibility=Eligibility(id=1, registration_id=registration_id),
    )


def fake_document(*args, **kwargs):
    return Document(
        id=1,
        eligibility_id=1,
        file_name="file_name",
        file_type="file_type",
        path="path",
        eligibility=Eligibility(id=1, registration_id=1),
    )


def keycloak_profile_json(*args, **kwargs):
    return {"keycloakGuid": "ecb1ef8f2fee443eb14a414321bbc1f2"}


def new_sbc_account(*args, **kwargs):
    return {"id": 1}


def no_op(*args, **kwargs):
    None


def empty_json(*args, **kwargs):
    return {}
