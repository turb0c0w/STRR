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
  preferredName: string | undefined,
  phoneNumber: string | undefined,
  extension: string | undefined,
  faxNumber: string | undefined,
  emailAddress: string | undefined,
  address: string | undefined,
  country: string | undefined,
  addressLineTwo: string | undefined,
  city: string | undefined,
  province: string | undefined,
  postalCode: string | undefined,
  birthDay: string | undefined,
  birthMonth: string | undefined,
  birthYear: string | undefined,
}

export interface SecondaryContactInformationI extends ContactInformationI {
  firstName: string | undefined,
  middleName: string | undefined,
  lastName: string | undefined,
}

export interface CreateAccountFormStateI {
  primaryContact: ContactInformationI,
  secondaryContact: SecondaryContactInformationI,
  propertyDetails: {
    primaryResidence: string | undefined,
    whichPlatform: string | undefined,
    parcelIdentifier: string | undefined,
    businessLicense: string | undefined,
    propertyType: string | undefined,
    ownershipType: string | undefined,
    useMailing: boolean,
    nickname: string | undefined,
    country: string | undefined,
    address: string | undefined,
    addressLineTwo: string | undefined,
    city: string | undefined,
    province: string | undefined,
    postalCode: string | undefined,
    listingDetails: { url: string }[],
  },
  selectedAccount: OrgI
}

export interface MailingAddressAPII {
  address: string,
  addressLineTwo?: string,
  city: string,
  postalCode: string,
  province: string,
  country: string,
}

export interface ContactNameAPII {
  firstName: string,
  middleName?: string,
  lastName: string,
}

export interface ContactAPII {
  name: ContactNameAPII,
  dateOfBirth: string,
  details: {
    preferredName?: string,
    phoneNumber: string,
    extension?: string,
    faxNumber?: string,
    emailAddress: string
  },
  mailingAddress: MailingAddressAPII
}

export interface SelectedAccountMailingAPII {
  street: string,
  streetAdditional: string,
  city: string,
  postalCode: string,
  region: string,
  country: string,
}

export interface CreateAccountFormAPII {
  selectedAccount: {
    name: string,
    mailingAddress: SelectedAccountMailingAPII
  },
  registration: {
    primaryContact?: ContactAPII,
    secondaryContact?: ContactAPII,
    unitAddress: MailingAddressAPII,
    unitDetails: {
      parcelIdentifier?: string,
      businessLicense?: string,
      propertyType: string,
      ownershipType: string
    },
    listingDetails: { url: string }[]
  }
}
