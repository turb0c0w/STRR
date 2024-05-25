<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="desktop:mb-[180px] mobile:mb-[32px] bg-white rounded-[4px]">
      <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
        <p class="px-[40px] py-[15px] font-bold">
          {{ t('create-account.contact.subtitle') }}
        </p>
      </div>
      <UForm :schema="propertyDetailsSchema" :state="formState.propertyDetails">
        <BcrosFormSectionPropertyAddress
          id="propertyAddress"
          v-model:country="formState.propertyDetails.country"
          v-model:address="formState.propertyDetails.address"
          v-model:address-line-two="formState.propertyDetails.addressLineTwo"
          v-model:city="formState.propertyDetails.city"
          v-model:province="formState.propertyDetails.province"
          v-model:postal-code="formState.propertyDetails.postalCode"
          :enable-address-complete="enableAddressComplete"
          default-country-iso3="CAN"
        />
        <BcrosFormSectionPropertyDetails
          :property-types="propertyTypes"
          :ownership-types="ownershipTypes"
          v-model:property-type="formState.propertyDetails.propertyType"
          v-model:ownership-type="formState.propertyDetails.ownershipType"
          v-model:business-license="formState.propertyDetails.businessLicense"
          v-model:parcel-identifier="formState.propertyDetails.parcelIdentifier"
        />
        <BcrosFormSectionPropertyListingDetails
          v-model:form-state="formState.propertyDetails"
          :enable-address-complete="enableAddressComplete"
          :add-platform="addPlatform"
          :remove-detail-at-index="removeDetailAtIndex"
          v-model:listing-details="formState.propertyDetails.listingDetails"
        />
      </UForm>
    </div>
  </div>
</template>

<script setup lang="ts">
import { DropdownItem } from '@nuxt/ui/dist/runtime/types'

const {
  address: canadaPostAddress,
  enableAddressComplete
} = useCanadaPostAddress()

watch(canadaPostAddress, (newAddress) => {
  if (newAddress) {
    formState.propertyDetails.address = newAddress.street
    formState.propertyDetails.addressLineTwo = newAddress.streetAdditional
    formState.propertyDetails.country = newAddress.country
    formState.propertyDetails.city = newAddress.city
    formState.propertyDetails.province = newAddress.region
    formState.propertyDetails.postalCode = newAddress.postalCode
  }
})

const t = useNuxtApp().$i18n.t

const isValid = ref(false)

const addPlatform = () => {
  formState.propertyDetails.listingDetails.push('')
}

const removeDetailAtIndex = (index: number) => {
  formState.propertyDetails.listingDetails.splice(index, 1)
}

watch(formState.propertyDetails, () => {
  isValid.value = propertyDetailsSchema.safeParse(formState.propertyDetails).success
})

const emit = defineEmits<{
  validatePage: [isValid: boolean]
}>()

const propertyTypes: DropdownItem[][] = [
  [
    {
      label: t('create-account.property-form.primaryDwelling'),
      click: () => { formState.propertyDetails.propertyType = t('create-account.property-form.primaryDwelling') }
    },
    {
      label: t('create-account.property-form.secondarySuite'),
      click: () => { formState.propertyDetails.propertyType = t('create-account.property-form.secondarySuite') }
    },
    {
      label: t('create-account.property-form.accessory'),
      click: () => { formState.propertyDetails.propertyType = t('create-account.property-form.accessory') }
    },
    {
      label: t('create-account.property-form.float'),
      click: () => { formState.propertyDetails.propertyType = t('create-account.property-form.float') }
    },
    {
      label: t('create-account.property-form.other'),
      click: () => { formState.propertyDetails.propertyType = t('create-account.property-form.other') }
    }
  ]
]

const ownershipTypes: DropdownItem[][] = [
  [
    {
      label: t('create-account.property-form.rent'),
      click: () => { formState.propertyDetails.ownershipType = t('create-account.property-form.rent') }
    },
    {
      label: t('create-account.property-form.own'),
      click: () => { formState.propertyDetails.ownershipType = t('create-account.property-form.own') }
    },
    {
      label: t('create-account.property-form.other'),
      click: () => { formState.propertyDetails.ownershipType = t('create-account.property-form.coown') }
    }
  ]
]

</script>
