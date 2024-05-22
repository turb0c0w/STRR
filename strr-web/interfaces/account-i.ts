import { AccountTypeE } from '~/enums/account-type-e'
import { AccountStatusE } from '~/enums/account-status-e'
import { UserSettingsTypeE } from '~/enums/user-settings-type-e'

export interface DateOfBirthI {
  day: string
  month: string
  year: string
}

export interface AddressI {
  city: string
  country: string
  postalCode: string
  region: string
  street: string
  streetAdditional: string
}

export interface AccountI {
  id: string
  accessType: string
  accountType: AccountTypeE
  accountStatus: AccountStatusE
  additionalLabel?: string
  label: string
  type: UserSettingsTypeE.ACCOUNT
  urlpath: string
  urlorigin: string
  address: string
  mailingAddress?: AddressI[]
}

export interface OrgI {
  accessType: string
  branchName: string
  created: string
  createdBy: string
  id: string
  isBusinessAccount: boolean
  mailingAddress: AddressI[]
  modifiedBy: string
  name: string
  orgStatus: AccountStatusE
  orgType: AccountTypeE
  statusCode: string
  uuid: string
}

export interface ContactI {
  email: string
  phone: string
  phoneExtension: string
}

interface UserTermsI {
  isTermsOfUseAccepted: boolean
  termsOfUseAcceptedVersion: string
}

interface ProfileI {
  contacts: ContactI[]
  created: string
  firstname: string
  id: number
  idpUserid: string
  keycloakGuid: string
  lastname: string
  loginSource: string
  loginTime: string
  modified: string
  modifiedBy: string
  type: string
  userStatus: number
  userTerms: UserTermsI
  username: string
  verified: boolean
}

export interface MeI {
  orgs: OrgI[]
  profile: ProfileI
  settings: UserSettingsI[]
}

export interface ContactInformationI {
  preferredName: string,
  phoneNumber: string,
  extension: string,
  faxNumber: string,
  emailAddress: string,
  address: string,
  country: string,
  addressLineTwo: string,
  city: string,
  province: string,
  postalCode: string,
  dateOfBirth: {
    day: string,
    month: string,
    year: string
  }
}

export interface CreateAccountFormStateI {
  primaryContact: ContactInformationI,
  secondaryContact: ContactInformationI,
  questions: {
    primaryResidence: string,
    whichPlatform: string
  },
  unitDetails: {
    parcelIdentifier: string,
    businessLicense: string,
    propertyType: string,
    ownershipType: string
  },
  unitAddress: {
    useMailing: boolean,
    nickname: string,
    country: string,
    address: string,
    addressLineTwo: string,
    city: string,
    province: string,
    postalCode: string
  },
  listingDetails: string[],
  selectedAccount: OrgI
}