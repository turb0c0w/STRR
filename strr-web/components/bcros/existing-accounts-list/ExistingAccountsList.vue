<template>
  <div class="flex flex-col justify-center mb-[32px]" data-cy="existing-accounts-list">
    <div v-for="account in accounts" :key="account.id" class="bg-white shadow-md">
      <div
        class="mobile:flex-col items-center pb-[24px] flex flex-row
        justify-space-between mobile:mx-[8px] mx-[32px] mt-[24px] border-b border-bcGovColor-hairlinesOnWhite"
      >
        <div class="flex grow mobile:justify-between mobile:w-full mobile:mb-[16px]">
          <div><BcrosLetterIcon :letter="account.label.charAt(0)" /></div>
          <div class="grow pl-[20px]">
            <div class="text-[18px] font-bold">
              {{ account.label }}
            </div>
            <div class="text-[14px]">
              {{
                account.mailingAddress
                  ? `${account.mailingAddress.street}, ${account.mailingAddress.city},
                    ${account.mailingAddress.region} ${account.mailingAddress.postalCode},
                    ${account.mailingAddress.country}`
                  : '-'
              }}
            </div>
          </div>
        </div>
        <div class="mobile:w-full">
          <BcrosButtonsPrimary
            :action="() => chooseButtonAction(account)"
            icon="i-mdi-chevron-right"
            :label="buttonText"
            :text="buttonText"
            :trailing="true"
            class="mobile:grow"
          />
        </div>
      </div>
    </div>
  </div>
  <div class="flex justify-center">
    <BcrosButtonsPrimary
      :action="createButtonAction"
      icon="i-mdi-chevron-right"
      :label="buttonText"
      :text="createAccountButtonText"
      :trailing="true"
      variant="outline"
      class="mobile:grow px-[8px]"
    />
  </div>
</template>

<script setup lang="ts">
const { accounts } = defineProps<{ accounts: AccountI[] }>()
const t = useNuxtApp().$i18n.t

const buttonText = t('account.existing-account-section.use-account-button')
const createButtonAction = () => alert('Creating new Account')
const chooseButtonAction = (account : AccountI) => alert(`Using Account ID: ${account.label}`)

const createAccountButtonText = t('account.existing-account-section.create-account-button')

</script>
