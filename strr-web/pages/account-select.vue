<template>
  <div data-cy="account-select-page">
    <div v-if="userAccounts.length > 0">
      <div class="mobile:px-[8px]">
        <BcrosTypographyH1 text="account.title" data-cy="accountPageTitle" class="mobile:pb-[20px]" />
        <BcrosAlertsMessage :flavour="alertFlavour">
          <b>{{ t('general.note') }} </b>{{ t('account.existing-account-warning') }}
        </BcrosAlertsMessage>
        <BcrosTypographyH2 :text="existingAcccountsTitle" data-cy="accountPageAccountSectionTitle" />
        <span class="text-[16px] mb-[20px] block">{{ t('account.existing-account-section.sub-title') }}</span>
      </div>
      <BcrosExistingAccountsList :accounts="userAccounts" />
    </div>
    <div v-else>
      <BcrosTypographyH1 text="account.logIn" data-cy="accountPageTitle" class="mobile:pb-[20px]" />
    </div>
  </div>
</template>

<script setup lang="ts">
import testAccounts from './test-accounts.json'
import { AccountI, AlertsFlavourE } from '#imports'

const t = useNuxtApp().$i18n.t

const alertFlavour: AlertsFlavourE = AlertsFlavourE.INFO

const { activeUserAccounts } = useBcrosAccount()

const query = useRoute().query

let userAccounts = activeUserAccounts

if ('test' in query && query.test === 'true') {
  const testData: AccountI[] = testAccounts as unknown as AccountI[]
  userAccounts = testData
}

const existingAcccountsTitle = `${t('account.existing-account-section.title')} (${userAccounts.length})`

</script>
