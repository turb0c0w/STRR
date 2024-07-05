from strr_api.models import Address
from strr_api.requests import SBCMailingAddress


def compare_addresses(property_address: Address, sbc_address: SBCMailingAddress):
    """Compare property address with sbc address."""
    return (
        property_address.street_address == sbc_address.street
        and property_address.street_address_additional == sbc_address.streetAdditional
        and property_address.city == sbc_address.city
        and property_address.province == sbc_address.region
        and property_address.postal_code == sbc_address.postalCode
        and property_address.country == sbc_address.country
    )
