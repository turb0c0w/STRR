<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.mailingAddress')" >
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="country" class="pr-[16px] flex-grow">
          <UInput v-model="country" :placeholder="t('create-account.contact-form.country')"  />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="Address" class="pr-[16px] flex-grow">
          <UInput v-model="address" :placeholder="t('create-account.contact-form.address')"  />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="AddressLineTwo" class="pr-[16px] flex-grow">
          <UInput v-model="addressLineTwo" :placeholder="t('create-account.contact-form.addressLineTwo')"  />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="city" class="pr-[16px] flex-grow">
          <UInput v-model="city" :placeholder="t('create-account.contact-form.city')"  />
        </UFormGroup>
        <UFormGroup name="province" class="pr-[16px] flex-grow">
          <UInput v-model="province" :placeholder="t('create-account.contact-form.province')"  />
        </UFormGroup>
        <UFormGroup name="postalCode" class="pr-[16px] flex-grow">
          <UInput v-model="postalCode" :placeholder="t('create-account.contact-form.postalCode')"  />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { formState } from '@/stores/strr'

const {
  primaryContact: {
    address,
    country,
    addressLineTwo,
    city,
    province,
    postalCode
  }
} = formState
const t = useNuxtApp().$i18n.t

</script>
