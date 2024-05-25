<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="mb-[180px] bg-white rounded-[4px]">
      <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
        <p class="px-[40px] py-[15px] font-bold">
          {{ t('create-account.contact.subtitle') }}
        </p>
      </div>
      <UForm :schema="propertyDetailsSchema" :state="formState.propertyDetails">
        <BcrosFormSectionPropertyAddress
          id="propertyAddress"
          :country="formState.propertyDetails.country"
          :address="formState.propertyDetails.address"
          :addressLineTwo="formState.propertyDetails.addressLineTwo"
          :city="formState.propertyDetails.city"
          :province="formState.propertyDetails.province"
          :postalCode="formState.propertyDetails.postalCode"
          :enable-address-complete="enableAddressComplete"
        />
        <BcrosFormSectionPropertyDetails
          :property-types="propertyTypes"
          :ownership-types="ownershipTypes"
          :property-type="formState.propertyDetails.propertyType"
          :ownership-type="formState.propertyDetails.ownershipType"
          :business-license="formState.propertyDetails.businessLicense"
          :parcel-identifier="formState.propertyDetails.parcelIdentifier"
          :on-change-ownership-type="(ownershipType: string) => setOwnershipType(ownershipType)"
          :on-change-property-type="(propertyType: string) => setPropertyType(propertyType)"
          :on-change-business-license="(businessLicense: string) => setBusinessLicense(businessLicense)"
          :on-change-parcel-identifier="(parcelIdentifier: string) => setParcelIdentifier(parcelIdentifier)"
          />
        <BcrosFormSectionPropertyListingDetails
          :form-state="formState.propertyDetails"
          :enable-address-complete="enableAddressComplete"
          :add-platform="addPlatform"
          :remove-detail-at-index="removeDetailAtIndex"
          :listing-details="formState.propertyDetails.listingDetails"
        />
      </UForm>
    </div>
  </div>
</template>

<script setup lang="ts">
import { DropdownItem } from '@nuxt/ui/dist/runtime/types';

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

const setOwnershipType = (ownershipType: string) => {
  formState.propertyDetails.ownershipType = ownershipType
}

const setPropertyType = (propertyType: string) => {
  formState.propertyDetails.propertyType = propertyType
}

const setBusinessLicense = (businessLicense: string) => {
  formState.propertyDetails.businessLicense = businessLicense
}

const setParcelIdentifier = (parcelIdentifier: string) => {
  formState.propertyDetails.parcelIdentifier = parcelIdentifier
}

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
