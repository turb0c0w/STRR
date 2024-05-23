<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div :class="`mb-[${addSecondaryContact ? '32px' : '132px'}] bg-white rounded-[4px]`">
      <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
        <p class="px-[40px] py-[15px] font-bold">
          {{ t('create-account.contact.subtitle') }}
        </p>
      </div>
      <BcrosFormSection :title="t('create-account.contact.your-name')">
        <div class="mb-[16px] text-[14px] leading-[22px]">
          {{ fullName }}
        </div>
        <div class="mb-[16px] text-[14px] leading-[22px]">
          {{ t('create-account.contact.disclaimer') }}
        </div>
      </BcrosFormSection>
      <div class="h-[2px] w-full bg-bcGovGray-300 mx-[40px] mobile:mx-[]" />
      <UForm :schema="primaryContactSchema" :state="formState">
        <BcrosFormSectionContactInformationContactInfo :form-state="formState.primaryContact" />
        <BcrosFormSectionContactInformationContactDetails :form-state="formState.primaryContact" />
        <BcrosFormSectionContactInformationMailingAddress :form-state="formState.primaryContact" />
      </UForm>
    </div>
    <div v-if="!addSecondaryContact" class="mb-[180px] mt-[32px]">
      <BcrosButtonsPrimary
        :action="toggleAddSecondary"
        :text="t('create-account.contact.add-secondary')"
        variant="outline"
        icon=""
      />
    </div>
    <div v-else>
      <div class="mb-[180px] bg-white rounded-[4px]">
        <div class="bg-bcGovColor-gray2 rounded-t-[4px] flex flex-row justify-between items-center">
          <p class="px-[40px] py-[15px] font-bold">
            {{ t('create-account.contact.subtitle-two') }}
          </p>
          <div
            class="flex flex-row mr-[20px] w-[117px] h-[36px] items-center justify-center text-[16px] text-blue-500"
            role="button"
            :onclick="toggleAddSecondary"
          >
            <p class="mr-[4px]">
              {{ t('create-account.contact.remove') }}
            </p>
            <UIcon class="h-[20px] w-[20px]" name="i-mdi-remove" alt="remove icon" />
          </div>
        </div>
        <UForm :schema="primaryContactSchema" :state="formState">
          <BcrosFormSectionContactInformationContactInfo :form-state="formState.secondaryContact" :dob-optional="true" />
          <BcrosFormSectionContactInformationContactDetails :form-state="formState.secondaryContact" />
          <BcrosFormSectionContactInformationMailingAddress :form-state="formState.secondaryContact" />
        </UForm>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { formState } from '@/stores/strr'

const { fullName } = defineProps<{ fullName: string }>()

const addSecondaryContact = ref(false)

const toggleAddSecondary = () => {
  addSecondaryContact.value = !addSecondaryContact.value
}

const t = useNuxtApp().$i18n.t

</script>
