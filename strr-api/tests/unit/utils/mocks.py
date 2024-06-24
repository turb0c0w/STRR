from strr_api.enums.enum import PaymentStatus
from strr_api.exceptions import ExternalServiceException
from strr_api.models import Document, Eligibility, Invoice, Registration, User


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


def fake_registration(*args, **kwargs):
    return Registration(
        id=1,
        user_id=1,
        sbc_account_id=1000,
        eligibility=Eligibility(id=1, registration_id=1),
    )


def fake_invoice(*args, **kwargs):
    return Invoice(
        id=1,
        registration_id=1,
        invoice_id=1,
        payment_status_code=PaymentStatus.CREATED,
        payment_completion_date=None,
        payment_account="3299",
    )


def fake_invoice_details(*args, **kwargs):
    return {"statusCode": "COMPLETED"}


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


def throw_external_service_exception(*args, **kwargs):
    raise ExternalServiceException("Test exception")


def empty_json(*args, **kwargs):
    return {}
