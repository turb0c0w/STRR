<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.contactDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="preferredName" class=" flex-grow">
          <UInput :model-value="preferredName" :placeholder="t('create-account.contact-form.preferredName')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px]">
        <UFormGroup name="phoneNumber" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput :model-value="phoneNumber" :placeholder="t('create-account.contact-form.phoneNumber')" />
        </UFormGroup>
        <UFormGroup name="extension" class="flex-grow">
          <UInput :model-value="extension" :placeholder="t('create-account.contact-form.extension')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="faxNumber" class="flex-grow">
          <UInput :model-value="faxNumber" :placeholder="t('create-account.contact-form.faxNumber')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="emailAddress" class="flex-grow">
          <UInput :model-value="emailAddress" :placeholder="t('create-account.contact-form.emailAddress')" />
        </UFormGroup>
      </div>
      <BcrosAlertsMessage :flavour="AlertsFlavourE.INFO">
        <p>
          <b>{{ t('create-account.contact-form.bold-warning') }}</b>
          {{ t('create-account.contact-form.warning') }}
        </p>
      </BcrosAlertsMessage>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
const t = useNuxtApp().$i18n.t

const { 
  preferredName,
  phoneNumber,
  extension,
  faxNumber,
  emailAddress
} = defineProps<{
  preferredName: string | undefined,
  phoneNumber: string | undefined,
  extension: string | undefined,
  faxNumber: string | undefined,
  emailAddress: string | undefined
}>()


const emit = defineEmits<{
  setPreferredName: [preferredName: string]
  setPhoneNumber: [phoneNumber: string]
  setExtension: [extension: string]
  setFaxNumber: [faxNumber: string]
  setEmailAddress: [emailAddress: string]
}>()

</script>
