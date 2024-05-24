<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.property-form.rentalUnitDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="parcelIdentifier" class="pr-[16px] flex-grow">
          <UInput v-model="formState.parcelIdentifier" :placeholder="t('create-account.property-form.parcelIdentifier')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="businessLicense" class="pr-[16px] flex-grow">
          <UInput v-model="formState.businessLicense" :placeholder="t('create-account.property-form.businessLicense')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="propertyType" class="pr-[16px] flex-grow">
          <UDropdown
            :items="propertyTypes"
            class="w-full"
            :popper="{
              placement: 'bottom-start',
            }"
          >
            <UInput
              v-model="formState.propertyType"
              class="w-full"
              color="white"
              :placeholder="t('create-account.property-form.propertyType')"
              trailing-icon="i-heroicons-chevron-down-20-solid"
            />
          </UDropdown>
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="ownershipType" class="pr-[16px] flex-grow">
          <UDropdown
            :items="ownershipTypes" 
            class="w-full"
            :popper="{
              placement: 'bottom-start',
            }"
          >
            <UInput
              v-model="formState.ownershipType"
              class="w-full"
              color="white"
              :placeholder="t('create-account.property-form.ownershipType')"
              trailing-icon="i-heroicons-chevron-down-20-solid"
            />
          </UDropdown>
        </UFormGroup>
      </div>
    </BcrosFormSection>
  </div>
</template>

<script setup lang="ts">
import { DropdownItem } from '@nuxt/ui/dist/runtime/types'

const { formState } = defineProps<{ formState: any }>()

const t = useNuxtApp().$i18n.t

const propertyTypes: DropdownItem[][] = [
  [
    { 
      label: 'Portion of principal residence',
      click: () => formState.propertyType = 'Portion of principal residence'
     },
    {
       label: 'Entire principal residence',
      click: () => formState.propertyType = 'Entire principal residence'
    },
    {
       label: 'Secondary suite',
      click: () => formState.propertyType = 'Secondary suite'
    },
    {
       label: 'Accessory dwelling unit',
      click: () => formState.propertyType = 'Accessory dwelling unit'
    },
    {
       label: 'Investment property',
      click: () => formState.propertyType = 'Investment property'
    }
  ]
]

const ownershipTypes: DropdownItem[][] = [
  [
    {
      label: 'Rent',
      click: () => formState.propertyType = 'Rent'
    },
    {
      label: 'Own',
      click: () => formState.propertyType = 'Own'
    },
    {
      label: 'Co-own',
      click: () => formState.propertyType = 'Co-own'
    }
  ]
]

</script>
