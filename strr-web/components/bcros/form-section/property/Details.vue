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
      label: t('create-account.property-form.primaryDwelling'),
      click: () => formState.propertyType = t('create-account.property-form.primaryDwelling')
    },
    { 
      label: t('create-account.property-form.secondarySuite'),
      click: () => formState.propertyType = t('create-account.property-form.secondarySuite')
    }, 
    { 
      label: t('create-account.property-form.accessory'),
      click: () => formState.propertyType = t('create-account.property-form.accessory')
    },
    { 
      label: t('create-account.property-form.float'),
      click: () => formState.propertyType = t('create-account.property-form.float')
    },
    { 
      label: t('create-account.property-form.other'),
      click: () => formState.propertyType = t('create-account.property-form.other')
    },
  ]
]

const ownershipTypes: DropdownItem[][] = [
  [
    { 
      label: t('create-account.property-form.rent'),
      click: () => formState.propertyType = t('create-account.property-form.rent')
    },
    { 
      label: t('create-account.property-form.own'),
      click: () => formState.propertyType = t('create-account.property-form.own')
    },
    { 
      label: t('create-account.property-form.other'),
      click: () => formState.propertyType = t('create-account.property-form.coown')
    },
  ]
]

</script>
