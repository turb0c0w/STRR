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
          <UDropdown :items="propertyTypes" v-model="propertyType" class="w-full">
            <UInput
              class="w-full"
              color="white" 
              :label="t('create-account.property-form.propertyType')"
              trailing-icon="i-heroicons-chevron-down-20-solid"
            />
          </UDropdown>
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="ownershipType" class="pr-[16px] flex-grow">
          <UDropdown :items="ownershipTypes" v-model="ownershipType" class="w-full">
            <UInput
              class="w-full"
              color="white" 
              :label="t('create-account.property-form.ownershipType')"
              trailing-icon="i-heroicons-chevron-down-20-solid"
            />
          </UDropdown>
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { DropdownItem } from '@nuxt/ui/dist/runtime/types';

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

const propertyTypes: DropdownItem[][] = [
  [
    {label: "Portion of principal residence"},
    {label: "Entire principal residence"},
    {label: "Secondary suite"},
    {label: "Accessory dwelling unit"},
    {label: "Investment property"}
  ]
]

const ownershipTypes: DropdownItem[][] = [
  [
    {label: "Rent"},
    {label: "Own"},
    {label: "Co-own"}
  ]
]


</script>
