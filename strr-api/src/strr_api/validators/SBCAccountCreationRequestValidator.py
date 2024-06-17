"""Validator for SBC account creation requests."""
from strr_api.requests import SBCAccountCreationRequest
from strr_api.validators.RegistrationRequestValidator import validate_and_format_canadian_postal_code


def validate_account_creation_request(sbc_account_creation_request: SBCAccountCreationRequest):
    """Validate the SBC account creation request."""
    # DO POSTAL CODE VALIDATION IF COUNTRY IS CANADA
    sbc_account_creation_request.mailingAddress.postalCode = validate_and_format_canadian_postal_code(
        sbc_account_creation_request.mailingAddress.country,
        sbc_account_creation_request.mailingAddress.region,
        sbc_account_creation_request.mailingAddress.postalCode,
    )
