<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.mailingAddress')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="country" class="flex-grow">
          <UDropdown
            v-model="formState.country"
            :items="[]"
            class="w-full"
            :popper="{
              placement: 'bottom-start',
            }"
          >
            <UInput
              class="w-full"
              color="white"
              :placeholder="t('create-account.contact-form.country')"
              trailing-icon="i-heroicons-chevron-down-20-solid"
            />
          </UDropdown>
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="Address" class="flex-grow">
          <UInput 
            :id="id"
            v-model="formState.address" 
            :placeholder="t('create-account.contact-form.address')" 
            @keypress.once="enableAddressComplete(id, 'CAN')"
            @click="enableAddressComplete(id, 'CAN')"
          />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="AddressLineTwo" class="flex-grow">
          <UInput v-model="formState.addressLineTwo" :placeholder="t('create-account.contact-form.addressLineTwo')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px]">
        <UFormGroup name="city" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput v-model="formState.city" :placeholder="t('create-account.contact-form.city')" />
        </UFormGroup>
        <UFormGroup name="province" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UDropdown
            v-model="formState.province"
            :items="[]"
            class="w-full"
            :popper="{
              placement: 'bottom-start',
            }"
          >
            <UInput
              class="w-full"
              color="white"
              :placeholder="t('create-account.contact-form.province')"
              trailing-icon="i-heroicons-chevron-down-20-solid"
            />
          </UDropdown>
        </UFormGroup>
        <UFormGroup name="postalCode" class="flex-grow mobile:mb-[16px]">
          <UInput v-model="formState.postalCode" :placeholder="t('create-account.contact-form.postalCode')" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { watch } from 'vue'
const { formState, id } = defineProps<{ formState: any, id : string }>()
const { address: canadaPostAddress, enableAddressComplete: enableAddressComplete } = useCanadaPostAddress()

const t = useNuxtApp().$i18n.t

watch(canadaPostAddress, (newAddress) => {
  console.log(newAddress)
  if (newAddress) {
    formState.address = newAddress.street
    formState.addressLineTwo = newAddress.streetAdditional
    formState.country = newAddress.country
    formState.city = newAddress.city
    formState.province = newAddress.region
    formState.postalCode = newAddress.postalCode
  }
})
</script>
