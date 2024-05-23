# pylint: disable=C0103
# pylint: disable=R0913
"""
Registration request payload objects.
"""


class RegistrationRequest:
    """RegistrationRequest payload object."""

    def __init__(self, selectedAccount, registration):
        self.selectedAccount = SelectedAccount(**selectedAccount)
        self.registration = Registration(**registration)


class SBCMailingAddress:
    """SBCMailingAddress payload object."""

    def __init__(self, street, city, region, postalCode, country, streetAdditional=None):
        self.street = street
        self.streetAdditional = streetAdditional
        self.city = city
        self.region = region
        self.postalCode = postalCode
        self.country = country


class SelectedAccount:
    """SelectedAccount payload object."""

    def __init__(self, name, mailingAddress):
        self.name = name
        self.mailingAddress = SBCMailingAddress(**mailingAddress)


class Registration:
    """Registration payload object."""

    def __init__(self, primaryContact, secondaryContact, unitAddress, unitDetails, listingDetails):
        self.primaryContact = Contact(**primaryContact)
        self.secondaryContact = Contact(**secondaryContact)
        self.unitAddress = UnitAddress(**unitAddress)
        self.unitDetails = UnitDetails(**unitDetails)
        self.listingDetails = [ListingDetails(**item) for item in listingDetails]


class ListingDetails:
    """ListingDetails payload object."""

    def __init__(self, url):
        self.url = url


class UnitDetails:
    """UnitDetails payload object."""

    def __init__(self, parcelIdentifier, businessLicense, propertyType, ownershipType):
        self.parcelIdentifier = parcelIdentifier
        self.businessLicense = businessLicense
        self.propertyType = propertyType
        self.ownershipType = ownershipType


class MailingAddress:
    """MailingAddress payload object."""

    def __init__(self, address, addressLineTwo, city, postalCode, province, country):
        self.address = address
        self.addressLineTwo = addressLineTwo
        self.city = city
        self.postalCode = postalCode
        self.province = province
        self.country = country


class UnitAddress(MailingAddress):
    """UnitAddress payload object."""

    def __init__(self, nickname, address, addressLineTwo, city, postalCode, province, country):
        super().__init__(address, addressLineTwo, city, postalCode, province, country)
        self.nickname = nickname


class ContactName:
    """ContactName payload object."""

    def __init__(self, firstName, middleName, lastName):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName


class ContactDetails:
    """ContactDetails payload object."""

    def __init__(self, preferredName, phoneNumber, extension, faxNumber, emailAddress):
        self.preferredName = preferredName
        self.phoneNumber = phoneNumber
        self.extension = extension
        self.faxNumber = faxNumber
        self.emailAddress = emailAddress


class Contact:
    """Contact payload object."""

    def __init__(self, name, dateOfBirth, details, mailingAddress):
        self.name = ContactName(**name)
        self.dateOfBirth = dateOfBirth
        self.details = ContactDetails(**details)
        self.mailingAddress = MailingAddress(**mailingAddress)
