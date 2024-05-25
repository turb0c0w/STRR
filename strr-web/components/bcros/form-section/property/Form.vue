<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="mb-[180px] bg-white rounded-[4px]">
      <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
        <p class="px-[40px] py-[15px] font-bold">
          {{ t('create-account.contact.subtitle') }}
        </p>
      </div>
      <UForm :schema="propertyDetailsSchema" :state="formState.propertyDetails">
        <BcrosFormSectionPropertyAddress :form-state="formState.propertyDetails" id="propertyAddress"/>
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
        <BcrosFormSectionPropertyListingDetails :form-state="formState.propertyDetails" />
      </UForm>
    </div>
  </div>
</template>

<script setup lang="ts">
import { DropdownItem } from '@nuxt/ui/dist/runtime/types';


const t = useNuxtApp().$i18n.t

const isValid = ref(false)

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
