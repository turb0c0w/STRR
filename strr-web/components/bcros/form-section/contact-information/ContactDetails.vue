<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.contactDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="preferredName" class=" flex-grow">
          <UInput v-model="preferredName" :placeholder="t('create-account.contact-form.preferredName')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px]">
        <UFormGroup name="phoneNumber" class="desktop:pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput v-model="phoneNumber" :placeholder="t('create-account.contact-form.phoneNumber')" />
        </UFormGroup>
        <UFormGroup name="extension" class="flex-grow">
          <UInput v-model="extension" :placeholder="t('create-account.contact-form.extension')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="faxNumber" class="flex-grow">
          <UInput v-model="faxNumber" :placeholder="t('create-account.contact-form.faxNumber')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="emailAddress" class="flex-grow">
          <UInput v-model="emailAddress" :placeholder="t('create-account.contact-form.emailAddress')" />
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

const preferredName = defineModel('preferredName')
const phoneNumber = defineModel('phoneNumber')
const extension = defineModel('extension')
const faxNumber = defineModel('faxNumber')
const emailAddress = defineModel('emailAddress')
</script>
