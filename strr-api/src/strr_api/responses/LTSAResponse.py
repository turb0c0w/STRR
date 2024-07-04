"""
LTSA response objects.
"""
from typing import List
from pydantic import BaseModel

class TitleSummary(BaseModel):
    """LTSA TitleSummary response object."""
    titleNumber: str
    landTitleDistrict: str
    landTitleDistrictCode: str
    parcelIdentifier: str
    status: str
    firstOwner: str

class TitleSummaries(BaseModel):
    """LTSA TitleSummaries response object."""
    titleSummaries: List[TitleSummary]

class TitleIdentifier(BaseModel):
    titleNumber: str
    landTitleDistrict: str

class FromTitle(BaseModel):
    titleNumber: str
    landTitleDistrict: str

class NatureOfTransfer(BaseModel):
    transferReason: str

class Tombstone(BaseModel):
    applicationReceivedDate: str
    enteredDate: str
    titleRemarks: str
    marketValueAmount: str
    fromTitles: List[FromTitle]
    natureOfTransfers: List[NatureOfTransfer]

class Address(BaseModel):
    addressLine1: str
    addressLine2: str
    city: str
    province: str
    provinceName: str
    country: str
    postalCode: str

class TitleOwner(BaseModel):
    lastNameOrCorpName1: str
    givenName: str
    incorporationNumber: str
    occupationDescription: str
    address: Address

class TaxAuthority(BaseModel):
    authorityName: str

class OwnershipGroup(BaseModel):
    jointTenancyIndication: bool
    interestFractionNumerator: str
    interestFractionDenominator: str
    ownershipRemarks: str
    titleOwners: List[TitleOwner]

class DescriptionOfLand(BaseModel):
    parcelIdentifier: str
    fullLegalDescription: str
    parcelStatus: str

class LtsaResponse(BaseModel):
    """LTSA Reference endpoint response object."""
    titleStatus: str
    titleIdentifier: TitleIdentifier
    tombstone: Tombstone
    taxAuthorities: List[TaxAuthority]
    ownershipGroups: List[OwnershipGroup]
    descriptionsOfLand: List[DescriptionOfLand]

    class Config:
        extra = 'ignore'
