"""
Registration response objects.
"""
from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from strr_api import models


class SBCMailingAddress(BaseModel):
    """SBCMailingAddress response object."""

    street: str
    streetAdditional: Optional[str] = None
    city: str
    region: str
    postalCode: str
    country: str


class ListingDetails(BaseModel):
    """ListingDetails response object."""

    url: str


class UnitDetails(BaseModel):
    """UnitDetails response object."""

    parcelIdentifier: Optional[str] = None
    businessLicense: Optional[str] = None
    propertyType: str
    ownershipType: str


class MailingAddress(BaseModel):
    """MailingAddress response object."""

    address: str
    addressLineTwo: Optional[str] = None
    city: str
    postalCode: str
    province: str
    country: str


class UnitAddress(MailingAddress):
    """UnitAddress response object."""

    nickname: Optional[str] = None

    def __init__(self, address_dict, nickname: Optional[str] = None):
        super().__init__(**address_dict)
        self.nickname = nickname


class ContactName(BaseModel):
    """ContactName response object."""

    firstName: str
    middleName: Optional[str] = None
    lastName: str


class ContactDetails(BaseModel):
    """ContactDetails response object."""

    preferredName: Optional[str] = None
    phoneNumber: str
    extension: Optional[str] = None
    faxNumber: Optional[str] = None
    emailAddress: Optional[str] = None


class Contact(BaseModel):
    """Contact response object."""

    name: ContactName
    dateOfBirth: date
    details: ContactDetails
    mailingAddress: MailingAddress


class Registration(BaseModel):
    """Registration response object."""

    id: int
    sbc_account_id: Optional[int] = None
    submissionDate: datetime
    updatedDate: datetime
    status: str
    primaryContact: Contact
    secondaryContact: Optional[Contact] = None
    unitAddress: UnitAddress
    unitDetails: UnitDetails
    listingDetails: List[ListingDetails]

    @classmethod
    def from_db(cls, source: models.Registration):
        """Return a Registration object from a database model."""
        return cls(
            id=source.id,
            sbc_account_id=source.sbc_account_id,
            submissionDate=source.submission_date,
            updatedDate=source.updated_date,
            status=source.status.name,
            primaryContact=Contact(
                name=ContactName(
                    firstName=source.rental_property.property_manager.primary_contact_user.firstname,
                    middleName=source.rental_property.property_manager.primary_contact_user.middlename,
                    lastName=source.rental_property.property_manager.primary_contact_user.lastname,
                ),
                dateOfBirth=source.rental_property.property_manager.primary_contact_user.date_of_birth,
                details=ContactDetails(
                    preferredName=source.rental_property.property_manager.primary_contact_user.preferredname,
                    phoneNumber=source.rental_property.property_manager.primary_contact_user.phone_number,
                    extension=source.rental_property.property_manager.primary_contact_user.phone_extension,
                    faxNumber=source.rental_property.property_manager.primary_contact_user.fax_number,
                    emailAddress=source.rental_property.property_manager.primary_contact_user.email,
                ),
                mailingAddress=MailingAddress(
                    address=source.rental_property.property_manager.primary_address.street_address,
                    addressLineTwo=source.rental_property.property_manager.primary_address.street_address_additional,
                    city=source.rental_property.property_manager.primary_address.city,
                    postalCode=source.rental_property.property_manager.primary_address.postal_code,
                    province=source.rental_property.property_manager.primary_address.province,
                    country=source.rental_property.property_manager.primary_address.country,
                ),
            ),
            secondaryContact=Contact(
                name=ContactName(
                    firstName=source.rental_property.property_manager.secondary_contact_user.firstname,
                    middleName=source.rental_property.property_manager.secondary_contact_user.middlename,
                    lastName=source.rental_property.property_manager.secondary_contact_user.lastname,
                ),
                dateOfBirth=source.rental_property.property_manager.secondary_contact_user.date_of_birth,
                details=ContactDetails(
                    preferredName=source.rental_property.property_manager.secondary_contact_user.preferredname,
                    phoneNumber=source.rental_property.property_manager.secondary_contact_user.phone_number,
                    extension=source.rental_property.property_manager.secondary_contact_user.phone_extension,
                    faxNumber=source.rental_property.property_manager.secondary_contact_user.fax_number,
                    emailAddress=source.rental_property.property_manager.secondary_contact_user.email,
                ),
                mailingAddress=MailingAddress(
                    address=source.rental_property.property_manager.secondary_address.street_address,
                    addressLineTwo=source.rental_property.property_manager.secondary_address.street_address_additional,
                    city=source.rental_property.property_manager.secondary_address.city,
                    postalCode=source.rental_property.property_manager.secondary_address.postal_code,
                    province=source.rental_property.property_manager.secondary_address.province,
                    country=source.rental_property.property_manager.secondary_address.country,
                ),
            )
            if source.rental_property.property_manager.secondary_contact_user
            else None,
            unitAddress=UnitAddress(
                {
                    "address": source.rental_property.address.street_address,
                    "addressLineTwo": source.rental_property.address.street_address_additional,
                    "city": source.rental_property.address.city,
                    "postalCode": source.rental_property.address.postal_code,
                    "province": source.rental_property.address.province,
                    "country": source.rental_property.address.country,
                },
                nickname=source.rental_property.nickname,
            ),
            unitDetails=UnitDetails(
                parcelIdentifier=source.rental_property.parcel_identifier,
                businessLicense=source.rental_property.local_business_licence,
                propertyType=source.rental_property.property_type.name,
                ownershipType=source.rental_property.ownership_type.name,
            ),
            listingDetails=[ListingDetails(url=platform.url) for platform in source.rental_property.rental_platforms],
        )
