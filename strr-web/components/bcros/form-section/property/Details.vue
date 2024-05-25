<template>
  <div data-cy="form-section-contact-info">
    <BcrosFormSection :title="t('create-account.property-form.rentalUnitDetails')">
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="parcelIdentifier" class="pr-[16px] flex-grow">
          <UInput
            v-model="parcelIdentifier"
            :placeholder="t('create-account.property-form.parcelIdentifier')"
          />
        </UFormGroup>
      </div>
      <div class="flex flex-row justify-between w-full mb-[40px] mobile:mb-[16px]">
        <UFormGroup name="businessLicense" class="pr-[16px] flex-grow">
          <UInput
            :placeholder="t('create-account.property-form.businessLicense')"
          />
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
              v-model="propertyType"
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
              v-model="ownershipType"
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

const t = useNuxtApp().$i18n.t

const propertyType = defineModel('propertyType')
const ownershipType = defineModel('ownershipType')
const businessLicense = defineModel('businessLicense')
const parcelIdentifier = defineModel('parcelIdentifier')

const {
  propertyTypes,
  ownershipTypes
} = defineProps<{
  propertyTypes: DropdownItem[][],
  ownershipTypes: DropdownItem[][]
}>()
</script>
