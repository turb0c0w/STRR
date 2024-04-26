<template>
  <div data-cy="account-page">
    <BcrosTypographyH1 text="account.title" data-cy="accountPageTitle" />
    <BcrosAlertsMessage :flavour="alertFlavour">
      {{ t('account.existing-account-warning') }}
    </BcrosAlertsMessage>
    <BcrosTypographyH2 text="account.existing-account-section.title" data-cy="accountPageAccountSectionTitle" />
    <span class="text-[16px] mb-[20px] block">{{ t('account.existing-account-section.sub-title') }}</span>
    <BcrosExistingAccountsList :accounts="userAccounts" />
  </div>
</template>

<script setup lang="ts">
import { AlertsFlavourE } from '#imports'

const t = useNuxtApp().$i18n.t

const alertFlavour: AlertsFlavourE = AlertsFlavourE.INFO

const { userAccounts } = useBcrosAccount();

</script>
