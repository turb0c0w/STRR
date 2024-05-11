import { AccountTypeE } from '~/enums/account-type-e'
import { AccountStatusE } from '~/enums/account-status-e'
import { UserSettingsTypeE } from '~/enums/user-settings-type-e'

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
