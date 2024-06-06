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

    def to_dict(self):
        """Convert object to dictionary for json serialization."""
        return {
            key: value
            for key, value in {
                "street": self.street,
                "streetAdditional": self.streetAdditional,
                "city": self.city,
                "region": self.region,
                "postalCode": self.postalCode,
                "country": self.country,
            }.items()
            if value is not None
        }


class SelectedAccount:
    """SelectedAccount payload object."""

    def __init__(self, sbc_account_id=None, name=None, mailingAddress=None):
        self.sbc_account_id = None
        self.name = None
        self.mailingAddress = None

        if sbc_account_id:
            self.sbc_account_id = sbc_account_id
        if name:
            self.name = name
        if mailingAddress:
            self.mailingAddress = SBCMailingAddress(**mailingAddress)


class Registration:
    """Registration payload object."""

    def __init__(
        self, primaryContact, unitAddress, unitDetails, listingDetails, principalResidence, secondaryContact=None
    ):
        self.primaryContact = Contact(**primaryContact)
        self.secondaryContact = None
        if secondaryContact:
            self.secondaryContact = Contact(**secondaryContact)
        self.unitAddress = UnitAddress(**unitAddress)
        self.unitDetails = UnitDetails(**unitDetails)
        self.listingDetails = [ListingDetails(**item) for item in listingDetails]
        self.principalResidence = PrincipalResidence(**principalResidence)


class PrincipalResidence:
    """PrincipalResidence payload object."""

    def __init__(
        self,
        isPrincipalResidence,
        agreedToRentalAct,
        agreedToSubmit,
        nonPrincipalOption=None,
        specifiedServiceProvider=None,
    ):
        self.isPrincipalResidence = isPrincipalResidence
        self.agreedToRentalAct = agreedToRentalAct
        self.agreedToSubmit = agreedToSubmit
        self.nonPrincipalOption = nonPrincipalOption
        self.specifiedServiceProvider = specifiedServiceProvider


class ListingDetails:
    """ListingDetails payload object."""

    def __init__(self, url):
        self.url = url


class UnitDetails:
    """UnitDetails payload object."""

    def __init__(self, propertyType, ownershipType, parcelIdentifier=None, businessLicense=None):
        self.propertyType = propertyType
        self.ownershipType = ownershipType
        self.parcelIdentifier = parcelIdentifier
        self.businessLicense = businessLicense


class MailingAddress:
    """MailingAddress payload object."""

    def __init__(self, address, city, postalCode, province, country, addressLineTwo=None):
        self.address = address
        self.city = city
        self.postalCode = postalCode
        self.province = province
        self.country = country
        self.addressLineTwo = addressLineTwo


class UnitAddress(MailingAddress):
    """UnitAddress payload object."""

    def __init__(self, address, city, postalCode, province, country, addressLineTwo=None, nickname=None):
        super().__init__(address, city, postalCode, province, country, addressLineTwo)
        self.nickname = nickname


class ContactName:
    """ContactName payload object."""

    def __init__(self, firstName, lastName, middleName=None):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName


class ContactDetails:
    """ContactDetails payload object."""

    def __init__(self, phoneNumber, emailAddress, preferredName=None, extension=None, faxNumber=None):
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.preferredName = preferredName
        self.extension = extension
        self.faxNumber = faxNumber


class Contact:
    """Contact payload object."""

    def __init__(self, name, dateOfBirth, details, mailingAddress):
        self.name = ContactName(**name)
        self.dateOfBirth = dateOfBirth
        self.details = ContactDetails(**details)
        self.mailingAddress = MailingAddress(**mailingAddress)
