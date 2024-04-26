<template>
  <div data-cy="account-page">
    <BcrosTypographyH1 text="account.title" data-cy="accountPageTitle" />
    <BcrosAlertsMessage :flavour="alertFlavour">
      {{ t('account.existing-account-warning') }}
    </BcrosAlertsMessage>
    <BcrosTypographyH2 text="account.existing-account-section.title" data-cy="accountPageAccountSectionTitle" />
    <span class="text-[16px]">{{ t('account.existing-account-section.sub-title') }}</span>
    <BcrosExistingAccountsList :accounts="mockExistingAccountsData" />
  </div>
</template>

<script setup lang="ts">
import { AlertsFlavourE } from '#imports'

const t = useNuxtApp().$i18n.t

const alertFlavour: AlertsFlavourE = AlertsFlavourE.INFO

const mockExistingAccountsData: AccountI[] = [
  {
    id: 'ID',
    accountType: AccountTypeE.BASIC,
    accountStatus: AccountStatusE.ACTIVE,
    label: 'Existing Account Name',
    type: UserSettingsTypeE.ACCOUNT,
    urlpath: 'URLPATH',
    urlorigin: 'URLORIGIN',
    address: '123456 Temporary St, Parksville, BC V8V 8V8, Canada'
  },
  {
    id: 'ID',
    accountType: AccountTypeE.BASIC,
    accountStatus: AccountStatusE.ACTIVE,
    label: 'Existing Account Name 2',
    type: UserSettingsTypeE.ACCOUNT,
    urlpath: 'URLPATH',
    urlorigin: 'URLORIGIN',
    address: '123456 Temporary St, Parksville, BC V8V 8V8, Canada'
  },
  {
    id: 'ID',
    accountType: AccountTypeE.BASIC,
    accountStatus: AccountStatusE.ACTIVE,
    label: 'Zang & Associates',
    type: UserSettingsTypeE.ACCOUNT,
    urlpath: 'URLPATH',
    urlorigin: 'URLORIGIN',
    address: '-'
  }
]

</script>
