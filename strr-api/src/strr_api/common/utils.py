"""Common utility functions."""
from strr_api.models import Address
from strr_api.requests import SBCMailingAddress


def compare_addresses(property_address: Address, sbc_address: SBCMailingAddress):
    """Compare property address with sbc address."""

    result = (
        property_address.street_address.lower() == sbc_address.street.lower()
        and (
            (property_address.street_address_additional.lower() if property_address.street_address_additional else "")
            == (sbc_address.streetAdditional.lower() if sbc_address.streetAdditional else "")
        )
        and property_address.city.lower() == sbc_address.city.lower()
        and property_address.province.lower() == sbc_address.region.lower()
        and property_address.postal_code.lower().replace(" ", "") == sbc_address.postalCode.lower().replace(" ", "")
        and property_address.country.lower() == sbc_address.country.lower()
    )
    print(f"result: {result}")
    return result
