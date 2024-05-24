<template>
  <div data-cy="create-account-page" class="relative h-full">
    <div class="mb-[180px] bg-white rounded-[4px]">
      <div class="bg-bcGovColor-gray2 rounded-t-[4px]">
        <p class="px-[40px] py-[15px] font-bold">
          {{ t('create-account.contact.subtitle') }}
        </p>
      </div>
      <UForm :schema="propertyDetailsSchema" :state="formState.propertyDetails">
        <BcrosFormSectionPropertyAddress :form-state="formState.propertyDetails" />
        <BcrosFormSectionPropertyDetails
          :form-state="formState.propertyDetails"
          :on-change-ownership-type="(ownershipType: string) => changeOwnershipType(ownershipType)"
          :on-change-property-type="(propertyType: string) => changePropertyType(propertyType)"
          :on-change-business-license="(businessLicense: string) => changeBusinessLicense(businessLicense)"
          :on-change-parcel-identifier="(parcelIdentifier: string) => changeParcelIdentifier(parcelIdentifier)"
          />
        <BcrosFormSectionPropertyListingDetails :form-state="formState.propertyDetails" />
      </UForm>
    </div>
  </div>
</template>

<script setup lang="ts">

const t = useNuxtApp().$i18n.t

const isValid = ref(false)

watch(formState.propertyDetails, () => {
  isValid.value = propertyDetailsSchema.safeParse(formState.propertyDetails).success
})

const changeOwnershipType = (ownershipType: string) => {
  formState.propertyDetails.ownershipType = ownershipType
}

const changePropertyType = (propertyType: string) => {
  formState.propertyDetails.propertyType = propertyType
}

const changeBusinessLicense = (businessLicense: string) => {
  formState.propertyDetails.businessLicense = businessLicense
}

const changeParcelIdentifier = (parcelIdentifier: string) => {
  formState.propertyDetails.parcelIdentifier = parcelIdentifier
}

const emit = defineEmits<{
  validatePage: [isValid: boolean]
}>()

</script>
