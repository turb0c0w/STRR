<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.contactDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="preferredName" class=" flex-grow">
          <UInput v-model="formState.preferredName" :placeholder="t('create-account.contact-form.preferredName')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px]">
        <UFormGroup name="phoneNumber" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput v-model.number="formState.phoneNumber" :placeholder="t('create-account.contact-form.phoneNumber')" />
        </UFormGroup>
        <UFormGroup name="extension" class="flex-grow">
          <UInput v-model.number="formState.extension" :placeholder="t('create-account.contact-form.extension')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="faxNumber" class="flex-grow">
          <UInput v-model="formState.faxNumber" :placeholder="t('create-account.contact-form.faxNumber')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="emailAddress" class="flex-grow">
          <UInput v-model="formState.emailAddress" :placeholder="t('create-account.contact-form.emailAddress')" />
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
const { formState } = defineProps<{ formState: any }>()

const t = useNuxtApp().$i18n.t

</script>
