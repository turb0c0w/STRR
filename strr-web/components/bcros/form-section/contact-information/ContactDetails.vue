<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.contactDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="preferredName" class="pr-[16px] flex-grow">
          <UInput v-model="preferredName" :placeholder="t('create-account.contact-form.preferredName')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="phoneNumber" class="pr-[16px] flex-grow">
          <UInput v-model="phoneNumber" :placeholder="t('create-account.contact-form.phoneNumber')" />
        </UFormGroup>
        <UFormGroup name="extension" class="pr-[16px] flex-grow">
          <UInput v-model="extension" :placeholder="t('create-account.contact-form.extension')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="faxNumber" class="pr-[16px] flex-grow">
          <UInput v-model="faxNumber" :placeholder="t('create-account.contact-form.faxNumber')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="emailAddress" class="pr-[16px] flex-grow">
          <UInput v-model="emailAddress" :placeholder="t('create-account.contact-form.emailAddress')" />
        </UFormGroup>
      </div>
      <BcrosAlertsMessage :flavour="AlertsFlavourE.INFO" class="mr-[20px]">
        <p>
          <b>{{ t('create-account.contact-form.bold-warning') }}</b>
          {{ t('create-account.contact-form.warning') }}
        </p>
      </BcrosAlertsMessage>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
const { formState } = defineProps<{ formState: any }>();

const {
  preferredName,
  phoneNumber,
  extension,
  faxNumber,
  emailAddress
} = formState

const t = useNuxtApp().$i18n.t

</script>
