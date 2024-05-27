<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.contactDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="preferredName" class=" flex-grow">
          <UInput
            type="name"
            v-model="preferredName"
            :placeholder="t('create-account.contact-form.preferredName')"
          />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px]">
        <UFormGroup name="phoneNumber" class="desktop:pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput
            type="tel"
            v-model="phoneNumber"
            :placeholder="t('create-account.contact-form.phoneNumber')"
          />
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
        <UFormGroup
          type="email"
          name="emailAddress"
          class="flex-grow"
        >
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

const preferredName = defineModel<string>('preferredName')
const phoneNumber = defineModel<string>('phoneNumber')
const extension = defineModel<string>('extension')
const faxNumber = defineModel<string>('faxNumber')
const emailAddress = defineModel<string>('emailAddress')
</script>
