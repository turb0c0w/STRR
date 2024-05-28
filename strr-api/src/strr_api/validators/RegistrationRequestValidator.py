"""Validator for registration requests."""
import re

from strr_api.exceptions import ValidationException


def validate_registration_request(selected_account, registration_request):
    """Validate the registration request."""
    # DO POSTAL CODE VALIDATION IF COUNTRY IS CANADA
    if selected_account.mailingAddress:
        selected_account.mailingAddress.postalCode = validate_and_format_canadian_postal_code(
            selected_account.mailingAddress.country,
            selected_account.mailingAddress.region,
            selected_account.mailingAddress.postalCode,
        )

    registration_request.registration.unitAddress.postalCode = validate_and_format_canadian_postal_code(
        registration_request.registration.unitAddress.country,
        registration_request.registration.unitAddress.province,
        registration_request.registration.unitAddress.postalCode,
    )

    if (
        registration_request.registration.unitAddress.country != "CA"
        or registration_request.registration.unitAddress.province != "BC"
    ):
        raise ValidationException(message="Invalid Rental Unit Address. Location must be in British Columbia.")

    registration_request.registration.primaryContact.mailingAddress.postalCode = (
        validate_and_format_canadian_postal_code(
            registration_request.registration.primaryContact.mailingAddress.country,
            registration_request.registration.primaryContact.mailingAddress.province,
            registration_request.registration.primaryContact.mailingAddress.postalCode,
        )
    )

    if registration_request.registration.secondaryContact:
        registration_request.registration.secondaryContact.mailingAddress.postalCode = (
            validate_and_format_canadian_postal_code(
                registration_request.registration.secondaryContact.mailingAddress.country,
                registration_request.registration.secondaryContact.mailingAddress.province,
                registration_request.registration.secondaryContact.mailingAddress.postalCode,
            )
        )


def validate_and_format_canadian_postal_code(country: str, province: str, postal_code: str):
    """Validate and format a Canadian postal code."""

    if country == "CA":
        if province not in ["BC", "AB", "SK", "MB", "ON", "QC", "NB", "PE", "NS", "NL", "YT", "NT", "NU"]:
            raise ValidationException(
                message="Invalid province. Must be one of 'BC', 'AB', 'SK', 'MB', 'ON', 'QC', "
                + "'NB', 'PE', 'NS', 'NL', 'YT', 'NT', 'NU'"
            )

        regex = r"^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$"
        match = re.match(regex, postal_code)
        if match:
            return postal_code.upper().replace(" ", "")
        else:
            raise ValidationException(message="Invalid postal code. Must be in the format 'A1A 1A1' or 'A1A1A1'")

    return postal_code
