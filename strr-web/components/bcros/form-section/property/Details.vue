<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.property-form.rentalUnitDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="parcelIdentifier" class="pr-[16px] flex-grow">
          <UInput v-model="parcelIdentifier" :placeholder="t('create-account.property-form.parcelIdentifier')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="businessLicense" class="pr-[16px] flex-grow">
          <UInput v-model="businessLicense" :placeholder="t('create-account.property-form.businessLicense')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="propertyType" class="pr-[16px] flex-grow">
          <UInput v-model="propertyType" :placeholder="t('create-account.property-form.propertyType')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="ownershipType" class="pr-[16px] flex-grow">
          <UInput v-model="ownershipType" :placeholder="t('create-account.property-form.ownershipType')" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
const { formState } = defineProps<{ formState: any }>();

const {
  unitDetails: {
    parcelIdentifier,
    businessLicense,
    propertyType,
    ownershipType
  }
} = formState
const t = useNuxtApp().$i18n.t

</script>
