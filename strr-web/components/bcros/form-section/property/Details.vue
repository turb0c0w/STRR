<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection title="Mailing Address">
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="parcelIdentifier" class="pr-[16px] flex-grow">
          <UInput v-model="parcelIdentifier" placeholder="Parcel Identifier (Optional)" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="businessLicense" class="pr-[16px] flex-grow">
          <UInput v-model="businessLicense" placeholder="Local Government Business Licence (Optional)" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="propertyType" class="pr-[16px] flex-grow">
          <UInput v-model="propertyType" placeholder="Type of Property" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px]">
        <UFormGroup name="ownershipType" class="pr-[16px] flex-grow">
          <UInput v-model="ownershipType" placeholder="Ownership Type" />
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { formState } from '@/stores/strr'

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
