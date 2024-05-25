<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.contact-form.mailingAddress')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="country" class="flex-grow">
          <UDropdown
            :model-value="country"
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
            :model-value="address" 
            :placeholder="t('create-account.contact-form.address')" 
            @keypress.once="enableAddressComplete(id, 'CAN')"
            @click="enableAddressComplete(id, 'CAN')"
          />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="AddressLineTwo" class="flex-grow">
          <UInput :model-value="addressLineTwo" :placeholder="t('create-account.contact-form.addressLineTwo')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px]">
        <UFormGroup name="city" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput :model-value="city" :placeholder="t('create-account.contact-form.city')" />
        </UFormGroup>
        <UFormGroup name="province" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UDropdown
            :model-value="province"
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
          <UInput :model-value="postalCode" :placeholder="t('create-account.contact-form.postalCode')" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">

const t = useNuxtApp().$i18n.t

const {
  id,
  enableAddressComplete,
  country,
  address,
  addressLineTwo,
  city,
  province,
  postalCode
} = defineProps<{
  id: string,
  enableAddressComplete: (id: string) => void,
  country: string | undefined,
  address: string | undefined,
  addressLineTwo: string | undefined,
  city: string | undefined,
  province: string | undefined,
  postalCode: string | undefined,
}>()


const emit = defineEmits<{
  setCountry: [country: string],
  setAddress: [address: string],
  setAddressLineTwo: [addressLineTwo: string],
  setCity: [city: string],
  setProvince: [province: string],
  setPostalCode: [postalCode: string]
}>()

</script>
