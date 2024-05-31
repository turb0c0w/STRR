<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="desktop:mb-[180px] mobile:mb-[32px] bg-white rounded-[4px]">
      <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
        <p class="px-[40px] py-[15px] font-bold">
          {{ t('create-account.property-form.subtitle') }}
        </p>
      </div>
      <UForm form="form" :schema="propertyDetailsSchema" :state="formState.propertyDetails">
        <BcrosFormSectionPropertyAddress
          id="propertyAddress"
          v-model:nickname="formState.propertyDetails.nickname"
          v-model:country="formState.propertyDetails.country"
          v-model:address="formState.propertyDetails.address"
          v-model:address-line-two="formState.propertyDetails.addressLineTwo"
          v-model:city="formState.propertyDetails.city"
          v-model:province="formState.propertyDetails.province"
          v-model:postal-code="formState.propertyDetails.postalCode"
          :enable-address-complete="enableAddressComplete"
          default-country-iso2="CA"
        />
        <BcrosFormSectionPropertyDetails
          v-model:property-type="formState.propertyDetails.propertyType"
          v-model:ownership-type="formState.propertyDetails.ownershipType"
          v-model:business-license="formState.propertyDetails.businessLicense"
          v-model:parcel-identifier="formState.propertyDetails.parcelIdentifier"
          :property-types="propertyTypes"
          :ownership-types="ownershipTypes"
        />
        <BcrosFormSectionPropertyListingDetails
          v-model:listing-details="formState.propertyDetails.listingDetails"
          :enable-address-complete="enableAddressComplete"
          :add-platform="addPlatform"
          :remove-detail-at-index="removeDetailAtIndex"
        />
      </UForm>
    </div>
  </div>
</template>

<script setup lang="ts">
const { isComplete } = defineProps<{
  isComplete: boolean
}>()

const {
  address: canadaPostAddress,
  enableAddressComplete
} = useCanadaPostAddress()

watch(canadaPostAddress, (newAddress) => {
  if (newAddress) {
    if (newAddress.region === 'BC') {
      formState.propertyDetails.address = newAddress.street
      formState.propertyDetails.addressLineTwo = newAddress.streetAdditional
      formState.propertyDetails.country = newAddress.country
      formState.propertyDetails.city = newAddress.city
      formState.propertyDetails.province = newAddress.region
      formState.propertyDetails.postalCode = newAddress.postalCode
    } else {
      // replace with validation error?
      alert('Please choose an address in BC')
    }
  }
})

const t = useNuxtApp().$i18n.t

const isValid = ref(false)

const addPlatform = () => {
  formState.propertyDetails.listingDetails.push({ url: '' })
}

const removeDetailAtIndex = (index: number) => {
  formState.propertyDetails.listingDetails.splice(index, 1)
}

watch(formState.propertyDetails, () => {
  isValid.value = propertyDetailsSchema.safeParse(formState.propertyDetails).success
})

defineEmits<{
  validatePage: [isValid: boolean]
}>()

const propertyTypes: string[] = [
  t('create-account.property-form.primaryDwelling'),
  t('create-account.property-form.secondarySuite'),
  t('create-account.property-form.accessory'),
  t('create-account.property-form.float'),
  t('create-account.property-form.other')
]

const ownershipTypes: string[] = [
  t('create-account.property-form.rent'),
  t('create-account.property-form.own'),
  t('create-account.property-form.other')
]

const form = ref()

watch(form, () => {
  if (form.value && isComplete) { form.value.validate() }
})

</script>
