<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.property-form.rentalUnitDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="parcelIdentifier" class="pr-[16px] flex-grow">
          <UInput :on-change="changeParcelIdentifier" :placeholder="t('create-account.property-form.parcelIdentifier')" />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="businessLicense" class="pr-[16px] flex-grow">
          <UInput :on-change="changeBusinessLicense" :placeholder="t('create-account.property-form.businessLicense')" />
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
              :model-value="propertyType"
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
              :model-value="ownershipType"
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

const {
  propertyTypes,
  ownershipTypes,
  propertyType,
  ownershipType,
  businessLicense,
  parcelIdentifier
} = defineProps<{ 
  propertyTypes: DropdownItem[][],
  ownershipTypes: DropdownItem[][],
  propertyType: string | undefined,
  ownershipType: string | undefined,
  businessLicense: string | undefined,
  parcelIdentifier: string | undefined,
}>()

const emit = defineEmits<{
  changePropertyType: [propertyType: string],
  changeOwnershipType: [ownershipType: string],
  changeBusinessLicense: [businessLicense: string],
  changeParcelIdentifier: [parcelIdentifier: string],
}>()

const t = useNuxtApp().$i18n.t

</script>
