<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.property-form.rentalUnitAddress')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="nickname" class="pr-[16px] flex-grow">
          <UInput v-model="nickname" :placeholder="t('create-account.property-form.nickname')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="useMailing" class="pr-[16px] flex-grow mobile:text-[16px]">
          <UCheckbox v-model="useMailing" :label="t('create-account.property-form.useMailing')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="country" class="pr-[16px] flex-grow">
          <USelect
            v-model="country"
            :options="countryItems"
            option-attribute="name"
            class="w-full"
          />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="Address" class="pr-[16px] flex-grow">
          <UInput
            :id="id"
            v-model="address"
            :placeholder="t('create-account.contact-form.address')"
            @keypress.once="addressComplete()"
            @click="addressComplete()"
          />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="AddressLineTwo" class="pr-[16px] flex-grow">
          <UInput v-model="addressLineTwo" :placeholder="t('create-account.contact-form.addressLineTwo')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px]">
        <UFormGroup name="city" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput v-model="city" :placeholder="t('create-account.contact-form.city')" />
        </UFormGroup>
        <UFormGroup name="province" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput v-model="province" :placeholder="t('create-account.contact-form.city')" />
        </UFormGroup>
        <UFormGroup name="postalCode" class="pr-[16px] flex-grow mobile:mb-[16px]">
          <UInput v-model="postalCode" :placeholder="t('create-account.contact-form.postalCode')" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { CountryItem } from '@/interfaces/address-i'
import countries from '@/utils/countries.json'
const t = useNuxtApp().$i18n.t

const country = defineModel<string>('country')
const address = defineModel<string>('address')
const addressLineTwo = defineModel<string>('addressLineTwo')
const city = defineModel<string>('city')
const province = defineModel<string>('province')
const postalCode = defineModel<string>('postalCode')
const useMailing = defineModel<string>('useMailing')
const nickname = defineModel<string>('nickname')
const countryItems = ref<CountryItem[]>([])

const addressComplete = () => {
  if (typeof country.value === 'string') {
    enableAddressComplete(id, 'CAN')
  }
}

const {
  id,
  defaultCountryIso2,
  enableAddressComplete
} = defineProps<{
  id: string,
  defaultCountryIso2: string,
  enableAddressComplete:(id: string, countryIso2: string) => void
}>()

country.value = defaultCountryIso2

onMounted(() => {
  countryItems.value = countries.map(country => ({
    value: country.iso2,
    name: country.en
  }))
})

</script>
