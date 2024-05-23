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
  birthDay: string,
  birthMonth: string,
  birthYear: string
}

export interface CreateAccountFormStateI {
  preferredName: string | null,
  phoneNumber: number | null,
  extension: string | null,
  faxNumber: string | null,
  emailAddress: string | null,
  address: string | null,
  country: string | null,
  addressLineTwo: string | null,
  city: string | null,
  province: string | null,
  postalCode: string | null,
  birthDay: number | null,
  birthMonth: string | null,
  birthYear: number | null,
  secondaryContactPreferredName: string | null,
  secondaryContactPhoneNumber: number | null,
  secondaryContactExtension: string | null,
  secondaryContactFaxNumber: string | null,
  secondaryContactEmailAddress: string | null,
  secondaryContactAddress: string | null,
  secondaryContactCountry: string | null,
  secondaryContactAddressLineTwo: string | null,
  secondaryContactCity: string | null,
  secondaryContactProvince: string | null,
  secondaryContactPostalCode: string | null,
  secondaryContactBirthDay: number | null,
  secondaryContactBirthMonth: string | null,
  secondaryContactBirthYear: number | null,
  questions: {
    primaryResidence: string | null,
    whichPlatform: string | null
  },
  unitDetails: {
    parcelIdentifier: string | null,
    businessLicense: string | null,
    propertyType: string | null,
    ownershipType: string | null
  },
  unitAddress: {
    useMailing: boolean,
    nickname: string | null,
    country: string | null,
    address: string | null,
    addressLineTwo: string | null,
    city: string | null,
    province: string | null,
    postalCode: string | null
  },
  listingDetails: string | null[],
  selectedAccount: OrgI
}
