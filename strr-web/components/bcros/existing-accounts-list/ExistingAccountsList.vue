<template>
  <div class="flex flex-col justify-center">
    <div v-for="account in accounts">
      <div class="items-center h-[52px] flex flex-row justify-space-between w-full mx-[32px] my-[24px]">
        <div><BcrosLetterIcon letter="E"/></div>
        <div class="grow pl-[20px]">
          <div class="text-[18px] font-bold">{{ account.label }}</div>
          <div class="text-[14px]">{{ account.address }}</div>
        </div>
        <div>
          <BcrosButtonsPrimary
            :action="buttonAction"
            icon="i-mdi-chevron-right"
            :label="buttonText"
            :text="buttonText"
            :trailing="true"
          />
        </div>
      </div>
    </div>
    <div class="flex justify-center">
      <BcrosButtonsPrimary 
        :action="buttonAction"
        icon="i-mdi-chevron-right"
        :label="buttonText"
        :text="createAccountButtonText"
        :trailing="true"
        variant="outline"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import LetterIcon from '../letter-icon/LetterIcon.vue';
import { ButtonVariant } from '@nuxt/ui/dist/runtime/types';

const { accounts } = defineProps<{ accounts: AccountI[] }>()
const t = useNuxtApp().$i18n.t

const buttonText = t("account.existing-account-section.use-account-button")
const buttonAction = () => console.log("CLICKED")

const createAccountButtonText = t("account.existing-account-section.create-account-button")

</script>