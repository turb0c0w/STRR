export interface RegistrationAddressI {
  city: string
  country: string
  postalCode: string
  province: string
  address: string
  addressLineTwo: string
  nickname: string
}

export interface RegistrationI {
  id: number,
  listingDetails: { url: string }[],
  primaryContact: ContactI,
  principalResidence: PrincipalResidenceI,
  sbc_account_id: number,
  status: string,
  submissionDate: string,
  unitAddress: RegistrationAddressI,
  unitDetails: {
    parcelIdentifier?: string,
    businessLicense?: string,
    propertyType: string,
    ownershipType: string
  },
  updatedDate: string,
  user_id: number
}
