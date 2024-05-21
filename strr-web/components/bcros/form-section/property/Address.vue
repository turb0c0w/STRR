<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection title="Mailing Address">
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="nickname" class="pr-[16px] flex-grow">
          <UInput v-model="nickname" placeholder="Nickname (Optional)" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="country" class="pr-[16px] flex-grow">
          <UInput v-model="country" placeholder="Country" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="address" class="pr-[16px] flex-grow">
          <UInput v-model="address" placeholder="Address" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="AddressLineTwo" class="pr-[16px] flex-grow">
          <UInput v-model="addressLineTwo" placeholder="Address Line 2 (Optional)" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="city" class="pr-[16px] flex-grow">
          <UInput v-model="city" placeholder="City" />
        </UFormGroup>
        <UFormGroup name="province" class="pr-[16px] flex-grow">
          <UInput v-model="province" placeholder="Province" />
        </UFormGroup>
        <UFormGroup name="postalCode" class="pr-[16px] flex-grow">
          <UInput v-model="postalCode" placeholder="Postal Code" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { formState } from '@/stores/strr'

const {
  unitAddress: {
    nickname,
    country,
    address,
    addressLineTwo,
    city,
    province,
    postalCode
  }
} = formState
const t = useNuxtApp().$i18n.t

</script>
