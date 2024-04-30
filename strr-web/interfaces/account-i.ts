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
  accountType: AccountTypeE
  accountStatus: AccountStatusE
  additionalLabel?: string
  label: string
  type: UserSettingsTypeE.ACCOUNT
  urlpath: string
  urlorigin: string
  address: string
  mailingAddress?: AddressI
}
